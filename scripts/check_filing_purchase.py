"""Independent trade/publication/amendment state checks; no historical filings."""
from pathlib import Path
from copy import deepcopy
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.filing_purchase import filing_purchase
identity={k:'toy-'+k for k in ['event_id','issuer_id','insider_id','transaction_id']}
auth={k:'qualified' for k in ['source','complete_ledger','identity','historical_availability','transaction_mapping']}
a=dict(identity,version_id='A',source_id='toy-A',clock_kind='observed',trade_at=1,published_at=5,
       available_at=6,market='open_market',market_provenance='qualified',security='common_stock',
       table='I',code='P',acquired_disposed='A')
b=dict(a,version_id='B',source_id='toy-B',published_at=8,available_at=9,market='private')
rows=[a,b];original=deepcopy(rows);checks=0
def run(r=rows,d=6,i=identity,authority=auth):return filing_purchase(r,i,d,authority)
def check(condition):
    global checks
    assert condition
    checks+=1
check(run(d=4)['status']=='unknown');check(run(d=5)['status']=='unknown')
check(run()['status']=='purchase ingredient' and run()['version_id']=='A')
check(run(d=8)==run());check(run(d=9)['status']=='ineligible')
check(run(r=list(reversed(rows)))==run());check(run(r=[a])==run())
check(run(r=[])['status']=='unknown');check(rows==original)
check(run()['empirical_admission'] is False and run()['routine_classification']=='not implemented')
for key,value in [('table','II'),('security','other'),('code','A'),('code','M'),('code','S'),
                  ('acquired_disposed','D'),('market','private')]:
    check(run(r=[dict(a,**{key:value})])['status']=='ineligible')
for key,value in [('market','unknown'),('market_provenance','unknown'),('clock_kind','retrieval_date'),
                  ('trade_at',7),('published_at',7),('available_at',True),('trade_at',1.0),('source_id','')]:
    check(run(r=[dict(a,**{key:value})])['status']=='blocked')
for key in identity:check(run(r=[dict(a,**{key:'other'})])['status']=='blocked')
for key in a:
    bad=dict(a);del bad[key];check(run(r=[bad])['status']=='blocked')
for key in auth:check(run(authority=dict(auth,**{key:'unknown'}))['status']=='blocked')
check(run(r=[a,a])['status']=='blocked')
check(run(r=[a,dict(b,available_at=6,published_at=5)])['status']=='blocked')
check(run(r=[a,dict(b,source_id=a['source_id'])])['status']=='blocked')
for d in [True,6.0,'6',None]:check(run(d=d)['status']=='blocked')
check(run(i={})['status']=='blocked');check(run(r=None)['status']=='blocked')
check(run(r=[None])['status']=='blocked')
print(f'{checks} independent filing chronology/eligibility checks passed; empirical admission false')
