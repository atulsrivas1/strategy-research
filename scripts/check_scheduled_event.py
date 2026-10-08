"""Independent toy schedule state/time oracles; no historical market inputs."""
from pathlib import Path
from copy import deepcopy
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.scheduled_event import scheduled_event
auth={k:'qualified' for k in ['source','complete_ledger','historical_availability']}
a=dict(event_id='toy',version_id='A',source_id='toy-A',kind='scheduled_FOMC',status='active',
       clock_kind='observed',published_at=1,available_at=2,event_at=100)
b=dict(a,version_id='B',source_id='toy-B',published_at=12,available_at=13,event_at=200)
c=dict(b,version_id='C',source_id='toy-C',published_at=14,available_at=15,status='cancelled')
rows=[a,b,c];original=deepcopy(rows);checks=0
def run(r=rows,d=10,authority=auth):return scheduled_event(r,'toy',d,authority)
def check(condition):
    global checks
    assert condition
    checks+=1
check(run()['version_id']=='A' and run()['seconds_to_event']==90)
check(run(d=13)['version_id']=='B' and run(d=13)['seconds_to_event']==187)
check(run(d=14)['status']=='scheduled_future')
check(run(d=15)['status']=='cancelled' and 'seconds_to_event' not in run(d=15))
check(run(d=1)['status']=='unknown');check(run(r=[])['status']=='unknown')
check(run(r=[a],d=100)['status']=='at_or_after_event')
check(run(r=[a],d=101)['status']=='at_or_after_event')
check(run(r=[a],d=2)['seconds_to_event']==98)
check(run(r=list(reversed(rows)))==run());check(run(r=[a])==run())
check(rows==original and run()['empirical_admission'] is False)
check(run(r=[a,dict(b,available_at=2,published_at=1)])['status']=='blocked')
check(run(r=[a,a])['status']=='blocked')
check(run(r=[a,dict(b,source_id=a['source_id'])])['status']=='blocked')
for key,value in [('event_id','other'),('version_id',''),('source_id',''),('kind','unscheduled_FOMC'),
                  ('status','unknown'),('clock_kind','retrieval_date'),('published_at',3),
                  ('published_at',True),('available_at',2.0),('event_at',True),('event_at','100')]:
    check(run(r=[dict(a,**{key:value})])['status']=='blocked')
for key in a:
    bad=dict(a);del bad[key];check(run(r=[bad])['status']=='blocked')
for value in [True,10.0,'10',None]:check(run(d=value)['status']=='blocked')
for key in auth:check(run(authority=dict(auth,**{key:'unknown'}))['status']=='blocked')
check(run(authority={})['status']=='blocked');check(run(r=[None])['status']=='blocked')
check(run(r=None)['status']=='blocked')
print(f'{checks} independent schedule version/time checks passed; empirical admission false')
