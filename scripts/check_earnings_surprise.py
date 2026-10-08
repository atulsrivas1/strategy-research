"""Independent hand-derived EPS and availability oracles; synthetic only."""
from pathlib import Path
from copy import deepcopy
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fixtures.earnings_surprise import earnings_difference

authority = {k: 'qualified' for k in ['ledger_completeness', 'historical_availability',
                                     'source', 'actual_first_print', 'release_clock', 'basis']}
basis = dict(security_id='toy', period_end=4, metric='eps', currency='USD',
             share_basis='diluted', accounting_basis='GAAP', units='currency_per_share')
actual = dict(basis, value='1.25', published_at=10, release_at=10, available_at=11,
              first_print=True, event_id='toy-q', version_id='first', source_id='toy-release',
              clock_kind='observed')
prior = dict(basis, value='1', published_at=5, available_at=6,
             version_id='pre', source_id='toy-consensus', clock_kind='observed')
later = dict(prior, value='2', published_at=11, available_at=12, version_id='later')
checks = 0
def run(a=actual, rows=None, decision=11, auth=authority):
    return earnings_difference(a, [prior, later] if rows is None else rows, decision, auth)
def check(condition):
    global checks
    assert condition
    checks += 1

r=run()
check(r['difference']=='0.25' and r['direction']=='positive' and r['consensus_version']=='pre')
check(run(rows=[later, prior])==r)
check(run(decision=20)==r)  # post-release consensus cannot enter a later decision either
check(run(rows=[dict(prior, published_at=10, available_at=10)])['status']=='unknown')
check(run(rows=[])['status']=='unknown')
check(run(decision=10)['status']=='blocked')
check(run(dict(actual, first_print=False))['status']=='blocked')
check(run(dict(actual, first_print='true'))['status']=='blocked')
check(run(rows=[prior, prior])['status']=='blocked')
check(run(rows=[prior,dict(prior,version_id='competing')])['status']=='blocked')
check(run(rows=[prior,dict(prior,published_at=7,available_at=8,version_id='latest',value='1.1')])['difference']=='0.15')
check(run(rows=[dict(prior,value='0')])['difference']=='1.25')
check(run(dict(actual,value='-0.5'),[dict(prior,value='-1')])['difference']=='0.5')
check(run(dict(actual,value='1'))['direction']=='zero')
check(run(dict(actual,value='0.75'))['difference']=='-0.25')
check(r['empirical_admission'] is False and 'not percentage' in r['measure'])
for key,value in [('security_id','other'),('period_end',3),('metric','revenue'),
                  ('currency','EUR'),('share_basis','basic'),('accounting_basis','adjusted'),
                  ('units','currency'),('available_at',True),('published_at',7),
                  ('clock_kind','unknown'),('value','NaN')]:
    check(run(rows=[dict(prior, **{key:value})])['status']=='blocked')
for key,value in [('available_at',12),('available_at',True),('release_at',True),
                  ('published_at',9),('period_end',10),('source_id',''),('event_id',''),
                  ('version_id',''),('clock_kind','unknown'),('value',True),('value','Infinity')]:
    check(run(dict(actual, **{key:value}))['status']=='blocked')
for key in actual:
    bad=deepcopy(actual);del bad[key]
    check(run(bad)['status']=='blocked')
for key in authority:
    check(run(auth=dict(authority, **{key:'unknown'}))['status']=='blocked')
check(run(auth={})['status']=='blocked')
check(run(rows=[None])['status']=='blocked')
check(run(None)['status']=='blocked')
check(run(decision=True)['status']=='blocked')
print(f'{checks} hand-derived earnings-surprise checks passed; empirical admission false')
