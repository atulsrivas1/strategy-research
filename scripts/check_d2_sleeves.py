"""Actual artificial D2/CLI and independent compound bootstrap witnesses."""
from pathlib import Path
from datetime import date,timedelta
from decimal import Decimal as D
from fractions import Fraction as F
from collections import Counter
import sys,json,copy,hashlib,tempfile,subprocess,random,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'research'))
sys.set_int_max_str_digits(0)  # Exact compounded rational witnesses, as in the CLI.
import d2_sleeves as engine
import run_d2_sleeves as runner
import execution_guard as guard
checks=[]
def check(name,ok):assert ok,name;checks.append(name)
def fails(name,fn):
    try:fn()
    except ValueError:checks.append(name)
    else:raise AssertionError(name)
p=engine.protocol();cal=[];day=date(2022,1,3)
while len(cal)<280:
    if day.weekday()<5:cal.append(day.isoformat())
    day+=timedelta(days=1)
u=[dict(instrument_id=101+k,symbol=s) for k,s in enumerate(p['symbols'])];rows=[]
for i,day in enumerate(cal):
    for k,security in enumerate(u,1):
        price=D(100)+D(i*k)/100
        rows.append(dict(**security,date=day,open=str(price),close=str(price),high=str(price+1),low=str(price-1),volume=100,source='artificial',units='synthetic USD/share',actions='synthetic none',clock_assumption='modeled synthetic',start=day+'T00:00:00Z',available_at=None))
dec=cal[252:267]
meta=dict(basis=p['settlement_basis'],source='artificial schedule',clock_assumption='synthetic one session maturity close',price_calendar_sha256=hashlib.sha256(json.dumps(cal,separators=(',',':')).encode()).hexdigest(),maturities={d:cal.index(d)+8 for d in dec})
b=dict(kind='synthetic',final_access=False,calendar=cal,decisions=dec,universe=u,bars=rows,action_basis=p['action_basis'],split_events=[],settlement=meta)
r=engine.evaluate(b)
check('synthetic cannot report market success',r['verdict']=='synthetic witness only')
check('all three primary fee arms usable',all(c['primary_usable'] for c in r['costs']))
check('benchmark schedule generated independently',len(r['benchmark_ledger']['groups'])==len(dec))
check('frozen top3 rank retained',r['screens'][0]['selected']==[118,117,116])
check('compound arms have independent own budgets',r['ledger']['baseline']['budgets'][dec[7]]!=r['benchmark_ledger']['budgets'][dec[7]])
check('three configurations per three fee arms',p['arm_fee_configurations']==9 and len(r['costs'])==3)
check('seven sleeve assignments preserved',all(g['sleeve']==j%7 for j,g in enumerate(r['ledger']['baseline']['groups'])))
check('actual purchase concentration and omissions reported',F(r['costs'][0]['scanner']['maximum_security_purchase_share'])==F(1,3) and r['costs'][0]['scanner']['unfilled_groups']==0)
check('active interval includes first fill through last exit',r['active_sessions']==20)
check('point log telescopes independently',abs(float(F(r['costs'][0]['paired_log_point']))-math.log(float(F(r['costs'][0]['scanner']['terminal_nav'])/F(r['costs'][0]['benchmark']['terminal_nav']))))<1e-12)
values=[F(v) for v in r['primary_logs']];rng=random.Random(4102);samples=[]
for _ in range(1000):
    counts=Counter();length=0
    while length<len(values):
        start=rng.randrange(len(values))
        for j in range(min(20,len(values)-length)):counts[(start+j)%len(values)]+=1
        length+=20
    samples.append(sum((values[i]*n for i,n in counts.items()),F(0)))
samples.sort()
check('independent count-weighted compound bootstrap exact endpoints',[F(v) for v in r['primary_log_interval']]==[samples[24],samples[974]])
check('no fabricated market state',all(s['market']=='unknown' for s in r['screens']))
conflict=copy.deepcopy(b)
for row in conflict['bars']:
    if row['instrument_id']==118 and row['date']==dec[0]:row['close']='99';row['low']='98'
    if row['instrument_id']==118 and row['date']==cal[259]:row['open']='300';row['high']='301'
cr=engine.evaluate(conflict)
check('integrated context funding mismatch cannot contaminate primary',cr['costs'][0]['primary_usable'] and not cr['costs'][0]['context_usable'] and cr['diagnostic']['avoided_losses'] is None and cr['diagnostic']['sacrificed_winners'] is None)
blocked=copy.deepcopy(b);blocked['bars']=[row for row in blocked['bars'] if not(row['instrument_id']==101 and row['date']==cal[100])]
br=engine.evaluate(blocked)
check('missing cohort history affects primary only, benchmark independently funded',not any(c['primary_usable'] for c in br['costs']) and br['benchmark_ledger']['complete'])
bad=copy.deepcopy(b);bad['settlement']['maturities'][dec[0]]=261
late=engine.evaluate(bad)
check('known later settlement blocks next reuse without selecting dates',not late['costs'][0]['primary_usable'] and len(late['screens'])==15)
fails('wrong settlement calendar hash rejected',lambda:engine.evaluate(dict(b,settlement=dict(meta,price_calendar_sha256='0'*64))))
fails('omitted settlement coverage rejected',lambda:engine.evaluate(dict(b,settlement=dict(meta,maturities={}))))
fails('protected kind rejected',lambda:engine.evaluate(dict(b,kind='final',final_access=True)))
fails('unknown stable cohort cannot be pruned',lambda:engine.evaluate(dict(b,universe=u[:-1])))
with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);bundle=root/'bundle.json';bundle.write_text(json.dumps(b),encoding='utf-8')
    ad=dict(kind='synthetic',bundle=str(bundle),sha256=hashlib.sha256(bundle.read_bytes()).hexdigest(),start=cal[0],end=cal[-1],final_access=False,protected_ranges_reviewed=True,protected_ranges=[],exposure='synthetic')
    admission=root/'admission.json';admission.write_text(json.dumps(ad),encoding='utf-8');attempt=root/'attempt'
    result=subprocess.run([sys.executable,str(ROOT/'research/run_d2_sleeves.py'),'--admission',str(admission),'--attempt',str(attempt)],capture_output=True,text=True)
    check('actual guarded synthetic CLI succeeds',result.returncode==0)
    receipt=json.loads((attempt/'receipt.json').read_text())
    check('actual receipt complete with engine runner ledger and split dependencies',receipt['state']=='complete' and all(n in receipt['source'] for n in ('research/d2_sleeves.py','research/run_d2_sleeves.py','research/sleeve_ledger.py','research/split_actions.py','research/d2_funded_v3.py')))
    check('actual result and input hashes match',receipt['input_sha256']['bundle']==ad['sha256'] and receipt['result_sha256']==hashlib.sha256((attempt/'result.json').read_bytes()).hexdigest())
    unsafe=dict(ad,protected_ranges=[[cal[0],cal[-1]]]);admission.write_text(json.dumps(unsafe),encoding='utf-8')
    blocked_attempt=root/'protected'
    try:runner.run(admission,blocked_attempt)
    except ValueError:pass
    else:raise AssertionError('protected accepted')
    check('protected preflight rejects before bundle snapshot',json.loads((blocked_attempt/'receipt.json').read_text())['state']=='failed' and not (blocked_attempt/'inputs').exists())
    settlement=root/'settlement.json';settlement.write_text(json.dumps(meta),encoding='utf-8')
    dev=dict(kind='development',experiment_id='D2-SLEEVES-DEV-1',registry=str(root/'registry.json'),bundle=str(root/'absent.json'),sha256='0'*64,start=p['input_start'],end=p['input_end'],final_access=False,exposure='potentially exposed development',protected_ranges_reviewed=True,protected_ranges=[],protocol_version=p['version'],price_basis=p['price_basis'],action_basis=p['action_basis'],settlement_map=str(settlement),settlement_sha256=hashlib.sha256(settlement.read_bytes()).hexdigest())
    source=guard.source_manifest(engine,ROOT);source.update(guard.source_manifest(runner,ROOT))
    reg=dict(experiment_id=p['experiment_id'],protocol=p,registry=dev['registry'],bundle=dev['bundle'],bundle_sha256=dev['sha256'],source=source,admission_scope=dict(dev))
    registration=root/'registration.json';registration.write_text(json.dumps(reg),encoding='utf-8');dev.update(registration=str(registration),registration_sha256=hashlib.sha256(registration.read_bytes()).hexdigest())
    check('metadata-only frozen actual registration check',runner.registration_check(dev)['protocol']==p)
    fails('changed protocol cannot pass registration',lambda:runner.registration_check(dict(dev,protocol_version='other')))
    fails('changed protection cannot pass registration',lambda:runner.registration_check(dict(dev,protected_ranges=[[p['input_start'],p['input_end']]])))
    fails('wrong settlement bytes rejected before absent bundle',lambda:runner.admission_check(dict(dev,settlement_sha256='0'*64),dev['bundle']))
    check('no development budget was claimed in metadata tests',not Path(dev['registry']).exists())
print(json.dumps(dict(checks=len(checks),passed=True,scope='synthetic D2 and guarded CLI only; no real trial or registration')))
