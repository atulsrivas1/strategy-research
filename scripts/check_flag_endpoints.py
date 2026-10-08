"""Independent exact endpoint arithmetic and decision guards; no pattern selection."""
from pathlib import Path
from copy import deepcopy
from decimal import localcontext
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.flag_endpoints import flag_endpoints
auth={k:'qualified' for k in ['source','calendar','sessions','actions','historical_availability']}
a=dict(session='A',source_id='toy-A',security_id='toy',basis='action_normalized_close',complete=True,
       clock_kind='observed',close_at=1,available_at=2,close='100')
b=dict(a,session='B',source_id='toy-B',close_at=3,available_at=4,close='200')
c=dict(a,session='C',source_id='toy-C',close_at=5,available_at=6,close='180')
rows=[a,b,c];original=deepcopy(rows);checks=0
def run(r=rows,sessions=['A','B','C'],decision=7,authority=auth):
    return flag_endpoints(r,sessions,decision,authority)
def check(condition):
    global checks
    assert condition
    checks+=1
check(run()['advance']=='1' and run()['endpoint_retreat']=='0.1')
check(run(r=[a,b,dict(c,close='220')])['endpoint_retreat']=='-0.1')
check(run(r=[a,dict(b,close='100'),dict(c,close='100')])['advance']=='0')
check(run(r=[a,dict(b,close='50'),dict(c,close='45')])['advance']=='-0.5')
check(run(decision=6)==run());check(rows==original)
check(not run()['range_depth_authority'] and not run()['empirical_admission'])
with localcontext() as context:
    context.prec=3;check(run()['endpoint_retreat']=='0.1');check(context.prec==3)
for key,value in [('close',True),('close','NaN'),('close','Infinity'),('close',0),('close',-1),
                  ('close_at',3),('close_at',True),('available_at',4),('available_at',8),
                  ('complete',False),('basis','raw_close'),('clock_kind','retrieval_date'),
                  ('security_id','other'),('source_id',b['source_id'])]:
    check(run(r=[a,b,dict(c,**{key:value})])['status']=='blocked')
for key in c:
    bad=dict(c);del bad[key];check(run(r=[a,b,bad])['status']=='blocked')
for key in auth:check(run(authority=dict(auth,**{key:'unknown'}))['status']=='blocked')
check(run(decision=5)['status']=='blocked');check(run(r=[a,b])['status']=='blocked')
check(run(r=[c,b,a])['status']=='blocked');check(run(sessions=['A','B','B'])['status']=='blocked')
for decision in [True,7.0,'7',None]:check(run(decision=decision)['status']=='blocked')
check(run(r=None)['status']=='blocked');check(run(r=[a,b,None])['status']=='blocked')
print(f'{checks} independent fixed-endpoint checks passed; range/empirical authority false')
