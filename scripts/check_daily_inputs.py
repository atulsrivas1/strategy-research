"""Independent hand-derived unit/action/clock oracles, no market data."""
from pathlib import Path
from copy import deepcopy
from decimal import Decimal
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.daily_inputs import normalize_bar,split_feature_view,availability_admission,price,UNDEF_PRICE,bounded_prior_sessions

checks=0
def check(value):
    global checks
    assert value
    checks+=1
row=dict(symbol='TOY',instrument_id=1,ts_utc='2025-08-29T00:00:00Z',open='100',high='110',low='90',close='105',volume=10)
# Explicit independently transcribed date oracle, not derived from price records.
expected=['2025-08-13','2025-08-14','2025-08-15','2025-08-18','2025-08-19','2025-08-20','2025-08-21','2025-08-22','2025-08-25','2025-08-26','2025-08-27','2025-08-28','2025-08-29','2025-09-02','2025-09-03','2025-09-04','2025-09-05','2025-09-08','2025-09-09','2025-09-10']
check(bounded_prior_sessions('2025-09-11')==expected)
for invalid in ['2025-09-01','2025-09-06','2025-09-12','2025-08-13','invalid',None]:
    check(bounded_prior_sessions(invalid) is None)
check(bounded_prior_sessions('2025-09-11',0) is None)
bar=normalize_bar(row,'decimal_dollars','utc_day')
check(price('123.456789','decimal_dollars')==Decimal('123.456789'))
check(price(123456789000,'integer_nanos')==Decimal('123.456789'))
check(bar['interval_end'].isoformat()=='2025-08-30T00:00:00+00:00')
check(bar['available_at'] is None and not bar['regular_session_authority'])
snapshot=deepcopy(row)
coverage=dict(authority='qualified',source_id='toy-complete',start='2025-08-01',end='2025-09-02')
event=dict(id='split-v1',symbol='TOY',type='split',effective_session='2025-09-02',available_at='2025-09-01T12:00:00Z',clock_kind='observed',source_id='toy-event',price_factor='0.5')
def view(events, cov=coverage):
    return split_feature_view(bar,events,'2025-09-02T20:00:00Z','2025-09-02',cov)
v=view([event])
check(v['prices']=={'open':Decimal('50'),'high':Decimal('55'),'low':Decimal('45'),'close':Decimal('52.5')})
check(v['volume']==20 and v['factor']==Decimal('0.5'))
check(row==snapshot and bar['prices']['open']==100 and v['original']==snapshot)
check(not v['execution_prices_changed'] and not v['empirical_admission'])
reverse={**event,'id':'reverse-v1','price_factor':'2'}
check(view([reverse])['prices']['open']==200 and view([reverse])['volume']==5)
future={**event,'id':'future-v1','effective_session':'2025-09-03','price_factor':'0.1'}
check(view([event,future])['prices']==v['prices'])
second={**event,'id':'second-event','price_factor':'0.25'}
check(view([event,second])['prices']['open']==Decimal('12.5') and view([event,second])['volume']==80)
old={**event,'effective_session':'2025-08-29'}
check(view([old])['factor']==1)
dividend={**event,'type':'cash_dividend'}
check(view([dividend])['factor']==1)
check(view([event,event])['status']=='blocked')
for changes in [{'clock_kind':'modeled'},{'clock_kind':'reconstructed'},{'available_at':None},{'available_at':'2025-09-03T00:00:00Z'},{'symbol':'OTHER'},{'price_factor':0},{'source_id':None},{'type':'spinoff'}]:
    check(view([{**event,**changes}])['status']=='blocked')
for changes in [{'authority':'unknown'},{'source_id':None},{'start':'2025-08-30'},{'end':'2025-09-01'}]:
    check(view([],{**coverage,**changes})['status']=='blocked')
for changes in [{'close':None},{'high':'NaN'},{'low':0},{'high':99},{'volume':-1},{'volume':1.5},{'volume':True},{'instrument_id':None},{'ts_utc':'2025-08-29T00:00:00'},{'ts_utc':'2025-08-29T01:00:00Z'}]:
    check(normalize_bar({**row,**changes},'decimal_dollars','utc_day')['status']=='blocked')
check(normalize_bar(row,'unknown','utc_day')['status']=='blocked')
check(normalize_bar(row,'decimal_dollars','core_session')['status']=='blocked')
nanos={**row,**{k:int(Decimal(row[k])*1_000_000_000) for k in ['open','high','low','close']}}
check(normalize_bar(nanos,'integer_nanos','utc_day')['prices']==bar['prices'])
for bad in [UNDEF_PRICE,True,100.0,None]:
    check(normalize_bar({**nanos,'open':bad},'integer_nanos','utc_day')['status']=='blocked')
args=['2025-08-29T16:00:00-04:00','2025-08-29T20:01:00Z','observed','2025-08-29T20:02:00Z','qualified_core_session']
check(availability_admission(*args))
for index,bad in [(0,'2025-08-30T00:00:00Z'),(1,'2025-08-29T19:59:00Z'),(1,None),(1,'2025-08-29T20:03:00Z'),(2,'modeled'),(2,'reconstructed'),(3,'2025-08-29T20:02:00'),(4,'utc_day')]:
    changed=args.copy();changed[index]=bad;check(not availability_admission(*changed))
print(json.dumps(dict(checks=checks,result='PASS',scope='synthetic daily normalization/actions/clocks; no feed or empirical admission')))
