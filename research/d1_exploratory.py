"""Frozen exploratory price proxy; no loader, optimizer or source certification."""
import math
import random

STATES=('aligned','conflicting','neutral','unknown')


def screen(history, current):
    if len(history)!=20 or current is None or any(b is None for b in history):
        return dict(status='missing input',signal=None,stock='unknown')
    highs=[b['high'] for b in history];closes=[b['close'] for b in history]
    if any(not math.isfinite(x) or x<=0 for x in highs+closes+[current['close']]):
        return dict(status='invalid input',signal=None,stock='unknown')
    mean=sum(closes)/20
    sd=math.sqrt(sum((x-mean)**2 for x in closes)/20)
    boundary=mean+2*sd;difference=current['close']-boundary
    stock='neutral' if abs(difference)<=1e-10 else ('conflicting' if difference>0 else 'aligned')
    return dict(status='screened',signal=current['close']>max(highs),stock=stock,threshold=max(highs),context_boundary=boundary)


def opportunities(bars,calendar,decisions,symbols):
    rows=[];events=[]
    for day in decisions:
        i=calendar.index(day)
        for symbol in symbols:
            s=screen([bars.get((symbol,d)) for d in calendar[i-20:i]],bars.get((symbol,day)))
            row=dict(day=day,symbol=symbol,market='unknown',**s)
            rows.append(row)
            if s['signal'] is not True:continue
            e=dict(row,entry_day=calendar[i+2],exit_day=calendar[i+7],weight=0.1,
                   joint='conflicting' if s['stock']=='conflicting' else 'unknown',veto=s['stock']=='conflicting')
            entry=bars.get((symbol,e['entry_day']));exit=bars.get((symbol,e['exit_day']))
            e['outcome']='unfilled' if entry is None else ('censored' if exit is None else 'filled')
            if e['outcome']=='filled':
                e.update(entry=entry['open'],exit=exit['open'])
                if not all(math.isfinite(e[k]) and e[k]>0 for k in ['entry','exit']):e['outcome']='invalid outcome'
            events.append(e)
    return rows,events


def net_return(entry,exit,fee):
    ratio=exit/entry
    return ratio-1-fee*(1+ratio)


def proxy_path(events,bars,calendar,fee,candidate=False):
    increments=[0.0]*len(calendar);exposure=[0.0]*len(calendar);turnover=0.0
    for e in events:
        if e['outcome']!='filled' or (candidate and e['veto']):continue
        a,b=calendar.index(e['entry_day']),calendar.index(e['exit_day'])
        previous=0.0
        for i in range(a,b+1):
            bar=bars.get((e['symbol'],calendar[i]))
            if bar is None:return dict(curve=None,drawdown=None,reason='missing holding close')
            mark=e['exit'] if i==b else bar['close']
            value=e['weight']*(mark/e['entry']-1-fee)
            if i==b:value-=e['weight']*fee*mark/e['entry']
            increments[i]+=value-previous;previous=value
            if i<b:exposure[i]+=e['weight']
        turnover+=e['weight']*(1+e['exit']/e['entry'])
    curve=[];level=1.0;peak=1.0;dd=0.0
    for change in increments:
        level+=change;curve.append(level);peak=max(peak,level);dd=max(dd,(peak-level)/peak)
    return dict(curve=curve,drawdown=dd,max_reference_exposure=max(exposure),turnover=turnover)


def summarize(events,decisions,fee):
    baseline=0.0;candidate=0.0;avoided=0;sacrificed=0;avoided_value=0.0;sacrificed_value=0.0
    daily={d:0.0 for d in decisions}
    for e in events:
        if e['outcome']!='filled':continue
        n=net_return(e['entry'],e['exit'],fee);v=e['weight']*n
        baseline+=v
        if not e['veto']:candidate+=v
        else:
            daily[e['day']]-=v
            if n<0:avoided+=1;avoided_value-=v
            if n>0:sacrificed+=1;sacrificed_value+=v
    return dict(fee_per_side=fee,baseline_contribution=baseline,candidate_contribution=candidate,
                paired_delta=candidate-baseline,original_opportunities=len(events),
                filled=sum(e['outcome']=='filled' for e in events),
                vetoed_filled=sum(e['outcome']=='filled' and e['veto'] for e in events),
                avoided_losses=avoided,sacrificed_winners=sacrificed,
                avoided_loss_contribution=avoided_value,sacrificed_winner_contribution=sacrificed_value,
                mean_delta_per_original_opportunity=(candidate-baseline)/len(events) if events else None,
                daily_delta=daily)


def bootstrap(daily):
    values=list(daily.values());rng=random.Random(4001);n=len(values);samples=[]
    for _ in range(1000):
        draw=[]
        while len(draw)<n:
            start=rng.randrange(n);draw.extend(values[(start+j)%n] for j in range(5))
        samples.append(sum(draw[:n]))
    samples.sort()
    return [samples[24],samples[974]]


def evaluate(bars,calendar,decisions,symbols):
    rows,events=opportunities(bars,calendar,decisions,symbols)
    costs=[summarize(events,decisions,f) for f in [0.001,0.002,0.003]]
    primary=costs[0];interval=bootstrap(primary['daily_delta'])
    unresolved=sum(e['outcome']!='filled' for e in events)
    support_days=len({e['day'] for e in events if e['outcome']=='filled'})
    if unresolved or primary['filled']==0:verdict='inconclusive'
    elif primary['paired_delta']<=0:verdict='rejected incremental criterion'
    elif (primary['filled']>=20 and primary['vetoed_filled']>=5 and support_days>=10
          and interval[0]>0 and all(c['paired_delta']>0 for c in costs)):verdict='promising exploratory under assumptions'
    else:verdict='inconclusive'
    states={which:{state:sum(e.get(which)=='%s'%state for e in events) for state in STATES} for which in ['stock','market','joint']}
    subwindows=[summarize([e for e in events if e['day']<'2025-08-27'],decisions,0.001),
                summarize([e for e in events if e['day']>='2025-08-27'],decisions,0.001)]
    return dict(screen_rows=rows,events=events,costs=costs,paired_interval=interval,verdict=verdict,
                unresolved=unresolved,distinct_signal_days=support_days,states=states,subwindows=subwindows,
                baseline_proxy=proxy_path(events,bars,calendar,0.001),candidate_proxy=proxy_path(events,bars,calendar,0.001,True),
                final_access=False,source_qualification='unverified',clock_basis='modeled',funded_accounting=False)
