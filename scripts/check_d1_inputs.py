"""Hand-derived boundary expectations; no market files, labels or outcomes."""
import copy, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fixtures.d1_inputs import qualify_window

sessions = [f'2025-01-{i:02}' for i in range(1, 21)]  # synthetic calendar, not exchange dates
base = dict(bars=[dict(session=d, high=i, available_at=9) for i,d in enumerate(sessions,1)],
            expected_sessions=sessions, signal_session='2025-01-21', close='21',
            close_available_at=10, decision_at=10,
            authorities={k:'qualified' for k in ['calendar','universe','adjustment','historical_availability','source_parity']})
checks = 0
def expect(changes, **expected):
    global checks
    args=copy.deepcopy(base); args.update(changes)
    result=qualify_window(**args)
    assert all(result.get(k)==v for k,v in expected.items()), (changes,result,expected)
    checks += 1

# Hand expectation: max(1,...,20)=20; equality is not a strict breakout.
expect({}, status='qualified ingredient', prior20_high='20', breakout=True, empirical_admission=False)
expect({'close':'20'}, breakout=False)
expect({'close':'19.999999999'}, breakout=False)
expect({'close':'20.000000001'}, breakout=True)
expect({'bars':base['bars']+[dict(session='2025-01-21',high=999,available_at=10),dict(session='2025-01-22',high=9999,available_at=11)]}, prior20_high='20', breakout=True)
expect({'bars':list(reversed(base['bars']))}, prior20_high='20')
expect({'bars':base['bars'][:-1]}, status='blocked', reason='coverage')
expect({'bars':base['bars'][:-1]+[base['bars'][0]]}, status='blocked', reason='coverage')
for value in [None, 11]:
    expect({'close_available_at':value}, status='blocked', reason='close clock')
    changed=copy.deepcopy(base['bars']); changed[0]['available_at']=value
    expect({'bars':changed}, status='blocked', reason='bar clock')
for value in [None, 'NaN', 'Infinity', 0, -1]:
    changed=copy.deepcopy(base['bars']); changed[0]['high']=value
    expect({'bars':changed}, status='blocked')
    expect({'close':value}, status='blocked')
expect({'expected_sessions':sessions[:-1]}, status='blocked', reason='calendar')
expect({'expected_sessions':sessions[:-1]+['2025-01-21']}, status='blocked', reason='calendar')
for field in base['authorities']:
    for state in ['unknown','modeled','reconstructed','unavailable']:
        changed=base['authorities'].copy(); changed[field]=state
        expect({'authorities':changed}, status='blocked', reason='authority')
expect({'authorities':{}}, status='blocked', reason='authority')
print(json.dumps(dict(checks=checks, result='PASS', scope='synthetic ingredient checks; no empirical admission or package parity')))
