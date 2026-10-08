"""Hand-derived aggregation/boundary oracle, no source reader or strategy test."""
from pathlib import Path
from copy import deepcopy
from decimal import Decimal
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.session_proxy import aggregate_minutes

rows=[dict(ts_utc='2025-09-10T13:30:00Z',symbol='TOY',instrument_id=1,open=100,high=103,low=99,close=102,volume=10),dict(ts_utc='2025-09-10T13:31:00Z',symbol='TOY',instrument_id=1,open=102,high=105,low=101,close=104,volume=20)]
original=deepcopy(rows);checks=0
def check(v):
    global checks
    assert v;checks+=1
def run(data,start='2025-09-10T13:30:00Z',end='2025-09-10T13:32:00Z',unit='decimal_dollars',source='toy-v1'):
    return aggregate_minutes(data,start,end,'TOY',unit,source)
result=run(rows)
check([result[k] for k in ['open','high','low','close','volume']]==[100,105,99,104,30])
check(result['observed_minutes']==2 and not result['missing_minutes'])
check(not result['official_close_authority'] and not result['empirical_admission'] and result['available_at'] is None)
check(run(list(reversed(rows)))==result)
outside=[{**rows[0],'ts_utc':'2025-09-10T13:29:00Z','high':9999},{**rows[1],'ts_utc':'2025-09-10T13:32:00Z','high':99999}]
check(run(rows+outside)==result)
check(rows==original)
check(run(rows[:1])['missing_minutes']==['2025-09-10T13:31:00+00:00'])
check(run([])['status']=='blocked')
check(run(rows+[rows[0]])['status']=='blocked')
for changes in [{'symbol':'OTHER'},{'instrument_id':2},{'instrument_id':None},{'high':100},{'volume':-1},{'volume':False},{'close':'NaN'},{'ts_utc':'2025-09-10T13:30:00.000000001Z'},{'ts_utc':'2025-09-10T13:30:01Z'},{'ts_utc':'2025-09-10T13:30:00'}]:
    check(run([rows[0],{**rows[1],**changes}])['status']=='blocked')
check(run(rows,end='2025-09-10T13:31:30Z')['status']=='blocked')
check(run(rows,end='2025-09-10T13:30:00Z')['status']=='blocked')
check(run(rows,source=None)['status']=='blocked')
check(run(rows,unit='unknown')['status']=='blocked')
check(run(rows,start='2025-09-10T09:30:00-04:00',end='2025-09-10T09:32:00-04:00')==result)
precise=[{**r,**{k:str(Decimal(str(r[k]))+Decimal('0.000000001')) for k in ['open','high','low','close']}} for r in rows]
check(run(precise)['high']==Decimal('105.000000001'))
print(json.dumps(dict(checks=checks,result='PASS',scope='synthetic half-open minute aggregation; official close/arrival and empirical admission remain unqualified')))
