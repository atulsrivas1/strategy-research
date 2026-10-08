"""Independent receipt truth-table/identity checks; no market I/O."""
from pathlib import Path
from copy import deepcopy
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.source_admission import source_admission,GATES
request=dict(scope_id='toy20',source_sha256='a'*64,requirements=list(GATES))
rows=[dict(gate=g,scope_id=request['scope_id'],source_sha256=request['source_sha256'],evidence_id='toy-'+g,
           reason='toy hand qualification',status='qualified',clock_kind='qualified_historical',
           checked_at='2026-10-08T12:00:00Z') for g in GATES]
original=deepcopy((request,rows));checks=0
def run(r=request,e=rows):return source_admission(r,e)
def check(condition):
    global checks
    assert condition
    checks+=1
check(run()['status']=='receipt-consistent prerequisites')
check(not run()['empirical_admission'] and not run()['external_evidence_certified'])
check(run(e=list(reversed(rows)))==run());check((request,rows)==original)
for index,gate in enumerate(GATES):
    for status in ['blocked','unknown']:
        e=deepcopy(rows);e[index]['status']=status
        check(run(e=e)['unmet']==[dict(gate=gate,evidence_id='toy-'+gate,reason='toy hand qualification')])
    for kind in ['unknown','modeled']:
        e=deepcopy(rows);e[index]['clock_kind']=kind;check(len(run(e=e)['unmet'])==1)
check(len(run(e=[])['unmet'])==4);check(len(run(e=rows[:3])['unmet'])==1)
check(run(e=rows+[rows[0]])['status']=='blocked')
for key,value in [('gate','other'),('scope_id','other'),('source_sha256','b'*64),('evidence_id',''),
                  ('evidence_id',rows[1]['evidence_id']),('reason',''),('status',True),('clock_kind','retrieved'),
                  ('checked_at','2026-10-08T12:00:00'),('checked_at','2026-10-08T12:00:00.000000001Z')]:
    e=deepcopy(rows);e[0][key]=value;check(run(e=e)['status']=='blocked')
for key in rows[0]:
    e=deepcopy(rows);del e[0][key];check(run(e=e)['status']=='blocked')
for key,value in [('source_sha256','A'*64),('source_sha256','a'*63),('scope_id',''),
                  ('requirements',GATES[:3]),('requirements',list(reversed(GATES)))]:
    check(run(r=dict(request,**{key:value}))['status']=='blocked')
e=deepcopy(rows)
for row in e:row['checked_at']='2030-01-01T00:00:00Z'
check(run(e=e)==run())  # Later inspection does not add historical authority.
check(run(e=[None])['status']=='blocked');check(run(r=None)['status']=='blocked')
check(run(e=None)['status']=='blocked');check(run(r=dict(request,hidden_pass=True))['status']=='blocked')
check(run(e=[dict(rows[0],hidden_pass=True)]+rows[1:])['status']=='blocked')
print(f'{checks} independent source-admission receipt checks passed; empirical admission false')
