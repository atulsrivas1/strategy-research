"""Artificial strategy/CLI witnesses; no market data, no profitability evidence."""
from pathlib import Path
from datetime import date,timedelta
from decimal import Decimal as D
from fractions import Fraction as F
import copy,json,hashlib,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'research'))
import d2_funded_v2 as engine
import run_d2_funded_v2 as runner

checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
def fails(name,function):
    try:function()
    except ValueError:checks.append(name)
    else:raise AssertionError(name)

p=engine.protocol();calendar=[];day=date(2022,1,3)
while len(calendar)<269:
    if day.weekday()<5:calendar.append(day.isoformat())
    day+=timedelta(days=1)
universe=[dict(instrument_id=100+k,symbol=symbol) for k,symbol in enumerate(p['symbols'],1)]
rows=[]
for i,day in enumerate(calendar):
    for k,security in enumerate(universe,1):
        close=D(100)+D(i*k)/100
        rows.append(dict(**security,date=day,open=str(close),close=str(close),high=str(close+1),low=str(close-1),volume=100,source='artificial',units='synthetic USD/share',actions='synthetic none',clock_assumption='synthetic modeled calendar',start=day+'T00:00:00Z',available_at=None))
bundle=dict(kind='synthetic',final_access=False,calendar=calendar,decisions=calendar[252:262],universe=universe,bars=rows)
bars={(row['instrument_id'],row['date']):row for row in rows}
ranking=engine.select(bars,calendar,252,[row['instrument_id'] for row in universe])
check('hand long formation rank',ranking['selected']==[118,117,116] and F(ranking['scores']['118'])==F(231*18,10000))
future=copy.deepcopy(bars);future[(118,calendar[254])]['close']='1'
check('future endpoint cannot change past ranking',engine.select(future,calendar,252,[r['instrument_id'] for r in universe])==ranking)
recent=copy.deepcopy(bars);recent[(118,calendar[252])]['close']='99'
recent_rank=engine.select(recent,calendar,252,[r['instrument_id'] for r in universe])
check('skip window ranking independent from recent context',recent_rank['selected']==ranking['selected'] and recent_rank['stock'][118]=='conflicting')
late=copy.deepcopy(bars);late[(118,calendar[231])]['available_at']=calendar[253]+'T00:00:00Z'
check('late known ranking endpoint unresolved',engine.select(late,calendar,252,[r['instrument_id'] for r in universe])['status']=='unresolved')
missing=copy.deepcopy(bars);missing.pop((101,calendar[100]))
check('missing cohort member cannot be pruned',engine.select(missing,calendar,252,[r['instrument_id'] for r in universe])['status']=='unresolved')
tie=copy.deepcopy(bars);tie[(115,calendar[231])]['close']=tie[(116,calendar[231])]['close']
check('exact selection boundary tie preserved',engine.select(tie,calendar,252,[r['instrument_id'] for r in universe])['reason']=='selection boundary tie')
precision=copy.deepcopy(tie);precision[(116,calendar[231])]['close']=str(D(precision[(116,calendar[231])]['close'])+D('0.000000000000001'))
check('subfloat rank difference retained',engine.select(precision,calendar,252,[r['instrument_id'] for r in universe])['selected']==[118,117,116])
fails('early history cannot negative-index',lambda:engine.select(bars,calendar,5,[r['instrument_id'] for r in universe]))
result=engine.evaluate(bundle)
check('synthetic cannot produce performance verdict',result['verdict']=='synthetic witness only' and not result['support_sufficient'])
check('nine declared arm fee configurations',len(result['costs'])==3 and len(result['protocol']['fees'])==3 and result['protocol']['arm_fee_configurations']==9)
check('primary and diagnostic separated',result['diagnostic']['promotion_allowed'] is False and result['protocol']['primary']=='scanner-minus-equal-cohort')
check('scanner versus benchmark original total notionals match',sum(F(o['notional']) for o in result['scanner_orders'])==sum(F(o['notional']) for o in result['benchmark_orders']))
check('fee reserve bounds aggregate purchases',sum(F(o['notional'])*(1+F('.003')) for o in result['scanner_orders'])==1)
check('all retained original filled with nonnegative exact cash',all(F(row['cash'])>=0 for row in result['ledger']['baseline']['daily']) and all(cost['usable'] for cost in result['costs']))
check('cash plus marked positions independent conservation',all(F(row['cash'])+F(row['gross'])==F(row['nav']) for row in result['ledger']['baseline']['daily']))
blocked=copy.deepcopy(bundle);blocked['bars']=[row for row in blocked['bars'] if not(row['instrument_id']==101 and row['date']==calendar[100])]
blocked_result=engine.evaluate(blocked)
check('benchmark schedule independent of blocked scanner',len(blocked_result['scanner_orders'])==0 and len(blocked_result['benchmark_orders'])==180 and not any(c['usable'] for c in blocked_result['costs']))
censored=copy.deepcopy(bundle);censored['bars']=[row for row in censored['bars'] if not(row['instrument_id']==118 and row['date']==calendar[268])]
check('missing final exit retains censorship',not engine.evaluate(censored)['costs'][0]['usable'])
fails('wrong stable ID map rejected',lambda:engine.evaluate(dict(bundle,universe=[dict(r,instrument_id=101) for r in universe])))
mixed=copy.deepcopy(bundle);mixed['bars'][0]['units']='different currency/share'
fails('known mixed units cannot be ignored',lambda:engine.evaluate(mixed))
fails('protected scope rejected',lambda:engine.evaluate(dict(bundle,kind='final',final_access=True)))
fails('holding endpoint beyond calendar rejected',lambda:engine.evaluate(dict(bundle,decisions=[calendar[-1]])))
check('seeded block interval reproducible',engine.interval([F(1),F(2),F(3)])==engine.interval([F(1),F(2),F(3)]))
check('all-negative hand interval',engine.interval([F(-1)]*25)==[F(-25),F(-25)])
check('nonpositive point with crossing interval inconclusive',engine.classify(F(-1),[F(-2),F(1)],True,True,[F(-1)]) .startswith('inconclusive'))
check('negative supported interval rejected',engine.classify(F(-1),[F(-2),F(-1,10)],True,True,[F(-1)])=='rejected tested scanner')
check('positive supported stress stable permitted only exploratory',engine.classify(F(1),[F(1,10),F(2)],True,True,[F(1,2)])=='promising exploratory under assumptions')
check('support and funding cannot be bypassed',engine.classify(F(1),[F(1,10),F(2)],False,True,[F(1)]).startswith('inconclusive') and engine.classify(F(1),[F(1,10),F(2)],True,False,[F(1)]).startswith('inconclusive'))

with tempfile.TemporaryDirectory() as directory:
    root=Path(directory);path=root/'bundle.json';raw=json.dumps(bundle).encode();path.write_bytes(raw)
    admission=dict(kind='synthetic',bundle=str(path),sha256=hashlib.sha256(raw).hexdigest(),final_access=False,start=calendar[0],end=calendar[-1],protected_ranges_reviewed=True,protected_ranges=[])
    manifest=root/'admission.json';manifest.write_text(json.dumps(admission),encoding='utf-8')
    cli=subprocess.run([sys.executable,str(ROOT/'research/run_d2_funded_v2.py'),'--admission',str(manifest),'--attempt',str(root/'attempt')],capture_output=True,text=True)
    check('actual guarded CLI succeeds on artificial inputs',cli.returncode==0 and json.loads(cli.stdout)['verdict']=='synthetic witness only')
    receipt=json.loads((root/'attempt/receipt.json').read_text())
    check('actual engine runner adapter ledger guard source binding',{'research/d2_funded_v2.py','research/run_d2_funded_v2.py','research/lossless_inputs.py','research/funded_ledger.py','research/execution_guard.py'}.issubset(receipt['source']) and receipt['state']=='complete')
    bad=dict(admission,protected_ranges=[[calendar[0],calendar[0]]],bundle=str(root/'absent.json'))
    fails('protected metadata rejects before absent bundle read',lambda:runner.admission_check(bad,root/'absent.json'))
    manifest.write_text(json.dumps(bad),encoding='utf-8')
    fails('protected run retains failed preflight',lambda:runner.run(manifest,root/'protected'))
    check('preflight failure preserves no market snapshot',json.loads((root/'protected/receipt.json').read_text())['phase']=='admission before bundle read' and not(root/'protected/inputs').exists())
    manifest.write_text(json.dumps(dict(admission,sha256='0'*64)),encoding='utf-8')
    fails('changed admitted bytes rejected',lambda:runner.run(manifest,root/'wrong-hash'))
    check('wrong hash attempt failed without result',json.loads((root/'wrong-hash/receipt.json').read_text())['state']=='failed' and not(root/'wrong-hash/result.json').exists())
    budget=runner.claim({'registry':str(root/'artificial-registry.json')},root/'artificial-attempt')
    check('one declared budget claimed before outcomes',json.loads(budget.read_text())['arm_fee_configurations']==9)
    try:runner.claim({'registry':str(budget)},root/'second-artificial-attempt')
    except FileExistsError:check('second experiment claim cannot overwrite consumed budget',json.loads(budget.read_text())['attempt'].endswith('artificial-attempt'))
    else:raise AssertionError('repeat budget claim')

print(json.dumps({'checks':len(checks),'passed':True,'cases':checks,'market_experiments':0,'scope':'synthetic D2 adoption only'}))
