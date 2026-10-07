from pathlib import Path
import json,hashlib,importlib.util
from decimal import Decimal as D
from fractions import Fraction as F
from dataclasses import replace
import sys, tempfile, subprocess
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"fixtures"))
from m2_foundation import Field,available,classify_stock,classify_market,gate,asof,pullback,rank_weights,compare,SyntheticAccount
OUT=Path(__file__).resolve().parent;checks=[];outputs={}
def check(name,actual,expected):
    checks.append({'name':name,'actual':actual,'expected':expected,'passed':actual==expected})
def field(v,session='current',observed=100,known=105,completed=100,qualified=True):return Field(None if v is None else D(v),session,observed,known,completed,qualified)
close=field(110);low=field(100,'prior',90,95,90)
def stock(c=close,l=low):return classify_stock(c,l,'current','prior',110,30)
market=classify_market(close,field(105,'prior',90,95,90),low,'current','prior',110,30)
check('stock_above',stock()['state'],'aligned');check('stock_below',stock(field(99))['state'],'conflicting');check('stock_equal',stock(field(100))['state'],'neutral')
check('market_uptrend',market['state'],'aligned')
check('market_downtrend',classify_market(field(90),field(95,'prior',90,95,90),low,'current','prior',110,30)['state'],'conflicting')
check('market_equal',classify_market(field(105),field(105,'prior',90,95,90),low,'current','prior',110,30)['state'],'neutral')
for name,c,reason in [('late',replace(close,known=111),'late'),('clockless',replace(close,known=None),'missing_clock'),('wrong_session',replace(close,session='prior'),'wrong_session'),('stale',replace(close,observed=79),'stale'),('future',replace(close,observed=111,known=111),'future_observation'),('unqualified',replace(close,qualified=False),'unqualified_source'),('missing',replace(close,value=None),'missing_or_invalid_value'),('nan',replace(close,value=D('NaN')),'missing_or_invalid_value'),('negative',replace(close,value=D(-1)),'missing_or_invalid_value'),('clock_order',replace(close,observed=106),'clock_order')]:
    result=stock(c);check(name,result['state'],'unknown');check(name+'_reason',reason in result['reasons'],True)
check('known_equal_decision',stock(replace(close,known=110))['state'],'aligned')
check('future_completion',stock(replace(close,completed=111))['state'],'unknown')
check('known_before_finalization',stock(replace(close,known=100,completed=105))['state'],'unknown')
check('neutral_stock_admitted',gate(stock(field(100)),market),True)
check('neutral_market_veto',gate(stock(),{'state':'neutral'}),False)
check('unknown_market_veto',gate(stock(),{'state':'unknown'}),False)
prefix=[low,close];future=field(1,'future',200,205,200);late_revision=replace(close,value=D(1),known=111)
check('future_invariance',asof(prefix,110)==asof(prefix+[future],110),True)
check('late_revision_invariance',asof(prefix,110)==asof(prefix+[late_revision],110),True)
check('pullback_pass',pullback(D(110),D(112),D(105),D(100),D(50_000_000)),True)
check('pullback_equal_rejected',pullback(D(110),D(110),D(105),D(100),D(50_000_000)),False)
check('uptrend_equal_rejected',pullback(D(110),D(112),D(110),D(100),D(50_000_000)),False)
weights=rank_weights([F(-2,100),F(0),F(2,100)])
check('weights_3',weights,(F(1,2),F(1,3),F(1,6)))
check('tie_weights',rank_weights([F(-1),F(-1),F(1)]),(F(5,12),F(5,12),F(1,6)))
check('weights_sum',sum(weights),F(1))
r=compare(weights,[False,True,False],[F(-21,1000),F(9,1000),F(19,1000)])
outputs['matched']=r
check('cash_no_rescaling',r['cash'],F(2,3));check('retained_weight',r['retained'],(F(0),F(1,3),F(0)))
check('avoided_loss_net_fee',r['avoided_losses'],F(21,2000));check('sacrificed_winner_net_fee',r['sacrificed_winners'],F(19,6000))
check('incremental_handworked',r['incremental'],F(11,1500))
check('paired_economics_identity',r['incremental'],r['avoided_losses']-r['sacrificed_winners'])
stressed=compare(weights,[False,True,False],[F(-21,1000),F(9,1000),F(19,1000)],F(1,1000))
outputs['stressed']=stressed
check('differential_cost_cash_excluded',stressed['differential_cost'],F(1,3000))
check('differential_cost_increment',stressed['incremental'],F(7,1000))
censored=compare(weights,[False,True,False],[None,F(9,1000),F(19,1000)])
outputs['censored']=censored;check('censored_scanner',censored['scanner'],None);check('censored_increment',censored['incremental'],None);check('censored_rows_retained',censored['opportunities'],3)
a=SyntheticAccount('1000');a.reserve('402');a.buy('A',4,'100','2','402');a.reserve('201');a.buy('B',2,'100','1','201')
check('overlap_cash',a.cash,D(397));check('overlap_equity_net_fees',a.equity({'A':'100','B':'100'}),D(997))
a.dividend('A','0.50');a.split('A',2)
check('split_dividend_equity',a.equity({'A':'50','B':'100'}),D(999))
check('unmarked_position_unknown',a.equity({'A':'50'}),None)
a.sell('A',8,'55','2');a.sell('B',2,'95','1')
check('final_cash',a.cash,D(1026));check('flat_equity',a.equity({}),D(1026));check('reservation_empty',a.reserved,D(0))
a.reserve('100');check('reservation_equity_unchanged',a.equity({}),D(1026));a.cancel('100');check('cancel_releases_cash',a.reserved,D(0))
for name,fn in [('overreserve',lambda:a.reserve('1027')),('oversell',lambda:a.sell('A',1,'55','0')),('fractional_quantity',lambda:a.buy('A',1.5,'10','0','20'))]:
    try:fn();raised=False
    except ValueError:raised=True
    check(name,raised,True)
spec=importlib.util.spec_from_file_location('date_only',ROOT/'fixtures/chronology.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
loader_calls=[]
registry={'final_confirmation':{'status':'blocked','access_enabled':False,'start':None,'end':None}}
for name,contract in [('actual_disabled',registry['final_confirmation']),('forged_enabled',{'status':'qualified','access_enabled':True,'start':'x','end':'y'})]:
    try:module.guarded_confirmation_read(contract,lambda:loader_calls.append(1));raised=False
    except PermissionError:raised=True
    check('final_guard_'+name,raised,True)
check('guard_before_io',len(loader_calls),0)
sessions=['2025-12-29','2025-12-30','2025-12-31','2026-01-02','2026-01-05']
check('path_split_rejected',module.holding_path(sessions,'2025-12-30',2,'2025-09-11','2025-12-31'),None)
check('path_exact_sessions',module.holding_path(sessions,'2025-12-29',2,'2025-09-11','2025-12-31'),['2025-12-30','2025-12-31'])
result={'checks':checks,'outputs':outputs,'scope':'synthetic foundations only; incomplete SR-004/SR-025','market_replays':0,
  'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'reports/M2-readiness.md',ROOT/'fixtures/m2_foundation.py',Path(__file__)]}}
with tempfile.TemporaryDirectory() as scratch:
    artifact=Path(scratch)/'checks.json'
    artifact.write_text(json.dumps(result,indent=2,default=str)+'\n')
    subprocess.run([sys.executable,str(ROOT/'scripts/verify_m2.py'),str(artifact)],check=True)
failed=[c['name'] for c in checks if not c['passed']]
print(json.dumps({'checks':len(checks),'failed':failed}));assert not failed
