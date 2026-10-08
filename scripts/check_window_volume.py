"""Independent rational volume and causal-window checks; synthetic only."""
from pathlib import Path
from copy import deepcopy
from decimal import localcontext
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.window_volume import window_volume
auth={k:'qualified' for k in ['source','calendar','sessions','actions','window','historical_availability']}
c=dict(source_id='toy-c',session='C',security_id='toy',basis='action_normalized_shares',complete=True,
       clock_kind='observed',start=100,end=130,available=131,offset=0,duration=30,volume='600')
a=dict(c,source_id='toy-a',session='A',start=0,end=30,available=31,volume='100')
b=dict(c,source_id='toy-b',session='B',start=40,end=70,available=71,volume='200')
refs=[a,b];original=deepcopy((c,refs));checks=0
def run(current=c,references=refs,decision=132,authority=auth,sessions=['A','B']):
    return window_volume(current,references,sessions,decision,authority)
def check(condition):
    global checks
    assert condition
    checks+=1
check(run()['mean_reference_volume']=='150' and run()['ratio']=='4')
check(run(current=dict(c,volume='0'))['ratio']=='0')
check(run(current=dict(c,volume='75'))['ratio']=='0.5')
check(run(references=[b,a])==run());check(run(decision=131)==run())
check(run()['empirical_admission'] is False);check((c,refs)==original)
with localcontext() as context:
    context.prec=3;check(run()['ratio']=='4');check(context.prec==3)
for key,value in [('volume',True),('volume','NaN'),('volume','Infinity'),('volume',-1),('start',101),
                  ('duration',390),('offset',1),('complete',False),('basis','raw_shares'),
                  ('available',133),('available',129),('clock_kind','retrieval_date'),('end',True)]:
    check(run(current=dict(c,**{key:value}))['status']=='blocked')
check(run(decision=130)['status']=='blocked')
check(run(references=[a])['status']=='blocked')
check(run(references=[a,a])['status']=='blocked')
check(run(references=[dict(a,volume='0'),dict(b,volume='0')])['status']=='blocked')
check(run(references=[a,dict(b,security_id='other')])['status']=='blocked')
check(run(references=[a,dict(b,source_id=a['source_id'])])['status']=='blocked')
check(run(references=[a,dict(b,start=110,end=140,available=141)],decision=142)['status']=='blocked')
check(run(references=[a,dict(b,start=20,end=50,available=51)])['status']=='blocked')
check(run(sessions=['A','D'])['status']=='blocked')
for key in c:
    bad=dict(c);del bad[key];check(run(current=bad)['status']=='blocked')
for key in auth:check(run(authority=dict(auth,**{key:'unknown'}))['status']=='blocked')
for decision in [True,132.0,'132',None]:check(run(decision=decision)['status']=='blocked')
check(run(current=None)['status']=='blocked');check(run(references=[a,None])['status']=='blocked')
print(f'{checks} independent volume denominator/window checks passed; empirical admission false')
