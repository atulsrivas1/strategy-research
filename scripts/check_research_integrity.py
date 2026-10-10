"""Independent hand arithmetic and deliberate failure injections; no market data."""
import importlib.util
import json
import sys
import tempfile
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'research'))
from execution_guard import execute, source_manifest, verify_sources
from lossless_inputs import normalize, history
from funded_ledger import simulate
import funded_ledger as funded_engine

checks = []
def check(name, condition):
    assert condition, name
    checks.append(name)

def fails(name, function, exception=ValueError):
    try:
        function()
    except exception:
        checks.append(name)
    else:
        raise AssertionError(name)

row = dict(instrument_id=17, symbol='SYNTH', date='2025-01-02',
           open='100.000000000000001', high='101', low='99', close='100.000000000000002',
           start='2025-01-02T00:00:00Z', available_at=None,
           source='unknown', units='assumed USD/share', actions='unverified', clock_assumption='modeled daily date')
n = normalize([row])[0]
check('decimal difference retained without float', n['open'] != n['close'] and n['open'] == row['open'])
check('identity clocks uncertainty retained', n['instrument_id'] == 17 and n['start'] == row['start'] and n['available_at'] is None and n['evidence'] == 'exploratory-unqualified')
for name, updates in [('float rejected', {'open':100.0}), ('nonfinite rejected', {'close':'NaN'}), ('zero rejected', {'low':'0'}), ('invalid bounds rejected', {'low':'102'}), ('boolean identity rejected', {'instrument_id':True}), ('naive clock rejected', {'start':'2025-01-02T00:00:00'}), ('uncertainty required', {'actions':''})]:
    fails(name, lambda updates=updates: normalize([dict(row, **updates)]))
fails('duplicate identity date rejected', lambda: normalize([row,row]))
fails('ticker identity change rejected', lambda: normalize([row,dict(row,instrument_id=18,date='2025-01-03')]))
rows = normalize([dict(row,date=f'2025-01-0{day}') for day in (2,3,4)])
check('future rows never enter history', [x['date'] for x in history(rows,17,'2025-01-03',2)] == ['2025-01-02','2025-01-03'])
fails('short history rejected', lambda: history(rows,17,'2025-01-02',2))
fails('negative history rejected', lambda: history(rows,17,'2025-01-03',-1))
timed = normalize([dict(row,available_at='2025-01-03T22:00:00Z')])
fails('timestamped history requires decision clock',lambda: history(timed,17,'2025-01-03',1))
fails('late arrival cannot enter earlier decision',lambda: history(timed,17,'2025-01-03',1,'2025-01-03T21:00:00Z'))
check('known arrival usable at decision',history(timed,17,'2025-01-03',1,'2025-01-03T22:00:00Z')[0]['instrument_id']==17)
check('volume identity not discarded',normalize([dict(row,volume=123)])[0]['volume']==123)
fails('invalid numeric text rejected',lambda: normalize([dict(row,open='bad')]))
fails('noncanonical decision date rejected',lambda: history(rows,17,'20250103',1))

calendar = ['a','b','c','d']
order = dict(id='one',security=17,decision=0,entry=1,exit=3,notional='100')
entry = {(1,17):'100'}; exits = {(3,17):'110'}
marks = {(1,17):'100',(2,17):'105'}
base = simulate(calendar,[order],entry,exits,marks,'100.10','0.001')
check('independent terminal fee arithmetic', base['daily'][-1]['cash'] == F(10989,100) and base['daily'][-1]['cash']-base['initial']==F(979,100))
check('entry cash fee reservation', base['daily'][1]['cash'] == 0 and base['daily'][1]['nav'] == 100)
check('independent intermediate NAV', base['daily'][2]['nav'] == 105)
check('closed lot fees and conservation', base['lots'][0]['entry_fee'] == F(1,10) and base['lots'][0]['exit_fee'] == F(11,100) and base['daily'][-1]['gross'] == 0)
unfunded = simulate(calendar,[order],entry,exits,marks,'100','0.001')
check('fees cannot cause implicit borrowing', not unfunded['funding_feasible'] and not unfunded['lots'] and unfunded['daily'][-1]['cash'] == 100 and unfunded['orders'][0]['state'] == 'unfilled_cash')
vetoed = simulate(calendar,[order],entry,exits,marks,'100.10','0.001',{'one'})
check('veto remains cash without rescaling', not vetoed['lots'] and vetoed['daily'][-1]['cash'] == F(1001,10))
pair = [dict(order,notional='50'),dict(order,id='two',security=18,notional='50')]
ep = {(1,17):'100',(1,18):'50'}; xp = {(3,17):'110',(3,18):'55'}
mp = {(1,17):'100',(1,18):'50',(2,17):'105',(2,18):'50'}
filtered = simulate(calendar,pair,ep,xp,mp,'100.10','0.001',{'two'})
check('retained original size exact', filtered['lots'][0]['quantity'] == F(1,2) and filtered['orders'][0]['notional'] == 50)
small = simulate(calendar,pair,ep,xp,mp,'75','0')
check('batch shortage all-or-none outcome blind', len(small['lots']) == 0 and all(x['state']=='unfilled_cash' for x in small['orders']))
unmatched = funded_engine.paired(calendar,pair,ep,xp,mp,'75','0',{'two'})
check('differing arm funding blocks isolated overlay claim',not unmatched['matched_retained_schedule'] and not unmatched['isolated_overlay_comparable'])
matched = funded_engine.paired(calendar,pair,ep,xp,mp,'100.10','0.001',{'two'})
check('feasible matched original pair acknowledged',matched['isolated_overlay_comparable'] and matched['candidate']['lots'][0]['quantity']==F(1,2))
iterated = funded_engine.paired(calendar,iter(pair),ep,xp,mp,'100.10','0.001',iter(['two']))
check('iterable inputs cannot silently consume pairing or veto',iterated['isolated_overlay_comparable'] and len(iterated['baseline']['lots'])==2 and len(iterated['candidate']['lots'])==1)
missing = simulate(calendar,[order],{},exits,marks,'100.10','0.001')
check('missing entry unfilled not zero performance', not missing['complete'] and missing['orders'][0]['state'] == 'unfilled_missing_price')
unknown = simulate(calendar,[order],entry,exits,{(1,17):'100'},'100.10','0.001')
check('missing mark unknown NAV', unknown['daily'][2]['nav'] is None)
censored = simulate(calendar,[order],entry,{},dict(marks, **{}),'100.10','0.001')
check('missing exit censored remains invested', not censored['complete'] and censored['lots'][0]['state']=='censored' and censored['daily'][-1]['nav'] is None)
future = simulate(calendar,[dict(order,entry=4,exit=5)],{}, {}, {},'100','0')
check('calendar end entry not fabricated', future['orders'][0]['state']=='not_entered_calendar_end' and not future['complete'])
overlap_orders = [dict(order,id='a',notional='40'),dict(order,id='b',decision=1,entry=2,exit=3,notional='30')]
overlap = simulate(calendar,overlap_orders,{(1,17):'10',(2,17):'10'},{(3,17):'11'},{(1,17):'10',(2,17):'12'},'100','0')
check('overlapping lots independent hand ledger', overlap['daily'][2]['cash']==30 and overlap['daily'][2]['gross']==84 and overlap['daily'][-1]['cash']==107)
roll_orders = [dict(order,exit=2),dict(order,id='roll',decision=1,entry=2,exit=3)]
roll = simulate(calendar,roll_orders,{(1,17):'100',(2,17):'100'},{(2,17):'100',(3,17):'100'},{(1,17):'100',(2,17):'100'},'100','0')
check('explicit open exits before open entries', roll['funding_feasible'] and len(roll['lots'])==2 and roll['daily'][-1]['cash']==100)
for name, bad_orders in [('future decision endpoint rejected',[dict(order,decision=1)]), ('same open roundtrip rejected',[dict(order,exit=1)]), ('duplicate order rejected',[order,order])]:
    fails(name, lambda bad_orders=bad_orders: simulate(calendar,bad_orders,entry,exits,marks,'100','0'))
fails('float ledger price rejected', lambda: simulate(calendar,[order],{(1,17):100.0},exits,marks,'100.10','0.001'))
fails('unsorted calendar rejected', lambda: simulate(['b','a'],[],{}, {}, {},'100','0'))

def load_bytes(values):
    return json.loads(values['input'])
def evaluate(engine, values):
    return engine.compute(values['value'])
def evaluator_failure(engine, values):
    raise RuntimeError('intentional synthetic failure')
def evaluator_mutation(engine, values):
    path = Path(engine.__file__)
    path.write_bytes(path.read_bytes()+b'\n# injected mutation\n')
    return engine.compute(values['value'])
def load_funding(values):
    return json.loads(values['input'])
def encode_exact(value):
    if isinstance(value,F):
        return f'{value.numerator}/{value.denominator}'
    if isinstance(value,dict):
        return {key:encode_exact(item) for key,item in value.items()}
    if isinstance(value,list):
        return [encode_exact(item) for item in value]
    return value
def evaluate_funding(engine, values):
    bars=normalize(values['bars'])
    mappings={name:{(day,identity):price for day,identity,price in values[name]} for name in ('entry_prices','exit_prices','marks')}
    result=engine.simulate(values['calendar'],values['orders'],**mappings,capital=values['capital'],fee=values['fee'])
    return {'bars':bars,'ledger':encode_exact(result)}

def imported(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    (root/'dependency.py').write_text('def scale(value):\n    return value*2\n',encoding='utf-8')
    dep = imported(root/'dependency.py','synthetic_dependency')
    (root/'engine.py').write_text('from synthetic_dependency import scale\ndef compute(value):\n    return scale(value)+1\n',encoding='utf-8')
    engine = imported(root/'engine.py','synthetic_engine')
    data = root/'data.json';data.write_text('{"value":3}',encoding='utf-8')
    manifest = source_manifest(engine,root)
    check('actual engine and imported-function dependency discovered', set(manifest)=={'engine.py','dependency.py'})
    omitted = {name:value for name,value in manifest.items() if name!='engine.py'}
    fails('original omitted-engine receipt bug rejected', lambda: verify_sources(omitted,engine,root))
    result = execute(root/'ok',engine,root,{'trial_budget':0},{'input':data},{data},load_bytes,evaluate)
    receipt = json.loads((root/'ok'/'receipt.json').read_text())
    check('receipt complete with engine input protocol callback binding', result==7 and receipt['state']=='complete' and receipt['engine']=='engine.py' and receipt['input_sha256'] and receipt['protocol_sha256'] and receipt['callbacks'])
    check('exact input snapshot retained', next((root/'ok'/'inputs').iterdir()).read_bytes()==data.read_bytes())
    fails('attempt reuse rejected',lambda: execute(root/'ok',engine,root,{}, {'input':data},{data},load_bytes,evaluate),FileExistsError)
    fails('protected input before loader rejected',lambda: execute(root/'protected',engine,root,{}, {'input':data},set(),load_bytes,evaluate))
    check('protected attempt records failure without input reads', json.loads((root/'protected'/'receipt.json').read_text())['state']=='failed' and not (root/'protected'/'inputs').exists())
    fails('evaluator failure retained',lambda: execute(root/'bad-eval',engine,root,{}, {'input':data},{data},load_bytes,evaluator_failure),RuntimeError)
    check('failed evaluator never produces success', json.loads((root/'bad-eval'/'receipt.json').read_text())['state']=='failed' and not (root/'bad-eval'/'result.json').exists())
    original_engine=(root/'engine.py').read_bytes()
    fails('mid-execution mutation rejects result',lambda: execute(root/'mutated',engine,root,{}, {'input':data},{data},load_bytes,evaluator_mutation))
    check('mutated execution has no successful output',json.loads((root/'mutated'/'receipt.json').read_text())['state']=='failed' and not (root/'mutated'/'result.json').exists())
    (root/'engine.py').write_bytes(original_engine)
    (root/'dependency.py').write_text('def scale(value):\n    return value*3\n',encoding='utf-8')
    fails('stale imported function rejected',lambda: source_manifest(engine,root))
    (root/'dependency.py').write_text('def scale(value):\n    return value*2\n# changed bytes\n',encoding='utf-8')
    fails('dependency byte mutation rejected',lambda: verify_sources(manifest,engine,root))
    (root/'engine.py').write_text('def compute(value):\n    return value-1\n',encoding='utf-8')
    fails('stale main engine rejected',lambda: source_manifest(engine,root))
    payload=dict(bars=[row],calendar=calendar,orders=[order],entry_prices=[[1,17,'100']],exit_prices=[[3,17,'110']],marks=[[1,17,'100'],[2,17,'105']],capital='100.10',fee='0.001')
    data.write_text(json.dumps(payload),encoding='utf-8')
    integrated=execute(root/'integrated',funded_engine,ROOT,{'scope':'synthetic','trial_budget':0}, {'input':data},{data},load_funding,evaluate_funding)
    integrated_receipt=json.loads((root/'integrated'/'receipt.json').read_text())
    check('guarded lossless funded integration',integrated['ledger']['daily'][-1]['cash']=='10989/100' and integrated['bars'][0]['open']==row['open'])
    check('integration binds all local execution dependencies',{'research/funded_ledger.py','research/lossless_inputs.py','research/execution_guard.py','scripts/check_research_integrity.py'}.issubset(integrated_receipt['source']))

print(json.dumps({'passed':True,'checks':len(checks),'cases':checks,'scope':'synthetic infrastructure only; zero market experiments'}))
