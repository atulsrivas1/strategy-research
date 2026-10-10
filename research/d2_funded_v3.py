"""D2 long-history adaptation: exact IDs/prices, bounded cash, no source certification."""
from datetime import date, datetime
from fractions import Fraction as F
import random
import math
import stored_prices as stored
import lossless_inputs as inputs
import funded_split_ledger as ledger
import split_actions as actions


def protocol():
    return dict(version='d2-funded-v3', formation=252, skip=21, top=3, entry_delay=2, hold=5,
                capital='1', fees=['0.001','0.002','0.003'], minimum_decisions=200,
                minimum_blocks=40, minimum_months=10, minimum_securities=10,
                maximum_slot_share='0.25', bootstrap_block=20, bootstrap_draws=1000, seed=4102,
                input_start='2024-05-23', input_end='2026-06-09',
                decision_start='2025-06-02', decision_end='2026-05-29',
                symbols=['AMZN','GOOGL','META','NVDA','JPM','BAC','XOM','CVX','JNJ','PFE','PG','KO','HD','WMT','CAT','UNH','DIS','CSCO'],
                price_basis='raw stored binary64 with causal pure-split share normalization; original precision unknown',
                action_basis='raw_share_units; known issuer splits only; other actions unknown',
                experiment_id='D2-FUNDED-REPAIR-1',
                scope='potentially exposed development only', final_access=False,
                experiment_budget=1, arm_fee_configurations=9,
                primary='scanner-minus-equal-cohort', context='fixed rejected five-session veto diagnostic; market unknown')


def exact_json(value):
    if isinstance(value,F):
        return f'{value.numerator}/{value.denominator}'
    if isinstance(value,dict):
        return {key:exact_json(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):
        return [exact_json(item) for item in value]
    return value


def available(row, clock):
    return row is not None and (row['available_at'] is None or datetime.fromisoformat(row['available_at'].replace('Z','+00:00'))<=clock)


def select(bars, calendar, i, identities, events=()):
    p=protocol()
    if type(i) is not int or not p['formation']<=i<len(calendar):
        raise ValueError('formation/session boundary')
    clock=datetime.fromisoformat(calendar[i]+'T23:59:59+00:00')
    scores={};states={}
    for identity in identities:
        history=[bars.get((identity,day)) for day in calendar[i-p['formation']:i+1]]
        if not all(available(row,clock) for row in history):
            return dict(status='unresolved',reason='incomplete/late complete-cohort history',selected=[],stock={})
        needed=[history[-1-p['skip']],history[0],history[-1],history[-6]]
        adjusted=[actions.price(row['close'],events,identity,row['date'],calendar[i],clock.isoformat()) for row in needed]
        if any(value is None for value in adjusted):
            return dict(status='unresolved',reason='known effective split has unknown/late evidence',selected=[],stock={})
        scores[identity]=adjusted[0]/adjusted[1]-1
        change=adjusted[2]-adjusted[3]
        states[identity]='aligned' if change>0 else 'conflicting' if change<0 else 'neutral'
    ranked=sorted(scores,key=lambda identity:(-scores[identity],identity))
    if scores[ranked[p['top']-1]]==scores[ranked[p['top']]]:
        return dict(status='unresolved',reason='selection boundary tie',selected=[],stock=states)
    return dict(status='complete exploratory ranking',selected=ranked[:p['top']],stock=states,
                scores={str(key):str(value) for key,value in scores.items()})


def interval(values):
    if not values:
        return None
    p=protocol();n=len(values);rng=random.Random(p['seed']);samples=[]
    # Exact common-denominator integer sums avoid repeated large-rational GCDs.
    denominator=math.lcm(*(value.denominator for value in values))
    integers=[value.numerator*(denominator//value.denominator) for value in values]
    for _ in range(p['bootstrap_draws']):
        draw=[]
        while len(draw)<n:
            start=rng.randrange(n)
            draw.extend(integers[(start+j)%n] for j in range(p['bootstrap_block']))
        samples.append(sum(draw[:n]))
    samples.sort()
    return [F(samples[24],denominator),F(samples[974],denominator)]


def classify(delta, bounds, usable, support, stress):
    if not usable:
        return 'inconclusive: unresolved observations/funding'
    if not support:
        return 'inconclusive: insufficient temporal/security support'
    if delta<=0 and bounds[1]<0:
        return 'rejected tested scanner'
    if delta>0 and bounds[0]>0 and all(value>0 for value in stress):
        return 'promising exploratory under assumptions'
    return 'inconclusive: uncertainty or stress criterion'


def profits(arm, decisions):
    output={day:F(0) for day in decisions}
    for lot in arm['lots']:
        if lot['state']=='closed':
            output[lot['day']]+=lot['proceeds']-lot['notional']-lot['entry_fee']-lot['exit_fee']
    return output


def evaluate(bundle):
    p=protocol()
    if bundle.get('kind') not in ('synthetic','development') or bundle.get('final_access') is not False:
        raise ValueError('explicit nonfinal bundle required')
    calendar=bundle['calendar'];decisions=bundle['decisions'];universe=bundle['universe']
    if not calendar or list(calendar)!=sorted(set(calendar)) or any(date.fromisoformat(day).isoformat()!=day for day in calendar):
        raise ValueError('canonical unique increasing calendar required')
    if not decisions or decisions!=sorted(set(decisions)) or len(decisions)>252 or not set(decisions).issubset(calendar):
        raise ValueError('bounded unique decision schedule required')
    identities=[row['instrument_id'] for row in universe]
    if len(universe)!=18 or len(set(identities))!=18 or any(type(identity)is not int or identity<=0 for identity in identities) or {row['symbol'] for row in universe}!=set(p['symbols']):
        raise ValueError('exact frozen cohort identity map required')
    if bundle['kind']=='development':
        if calendar[0]<p['input_start'] or calendar[-1]>p['input_end']:
            raise ValueError('outside development input bounds')
        if decisions!=[day for day in calendar if p['decision_start']<=day<=p['decision_end']]:
            raise ValueError('do not select convenient decision subsets')
    if bundle['kind']=='development':
        if bundle.get('price_basis')!=p['price_basis']:
            raise ValueError('explicit stored binary64 proxy basis required')
        stored.verify(bundle['bars'])
    bars_list=inputs.normalize(bundle['bars'])
    if len({row['units'] for row in bars_list})>1:
        raise ValueError('mixed price units require an explicit conversion adapter')
    names={row['instrument_id']:row['symbol'] for row in universe}
    if any(row['instrument_id'] not in names or row['symbol']!=names[row['instrument_id']] or row['date'] not in calendar for row in bars_list):
        raise ValueError('bar outside frozen cohort/calendar')
    if bundle.get('action_basis')!=p['action_basis'] or not isinstance(bundle.get('split_events'),list):
        raise ValueError('explicit raw action basis and split-event register required')
    events=actions.normalize(bundle['split_events'],names)
    bars={(row['instrument_id'],row['date']):row for row in bars_list}
    planned=[];benchmark=[];screens=[];veto=[];selected=[]
    # Equal initial-cash tranches reserve maximum modeled fees before outcomes.
    tranche=F(p['capital'])/(len(decisions)*(1+F(p['fees'][-1])))
    for day in decisions:
        i=calendar.index(day);entry=i+p['entry_delay'];exit=entry+p['hold']
        if i<p['formation'] or exit>=len(calendar):
            raise ValueError('insufficient formation or holding calendar')
        ranking=select(bars,calendar,i,identities,events)
        screens.append(dict(day=day,market='unknown',**ranking))
        # Benchmark is planned independently, even on unresolved scanner dates.
        for identity in identities:
            benchmark.append(dict(id=f'{day}:{identity}',security=identity,day=day,decision=i,entry=entry,exit=exit,notional=tranche/18))
        for identity in ranking['selected']:
            order=dict(id=f'{day}:{identity}',security=identity,day=day,decision=i,entry=entry,exit=exit,notional=tranche/3)
            planned.append(order);selected.append(identity)
            if ranking['stock'][identity]=='conflicting':
                veto.append(order['id'])
    opens={(i,identity):row['open'] for (identity,day),row in bars.items() for i in [calendar.index(day)]}
    marks={(i,identity):row['close'] for (identity,day),row in bars.items() for i in [calendar.index(day)]}
    costs=[];primary_values=[];base_arm=None;control=None
    for fee in p['fees']:
        pair=ledger.paired(calendar,planned,opens,opens,marks,p['capital'],fee,veto,events)
        equal=ledger.simulate(calendar,benchmark,opens,opens,marks,p['capital'],fee,events=events)
        scanner=pair['baseline'];candidate=pair['candidate']
        original_schedule={order['day'] for order in scanner['orders']}
        usable=all(arm['complete'] and arm['funding_feasible'] and all(row['nav'] is not None for row in arm['daily']) for arm in (scanner,equal)) and original_schedule==set(decisions)
        scanner_profit=profits(scanner,decisions);equal_profit=profits(equal,decisions)
        daily=[scanner_profit[day]-equal_profit[day] for day in decisions]
        costs.append(dict(fee=fee,usable=usable,scanner_nav=scanner['daily'][-1]['nav'],benchmark_nav=equal['daily'][-1]['nav'],candidate_nav=candidate['daily'][-1]['nav'],scanner_minus_benchmark=sum(daily,F(0)),context_matched=pair['isolated_overlay_comparable']))
        if fee==p['fees'][0]:
            primary_values=daily;base_arm=scanner;control=pair
    counts={identity:selected.count(identity) for identity in set(selected)}
    concentration=max(counts.values())/F(len(selected)) if selected else None
    support=dict(decisions=len(decisions),disjoint_five_session_blocks=len(decisions)//5,months=len({day[:7] for day in decisions}),selected_securities=len(counts),maximum_slot_share=concentration)
    supported=(support['decisions']>=p['minimum_decisions'] and support['disjoint_five_session_blocks']>=p['minimum_blocks'] and support['months']>=p['minimum_months'] and support['selected_securities']>=p['minimum_securities'] and concentration is not None and concentration<=F(p['maximum_slot_share']))
    bounds=interval(primary_values)
    usable=all(row['usable'] for row in costs) and all(row['status']=='complete exploratory ranking' for row in screens)
    verdict=classify(costs[0]['scanner_minus_benchmark'],bounds,usable,supported,[row['scanner_minus_benchmark'] for row in costs[1:]])
    avoided=sacrificed=0
    for lot in base_arm['lots']:
        if lot['id'] in veto and lot['state']=='closed':
            profit=lot['proceeds']-lot['notional']-lot['entry_fee']-lot['exit_fee']
            avoided+=profit<0;sacrificed+=profit>0
    return exact_json(dict(protocol=p,screens=screens,scanner_orders=planned,benchmark_orders=benchmark,
                           costs=costs,primary_interval=bounds,support=support,support_sufficient=supported,
                           verdict='synthetic witness only' if bundle['kind']=='synthetic' else verdict,
                           point_criterion='positive' if costs[0]['scanner_minus_benchmark']>0 else 'failed',
                           ledger=control,diagnostic=dict(vetoed=len(veto),avoided_losses=avoided,sacrificed_winners=sacrificed,market='unknown',promotion_allowed=False),
                           split_events=events,action_coverage='known pure splits only; remaining events unknown',
                           final_access=False,source_qualification='unverified',clock_basis='modeled UTC day end',funded_accounting=True))
