"""Frozen exploratory D2 proxy, with complete-cohort ranking and no source certification."""
from decimal import Decimal
import math
import d1_exploratory as common


def choose(bars, calendar, day, symbols):
    i=calendar.index(day)
    if i<20 or len(symbols)!=len(set(symbols)) or len(symbols)<4:
        return dict(status='unresolved',reason='cohort/calendar',selected=[])
    scores={}
    for s in symbols:
        a,b=bars.get((s,calendar[i-20])),bars.get((s,day))
        if a is None or b is None:return dict(status='unresolved',reason='incomplete cohort',selected=[])
        x,y=Decimal(str(a['close'])),Decimal(str(b['close']))
        if not x.is_finite() or not y.is_finite() or min(x,y)<=0:
            return dict(status='unresolved',reason='invalid endpoint',selected=[])
        scores[s]=y/x-1
    ranked=sorted(scores,key=lambda s:(-scores[s],s))
    if scores[ranked[2]]==scores[ranked[3]]:
        return dict(status='unresolved',reason='boundary tie',selected=[])
    return dict(status='complete exploratory ranking',selected=ranked[:3],
                ranks={s:1+sum(v>scores[s] for v in scores.values()) for s in symbols},
                scores={s:str(v) for s,v in scores.items()})


def context(bars, calendar, day, symbol):
    i=calendar.index(day);a=bars.get((symbol,calendar[i-5]));b=bars.get((symbol,day))
    if a is None or b is None:return 'unknown'
    x,y=Decimal(str(a['close'])),Decimal(str(b['close']))
    if not x.is_finite() or not y.is_finite() or min(x,y)<=0:return 'unknown'
    return 'aligned' if y>x else 'conflicting' if y<x else 'neutral'


def event(bars, calendar, day, symbol, weight, stock='unknown'):
    i=calendar.index(day)
    e=dict(day=day,symbol=symbol,weight=weight,stock=stock,market='unknown',
           joint='conflicting' if stock=='conflicting' else 'unknown',veto=stock=='conflicting',
           entry_day=calendar[i+2],exit_day=calendar[i+7])
    a,b=bars.get((symbol,e['entry_day'])),bars.get((symbol,e['exit_day']))
    e['outcome']='unfilled' if a is None else 'censored' if b is None else 'filled'
    if e['outcome']=='filled':
        e.update(entry=a['open'],exit=b['open'])
        if not all(math.isfinite(e[k]) and e[k]>0 for k in ['entry','exit']):e['outcome']='invalid outcome'
    return e


def evaluate(bars,calendar,decisions,symbols):
    screens=[];events=[];benchmark=[]
    for day in decisions:
        ranking=choose(bars,calendar,day,symbols);screens.append(dict(day=day,**ranking))
        if ranking['status']!='complete exploratory ranking':continue
        events.extend(event(bars,calendar,day,s,1/15,context(bars,calendar,day,s)) for s in ranking['selected'])
        benchmark.extend(event(bars,calendar,day,s,.2/len(symbols)) for s in symbols)
    costs=[common.summarize(events,decisions,f) for f in [.001,.002,.003]]
    benchmark_summary=common.summarize(benchmark,decisions,.001)
    primary=costs[0];interval=common.bootstrap(primary['daily_delta'])
    secondary_daily={d:sum(e['weight']*common.net_return(e['entry'],e['exit'],.001) for e in events if e['day']==d and e['outcome']=='filled')-
                       sum(e['weight']*common.net_return(e['entry'],e['exit'],.001) for e in benchmark if e['day']==d and e['outcome']=='filled') for d in decisions}
    secondary=dict(paired_delta=primary['baseline_contribution']-benchmark_summary['baseline_contribution'],interval=common.bootstrap(secondary_daily))
    admitted=[e for e in events if not e['veto']]
    differential=sum(e['weight']*common.net_return(e['entry'],e['exit'],.002) for e in admitted if e['outcome']=='filled')-primary['baseline_contribution']
    blocked=sum(s['status']!='complete exploratory ranking' for s in screens)
    unresolved=sum(e['outcome']!='filled' for e in events+benchmark)
    support=len({e['day'] for e in events if e['outcome']=='filled'})
    if blocked or unresolved or not primary['filled']:verdict='inconclusive'
    elif primary['paired_delta']<=0 and interval[1]<0:verdict='rejected tested overlay'
    elif (primary['paired_delta']>0 and primary['filled']>=20 and primary['vetoed_filled']>=5 and support>=10
          and interval[0]>0 and all(c['paired_delta']>0 for c in costs) and differential>0):verdict='promising exploratory under assumptions'
    else:verdict='inconclusive'
    return dict(screen_rows=screens,events=events,benchmark_events=benchmark,costs=costs,benchmark_summary=benchmark_summary,
                secondary=secondary,paired_interval=interval,differential_stress_delta=differential,verdict=verdict,
                point_criterion='failed' if primary['paired_delta']<=0 else 'positive',blocked_decisions=blocked,
                expected_scanner_slots=len(decisions)*3,expected_benchmark_slots=len(decisions)*len(symbols),
                unresolved=unresolved,distinct_signal_days=support,
                states={k:{s:sum(e[k]==s for e in events) for s in common.STATES} for k in ['stock','market','joint']},
                subwindows=[common.summarize([e for e in events if e['day']<'2025-08-27'],decisions,.001),common.summarize([e for e in events if e['day']>='2025-08-27'],decisions,.001)],
                baseline_proxy=common.proxy_path(events,bars,calendar,.001),candidate_proxy=common.proxy_path(events,bars,calendar,.001,True),
                benchmark_proxy=common.proxy_path(benchmark,bars,calendar,.001),final_access=False,source_qualification='unverified',clock_basis='modeled',funded_accounting=False)
