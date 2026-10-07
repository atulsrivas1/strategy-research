"""Artificial scanner/sleeve witness only; no market or broker loader."""
from fractions import Fraction as F
from decimal import Decimal as D
import m2_foundation as core

def field(value,session,late=False):
    stamp=1000+100*session+20
    return core.Field(D(str(value)),str(session),stamp,stamp+(11 if late else 1),stamp,True)

def decision(t,scanner,late=False):
    # Artificial feature matrix with consistent day0/day1 closes and prior lows.
    values={'A':(12,13,13,11,10,11) if t==0 else (10,12,13,9,8,9),
            'B':(20,21,21,19,18,21) if t==0 else (18,20,21,17,16,19)}
    clock=1000+100*t+30;eligible=[];states=[];returns=[]
    for symbol,(close,prior,close2,s50,s100,low) in values.items():
        current=field(close,t);previous=field(prior,t-1)
        assert core.available(current,str(t),clock,1000) is None
        assert core.available(previous,str(t-1),clock,1000) is None
        # Shared original fixture eligibility; no outcome/mark/exit input here.
        if scanner=='pullback' and not core.pullback(D(close),D(close2),D(s50),D(s100),D(60_000_000)):continue
        eligible.append(symbol);returns.append(F(close,prior)-1)
        stock=core.classify_stock(current,field(low,t-1),str(t),str(t-1),clock,1000)
        market=core.classify_market(field(200,t,late),field(190,t-1),field(180,t-1),str(t),str(t-1),clock,1000)
        states.append({'stock':stock,'market':market,'keep':core.gate(stock,market)})
    weights=tuple(F(1,len(eligible)) for _ in eligible) if scanner=='pullback' else core.rank_weights(returns)
    return {'signal':t,'scanner':scanner,'symbols':eligible,'weights':weights,'keep':[s['keep'] for s in states],'states':states}

def simulate(decisions,opens,closes,overlay=False,cost=F(1,2000),horizon=5):
    cash=F(10);lots=[];rows=[];sleeves=[]
    n=len(closes)
    for d in decisions:
        entry=d['signal']+1;exit=entry+horizon-1
        retained=[w if not overlay or k else F(0) for w,k in zip(d['weights'],d['keep'])]
        sleeves.append({'signal':d['signal'],'entry':entry,'exit':exit,'original_weights':d['weights'],'retained':retained,'context_cash':1-sum(retained),'state':'planned'})
    for day in range(n):
        # Same-day events are independently retained; timing fixed by calendar indices.
        for d,s in zip(decisions,sleeves):
            if day!=s['entry']:continue
            prices=[opens.get((day,sym)) for sym,w in zip(d['symbols'],s['retained']) if w]
            if any(x is None or x<=0 for x in prices):s['state']='unfilled';continue
            s['state']='entered';s['entry_cost']=sum(s['retained'])*cost
            for sym,w in zip(d['symbols'],s['retained']):
                if not w:continue
                o=opens[(day,sym)];cash-=w*(1+cost)
                lots.append({'signal':s['signal'],'symbol':sym,'weight':w,'quantity':w/o,'exit':s['exit'],'open':o,'closed':False,'exit_missing':False})
        for lot in lots:
            if lot['closed'] or day!=lot['exit']:continue
            x=closes[day].get(lot['symbol'])
            if x is None:lot['exit_missing']=True;continue
            cash+=lot['quantity']*x*(1-cost);lot['closed']=True
        active=[l for l in lots if not l['closed']]
        marks=[closes[day].get(l['symbol']) for l in active]
        equity=None if any(m is None for m in marks) else cash+sum(l['quantity']*m for l,m in zip(active,marks))
        rows.append({'day':day,'cash':cash,'equity':equity,'active_lots':len(active),'active_sleeves':len({l['signal'] for l in active})})
    for s in sleeves:
        if s['state']=='unfilled':continue
        affected=[l for l in lots if l['signal']==s['signal']]
        if s['entry']>=n:s['state']='not_entered_calendar_end'
        elif s['exit']>=n or any(not l['closed'] for l in affected):s['state']='censored'
        else:s['state']='evaluable'
    return {'daily':rows,'sleeves':sleeves,'lots':lots}

def fixture():
    opens={(d,s):F(p) for d in [1,2] for s,p in [('A',10),('B',20)]}
    close=[{'A':F(a),'B':F(b)} for a,b in [(12,20),(10,18),(12,19),(10,18),(11,19),(11,18),(11,18)]]
    return opens,close
