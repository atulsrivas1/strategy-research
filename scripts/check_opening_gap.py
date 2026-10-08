"""Hand-derived split units and session/decision boundary checks; synthetic only."""
from pathlib import Path
from copy import deepcopy
from decimal import localcontext
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.opening_gap import opening_gap

authority={k:'qualified' for k in ['source','calendar','endpoints','actions','historical_availability']}
calendar=dict(sessions=['2025-10-31','2025-11-03'],close_at='2025-10-31T20:00:00Z',open_at='2025-11-03T14:30:00Z',
              endpoint_sources={'official_close':'toy-close','official_open':'toy-open'})
previous=dict(session='2025-10-31',role='official_close',security_id='toy',currency='USD',source_id='toy-close',
              price_basis='raw_unadjusted',clock_kind='observed',event_at=calendar['close_at'],
              available_at='2025-10-31T20:00:01Z',price='100')
current=dict(previous,session='2025-11-03',role='official_open',source_id='toy-open',event_at=calendar['open_at'],
             available_at='2025-11-03T14:30:01Z',price='102')
ledger=dict(security_id='toy',complete=True,from_at=calendar['close_at'],to_at=calendar['open_at'],rows=[])
split=dict(kind='split',security_id='toy',action_id='a',source_id='toy-action',clock_kind='observed',
           effective_at=calendar['open_at'],available_at='2025-10-30T12:00:00Z',new_per_old='2')
checks=0
def run(p=previous,c=current,cal=calendar,a=ledger,decision='2025-11-03T14:31:00Z',auth=authority):
    return opening_gap(p,c,cal,a,decision,auth)
def check(value):
    global checks
    assert value
    checks+=1
base=deepcopy((previous,current,calendar,ledger))
r=run();check(r['gap']=='0.02' and r['previous_close_in_current_share_units']=='100')
check(run(c=dict(current,price='51'),a=dict(ledger,rows=[split]))['gap']=='0.02')
check(run(c=dict(current,price='204'),a=dict(ledger,rows=[dict(split,new_per_old='0.5')]))['gap']=='0.02')
check(run(a=dict(ledger,rows=[split,dict(split,action_id='b',new_per_old='0.5')]))['gap']=='0.02')
check(run(c=dict(current,price='98'))['gap']=='-0.02')
check(run(c=dict(current,price='100'))['gap']=='0')
check(not r['open_fill_authority'] and not r['empirical_admission'])
check(run(p=dict(previous,event_at='2025-10-31T16:00:00-04:00'),c=dict(current,event_at='2025-11-03T09:30:00-05:00'))==r)
with localcontext() as ctx:
    ctx.prec=3;check(run()==r);check(ctx.prec==3)
check((previous,current,calendar,ledger)==base)
for decision in ['2025-11-03T14:29:00Z','2025-11-03T14:30:01Z','2025-11-03T14:31:00','2025-11-03T14:31:00.000000001Z']:
    check(run(decision=decision)['status']=='blocked')
for key,value in [('role','minute_proxy'),('security_id','other'),('currency','EUR'),('source_id',''),
                  ('session','2025-11-04'),('event_at','2025-11-03T13:30:00Z'),('clock_kind','unknown'),
                  ('price_basis','split_adjusted'),('available_at','2025-11-03T14:31:00Z'),
                  ('available_at','2025-11-03T14:29:00Z'),('price',True),('price','NaN'),('price',0),('price',-1)]:
    check(run(c=dict(current,**{key:value}))['status']=='blocked')
check(run(p=dict(previous,available_at=calendar['open_at']))['status']=='blocked')
check(run(cal=dict(calendar,sessions=['2025-10-31','2025-11-04']))['status']=='blocked')
check(run(cal=dict(calendar,open_at='2025-11-03T13:30:00Z'))['status']=='blocked')
check(run(a=dict(ledger,complete=False))['status']=='blocked')
check(run(a=dict(ledger,to_at='2025-11-03T14:29:00Z'))['status']=='blocked')
check(run(a=dict(ledger,rows=[split,split]))['status']=='blocked')
for key,value in [('kind','cash_dividend'),('security_id','other'),('action_id',''),('source_id',''),
                  ('clock_kind','unknown'),('new_per_old',True),('new_per_old',0),('new_per_old','Infinity'),
                  ('effective_at',calendar['close_at']),('effective_at','2025-11-03T14:32:00Z'),
                  ('available_at','2025-11-03T14:31:00Z')]:
    check(run(a=dict(ledger,rows=[dict(split,**{key:value})]))['status']=='blocked')
for key in current:
    bad=deepcopy(current);del bad[key];check(run(c=bad)['status']=='blocked')
for key in authority:
    check(run(auth=dict(authority,**{key:'unknown'}))['status']=='blocked')
check(run(auth={})['status']=='blocked')
check(run(a=dict(ledger,rows=[None]))['status']=='blocked')
check(run(c=None)['status']=='blocked')
check(run(c=dict(current,source_id='undeclared-source'))['status']=='blocked')
print(f'{checks} hand-derived opening-gap checks passed; empirical/open-fill admission false')
