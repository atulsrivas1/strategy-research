"""Independent complete-cohort/rank/tie arithmetic oracles, synthetic only."""
from pathlib import Path
from copy import deepcopy
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.relative_strength import rank_cohort,select_top_k
base=dict(start_at=1,end_at=9,available_at=9,clock_kind='observed',source_id='toy',price_basis='qualified_split_basis',start_price='100')
rows=[{**base,'security_id':sid,'end_price':end} for sid,end in [('A','120'),('B','110'),('C','90')]]
authority={k:'qualified' for k in ['universe','prices','actions','calendar','historical_availability']}
checks=0
def check(v):
    global checks
    assert v;checks+=1
def run(data=rows,ids=['A','B','C'],auth=authority):
    return rank_cohort(data,ids,1,9,10,auth)
r=run()
check(r['ranked']==[dict(security_id='A',score='0.2',rank=1),dict(security_id='B',score='0.1',rank=2),dict(security_id='C',score='-0.1',rank=3)])
check(run(list(reversed(rows)))==r)
check(select_top_k(r,1)['security_ids']==['A'] and not r['empirical_admission'])
missing=run(rows[:-1]);check(missing['status']=='blocked' and missing['missing']==['C'] and missing['expected']==3)
check(run(rows+[rows[0]])['status']=='blocked')
check(run(rows+[None])['status']=='blocked')
check(run(rows+[{**rows[0],'security_id':'FUTURE','end_at':11}])['status']=='blocked')
check(run(ids=['A','B','B'])['status']=='blocked')
for changes in [{'available_at':11},{'available_at':None},{'clock_kind':'modeled'},{'clock_kind':'reconstructed'},{'end_at':10},{'start_at':0},{'start_at':True},{'end_price':None},{'end_price':'NaN'},{'start_price':0},{'end_price':True},{'price_basis':'unknown'},{'source_id':None}]:
    changed=deepcopy(rows);changed[0].update(changes);check(run(changed)['status']=='blocked')
ties=deepcopy(rows);ties[1]['end_price']='120'
t=run(ties);check([x['rank'] for x in t['ranked']]==[1,1,3])
check(select_top_k(t,1)['status']=='blocked')
check(select_top_k(t,2)['security_ids']==['A','B'])
for field in authority:
    changed=authority.copy();changed[field]='unknown';check(run(auth=changed)['status']=='blocked')
for k in [0,4,True]:check(select_top_k(r,k)['status']=='blocked')
check(rank_cohort(rows,['A','B','C'],1,10,10,authority)['status']=='blocked')
print(json.dumps(dict(checks=checks,result='PASS',scope='synthetic complete-cohort/ranking/tie contract; no empirical results')))
