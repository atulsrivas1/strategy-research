"""D2 reusable capital adaptation; explicit modeled settlement admission only."""
from fractions import Fraction as F
from decimal import Decimal,localcontext
import hashlib,json,random
from datetime import date
import d2_funded_v3 as prior
import stored_prices as stored
import lossless_inputs as inputs
import split_actions as actions
import sleeve_ledger as ledger


def protocol():
    p=prior.protocol()
    p.update(version='d2-sleeves-v1',experiment_id='D2-SLEEVES-DEV-1',capital_policy='seven independent sleeves; prior-close budget; maturity-close receivables',settlement_basis='explicit frozen eligibility map; certified metadata or declared exploratory proxy',log_precision=50,log_check_tolerance='1e-12',uncertainty='paired daily log-NAV; circular20 active sessions',sleeves=7)
    return p


def log_ratio(a,b):
    a,b=F(a),F(b)
    if a<=0 or b<=0:raise ValueError('positive known NAV required')
    ratio=a/b
    with localcontext() as ctx:
        ctx.prec=50
        return (Decimal(ratio.numerator)/Decimal(ratio.denominator)).ln()


def log_interval(values):
    if not values:return None
    # Freeze each Decimal as an exact rational, including sums and resampling.
    values=[F(v) for v in values];rng=random.Random(4102);samples=[]
    for _ in range(1000):
        draw=[]
        while len(draw)<len(values):
            start=rng.randrange(len(values));draw.extend(values[(start+j)%len(values)] for j in range(20))
        samples.append(sum(draw[:len(values)],F(0)))
    samples.sort();return [samples[24],samples[974]]


def settlement_check(meta,calendar,decisions):
    if meta.get('basis')!=protocol()['settlement_basis'] or not meta.get('source') or not meta.get('clock_assumption'):
        raise ValueError('explicit settlement source/clock proxy required')
    digest=hashlib.sha256(json.dumps(calendar,separators=(',',':')).encode()).hexdigest()
    if meta.get('price_calendar_sha256')!=digest or set(meta.get('maturities',{}))!=set(decisions):
        raise ValueError('exact calendar and complete decision maturity map required')
    for day,value in meta['maturities'].items():
        exit=calendar.index(day)+7
        if value is not None and (type(value) is not int or value<=exit):raise ValueError('settlement close must follow modeled exit')


def metrics(arm):
    peak=F(1);drawdown=F(0);exposure=[]
    for d in arm['daily']:
        if d['nav'] is None or d['nav']<=0:return dict(known=False)
        peak=max(peak,d['nav']);drawdown=min(drawdown,d['nav']/peak-1);exposure.append(d['gross']/d['nav'])
    purchases={s:sum((l['notional'] for l in arm['lots'] if l['security']==s),F(0)) for s in {l['security'] for l in arm['lots']}}
    total=sum(purchases.values(),F(0))
    return dict(known=True,terminal_nav=arm['daily'][-1]['nav'],terminal_cash=arm['daily'][-1]['cash'],terminal_receivables=arm['daily'][-1]['receivables'],maximum_drawdown=drawdown,peak_gross_NAV_exposure=max(exposure),mean_gross_NAV_exposure=sum(exposure,F(0))/len(exposure),fees=sum((l['entry_fee']+l.get('exit_fee',F(0)) for l in arm['lots']),F(0)),turnover=sum((l['notional']+l.get('proceeds',F(0)) for l in arm['lots']),F(0)),maximum_security_purchase_share=None if not total else max(purchases.values())/total,filled_orders=len(arm['lots']),unfilled_groups=sum(g['state']!='entered' for g in arm['groups']),censored_lots=sum(l['state']!='closed' for l in arm['lots']))


def evaluate(bundle):
    p=protocol()
    if bundle.get('kind') not in ('synthetic','development') or bundle.get('final_access') is not False:raise ValueError('explicit development only')
    calendar=bundle['calendar'];decisions=bundle['decisions'];universe=bundle['universe'];ids=[u['instrument_id'] for u in universe]
    if len(ids)!=18 or len(set(ids))!=18 or any(type(s) is not int or s<=0 for s in ids) or {u['symbol'] for u in universe}!=set(p['symbols']):raise ValueError('complete frozen cohort required')
    if not calendar or calendar!=sorted(set(calendar)) or not decisions or decisions!=sorted(set(decisions)) or not set(decisions).issubset(calendar):raise ValueError('canonical complete chronology required')
    if len(decisions)>252 or any(date.fromisoformat(d).isoformat()!=d for d in calendar):raise ValueError('bounded canonical decisions required')
    if bundle['kind']=='development' and (calendar[0]!=p['input_start'] or calendar[-1]!=p['input_end'] or decisions!=[d for d in calendar if p['decision_start']<=d<=p['decision_end']]):raise ValueError('frozen development bounds required')
    settlement_check(bundle['settlement'],calendar,decisions)
    if bundle['kind']=='development':
        if bundle.get('price_basis')!=p['price_basis']:raise ValueError('explicit stored binary64 price basis required')
        stored.verify(bundle['bars'])
    rows=inputs.normalize(bundle['bars'])
    names={u['instrument_id']:u['symbol'] for u in universe}
    if len({r['units'] for r in rows})!=1 or any(r['instrument_id'] not in names or r['symbol']!=names[r['instrument_id']] or r['date'] not in calendar for r in rows):raise ValueError('cohort/calendar/unit mismatch')
    if bundle.get('action_basis')!=p['action_basis']:raise ValueError('raw share action basis required')
    events=actions.normalize(bundle['split_events'],names);bars={(r['instrument_id'],r['date']):r for r in rows};positions={d:i for i,d in enumerate(calendar)}
    opens={(positions[d],s):r['open'] for (s,d),r in bars.items()};marks={(positions[d],s):r['close'] for (s,d),r in bars.items()}
    scanner=[];benchmark=[];screens=[];veto=set();selected=[]
    for j,day in enumerate(decisions):
        i=positions[day]
        if i<252 or i+7>=len(calendar):raise ValueError('formation/holding calendar incomplete')
        ranking=prior.select(bars,calendar,i,ids,events);screens.append(dict(day=day,market='unknown',**ranking))
        g=dict(id=day,decision=i,entry=i+2,exit=i+7,sleeve=j%7,settlement_close=bundle['settlement']['maturities'][day])
        scanner.append(dict(g,securities=ranking['selected']));benchmark.append(dict(g,securities=ids))
        selected.extend(ranking['selected'])
        veto.update((day,s) for s in ranking['selected'] if ranking['stock'][s]=='conflicting')
    costs=[];arms=[];first=positions[decisions[0]]+2;last=positions[decisions[-1]]+7
    for fee in p['fees']:
        pair=ledger.paired(calendar,scanner,opens,marks,p['capital'],fee,events,veto);equal=ledger.simulate(calendar,benchmark,opens,marks,p['capital'],fee,events)
        base=pair['baseline'];candidate=pair['candidate'];usable=base['complete'] and equal['complete'] and all(s['status']=='complete exploratory ranking' for s in screens)
        logs=[]
        if usable:
            logs=[F(log_ratio(base['daily'][t]['nav'],base['daily'][t-1]['nav']))-F(log_ratio(equal['daily'][t]['nav'],equal['daily'][t-1]['nav'])) for t in range(first,last+1)]
        costs.append(dict(fee=fee,primary_usable=usable,context_usable=pair['isolated_overlay_comparable'],scanner=metrics(base),benchmark=metrics(equal),candidate=metrics(candidate),relative_wealth=None if not usable else base['daily'][-1]['nav']/equal['daily'][-1]['nav']-1,paired_log_point=None if not usable else sum(logs,F(0))))
        arms.append(dict(pair=pair,benchmark=equal,logs=logs))
    counts={s:selected.count(s) for s in set(selected)};concentration=None if not selected else F(max(counts.values()),len(selected))
    support=dict(decisions=len(decisions),disjoint_five_session_blocks=len(decisions)//5,months=len({d[:7] for d in decisions}),selected_securities=len(counts),maximum_slot_share=concentration)
    supported=len(decisions)>=200 and len(decisions)//5>=40 and support['months']>=10 and len(counts)>=10 and concentration is not None and concentration<=F('.25')
    interval=log_interval(arms[0]['logs']);usable=all(c['primary_usable'] for c in costs)
    verdict='inconclusive: unresolved observations/funding' if not usable else prior.classify(costs[0]['paired_log_point'],interval,True,supported,[c['paired_log_point'] for c in costs[1:]])
    losses=winners=0
    if arms[0]['pair']['isolated_overlay_comparable']:
        for lot in arms[0]['pair']['baseline']['lots']:
            if (lot['group'],lot['security']) in veto:
                net=lot['proceeds']-lot['notional']-lot['entry_fee']-lot['exit_fee'];losses+=net<0;winners+=net>0
    return prior.exact_json(dict(protocol=p,screens=screens,costs=costs,ledger=arms[0]['pair'],benchmark_ledger=arms[0]['benchmark'],primary_logs=arms[0]['logs'],primary_log_interval=interval,active_sessions=last-first+1,support=support,support_sufficient=supported,verdict='synthetic witness only' if bundle['kind']=='synthetic' else verdict,diagnostic=dict(promotion_allowed=False,matched=arms[0]['pair']['isolated_overlay_comparable'],avoided_losses=losses if arms[0]['pair']['isolated_overlay_comparable'] else None,sacrificed_winners=winners if arms[0]['pair']['isolated_overlay_comparable'] else None),final_access=False))
