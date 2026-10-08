"""Hand-derived synthetic clocks/values; never reads market data."""
from pathlib import Path
import sys
from copy import deepcopy
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fixtures.fundamental_vintages import select_vintage

authority = {k: 'qualified' for k in ['ledger_completeness', 'historical_availability', 'source']}
original = dict(security_id='toy', metric='eps', period_end=4, published_at=8,
                available_at=9, version_id='original', source_id='toy-source',
                clock_kind='observed', value='1')
revised = dict(original, published_at=12, available_at=13, version_id='revised', value='2')
checks = 0
def run(rows, decision=10, auth=authority):
    return select_vintage(rows, 'toy', 4, 'eps', decision, auth)
def check(condition):
    global checks
    assert condition
    checks += 1

check(run([original, revised])['value'] == '1')
check(run([revised, original]) == run([original, revised]))
check(run([original, revised], 13)['value'] == '2')
check(run([original], 8)['status'] == 'unknown')
check(run([])['status'] == 'unknown')
check(run([original, original])['status'] == 'blocked')
check(run([original, dict(original, version_id='competing')])['status'] == 'blocked')
check(run([dict(original, value='-1')])['value'] == '-1')
check(run([dict(original, value='0')])['value'] == '0')
check(run([dict(original, value='0.125')])['value'] == '0.125')
check(run([original])['empirical_admission'] is False)
for key, value in [('security_id', 'other'), ('metric', 'sales'), ('period_end', 3),
                   ('period_end', True), ('published_at', 3), ('published_at', True),
                   ('available_at', 7), ('available_at', True), ('version_id', ''),
                   ('source_id', ''), ('source_id', 12), ('clock_kind', 'unknown'),
                   ('value', True), ('value', 'NaN'), ('value', 'Infinity')]:
    check(run([dict(original, **{key: value})])['status'] == 'blocked')
for key in original:
    bad = deepcopy(original)
    del bad[key]
    check(run([bad])['status'] == 'blocked')
check(run([None])['status'] == 'blocked')
check(run([original], True)['status'] == 'blocked')
check(run([original], 3)['status'] == 'blocked')
for key in authority:
    check(run([original], auth=dict(authority, **{key: 'unknown'}))['status'] == 'blocked')
check(run([original], auth={})['status'] == 'blocked')
print(f'{checks} hand-derived fundamental-vintage checks passed; empirical admission false')
