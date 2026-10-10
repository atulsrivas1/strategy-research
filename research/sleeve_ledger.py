"""Seven independent research sleeves; exact cash, share and receivable accounting."""
from fractions import Fraction as F
from funded_ledger import exact
import split_actions as actions


def validate(calendar, groups):
    if not calendar or list(calendar)!=sorted(set(calendar)):
        raise ValueError('unique increasing calendar required')
    if len({g['id'] for g in groups})!=len(groups):raise ValueError('duplicate group')
    entries=set()
    for g in groups:
        d,e,x,s=(g[k] for k in ('decision','entry','exit','sleeve'))
        if any(type(v) is not int for v in (d,e,x,s)) or not 0<=d<e<x<len(calendar) or not 0<=s<7:
            raise ValueError('causal admitted sleeve schedule required')
        m=g['settlement_close']
        if m is not None and (type(m) is not int or m<=x):raise ValueError('settlement after exit required')
        ids=g['securities']
        if len(ids)!=len(set(ids)) or any(type(v) is not int or v<=0 for v in ids):raise ValueError('unique stable securities required')
        if (s,e) in entries:raise ValueError('duplicate sleeve entry')
        entries.add((s,e))


def simulate(calendar, groups, opens, marks, capital='1', fee='0.001', events=(), reference=None, veto=()):
    groups=[dict(g) for g in groups];validate(calendar,groups)
    cost=exact(fee);reserve=F('.003')
    if cost>reserve:raise ValueError('fee exceeds fixed reserve')
    events=actions.normalize(events,{e['instrument_id']:e['symbol'] for e in events})
    cash=[exact(capital,True)/7 for _ in range(7)]
    lots=[];receipts=[];daily=[];budgets={};orders=[];log=[];veto=set(veto)
    allowed={(g['id'],s) for g in groups for s in g['securities']}
    if not veto.issubset(allowed):raise ValueError('unknown veto order')
    if reference is not None and set(reference)!={g['id'] for g in groups}:raise ValueError('complete fixed reference schedule required')
    for g in groups:
        g['state']='planned'
    for t,day in enumerate(calendar):
        for event,ratio in actions.session_events(events,day,day+'T00:00:00Z'):
            for lot in lots:
                if lot['security']!=event['instrument_id'] or lot['state']=='closed':continue
                if ratio is None or lot['state']=='unresolved_action':lot['state']='unresolved_action'
                else:lot['quantity']*=ratio
                log.append(dict(event=event['id'],lot=lot['id'],session=t,cashflow=F(0),state=lot['state']))
        for lot in lots:
            if lot['state']!='open' or lot['exit']!=t:continue
            price=opens.get((t,lot['security']))
            if price is None:lot['state']='censored';continue
            gross=lot['quantity']*exact(price,True);net=gross*(1-cost)
            lot.update(state='closed',proceeds=gross,exit_fee=gross*cost)
            receipts.append(dict(lot=lot['id'],sleeve=lot['sleeve'],amount=net,maturity=lot['settlement_close'],state='pending'))
        for g in groups:
            if g['entry']!=t:continue
            budget=budgets.get(g['id']);securities=g['securities'];kept=[s for s in securities if (g['id'],s) not in veto]
            if budget is None or not securities:g['state']='unresolved_budget';continue
            n=budget/len(securities)
            if any(opens.get((t,s)) is None for s in kept):g['state']='unfilled_missing_price';continue
            required=n*len(kept)*(1+cost)
            if required>cash[g['sleeve']]:g['state']='unfilled_cash';continue
            g['state']='entered'
            for s in securities:
                order=dict(id=g['id']+':'+str(s),group=g['id'],security=s,sleeve=g['sleeve'],decision=g['decision'],entry=t,exit=g['exit'],settlement_close=g['settlement_close'],notional=n,state='vetoed' if (g['id'],s) in veto else 'entered')
                orders.append(order)
                if order['state']=='vetoed':continue
                cash[g['sleeve']]-=n*(1+cost)
                lots.append(dict(order,quantity=n/exact(opens[t,s],True),state='open',entry_fee=n*cost))
        # Maturity credits occur at close, after open entries, before next budget.
        for receipt in receipts:
            if receipt['state']=='pending' and receipt['maturity']==t:
                cash[receipt['sleeve']]+=receipt['amount'];receipt['state']='settled'
        for g in groups:
            if g['entry']-1!=t:continue
            sleeve=g['sleeve']
            blocked=any(l['sleeve']==sleeve and l['state']!='closed' for l in lots) or any(r['sleeve']==sleeve and r['state']=='pending' for r in receipts)
            if blocked or cash[sleeve]<=0:budget=None
            elif reference is None:budget=cash[sleeve]/(1+reserve)
            else:
                value=reference.get(g['id']);budget=None if value is None else exact(value,True)
            budgets[g['id']]=budget
        values=[]
        for lot in lots:
            if lot['state']=='closed':continue
            price=marks.get((t,lot['security']))
            values.append(None if price is None or lot['state']=='unresolved_action' else lot['quantity']*exact(price,True))
        gross=None if any(x is None for x in values) else sum(values,F(0))
        pending=sum((r['amount'] for r in receipts if r['state']=='pending'),F(0))
        assert all(x>=0 for x in cash),'no borrowing'
        daily.append(dict(session=t,cash=sum(cash,F(0)),sleeve_cash=list(cash),receivables=pending,gross=gross,nav=None if gross is None else sum(cash,F(0))+pending+gross))
    complete=all(g['state']=='entered' for g in groups) and all(l['state']=='closed' for l in lots) and all(d['nav'] is not None for d in daily)
    return dict(groups=groups,orders=orders,lots=lots,receipts=receipts,daily=daily,budgets=budgets,actions=log,complete=complete,funding_feasible=not any(g['state']=='unfilled_cash' for g in groups),initial=exact(capital,True))


def paired(calendar, groups, opens, marks, capital, fee, events, veto):
    baseline=simulate(calendar,groups,opens,marks,capital,fee,events)
    candidate=simulate(calendar,groups,opens,marks,capital,fee,events,baseline['budgets'],veto)
    b={o['id']:o for o in baseline['orders']};c={o['id']:o for o in candidate['orders']}
    retained=[key for key,o in b.items() if (o['group'],o['security']) not in veto]
    matched=all(key in c and b[key]['notional']==c[key]['notional'] and b[key]['state']==c[key]['state'] for key in retained)
    return dict(baseline=baseline,candidate=candidate,matched_retained_schedule=matched,isolated_overlay_comparable=matched and baseline['complete'] and candidate['complete'])
