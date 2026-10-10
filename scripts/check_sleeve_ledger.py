"""Hand-derived actual sleeve accounting and chronology witnesses; synthetic only."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal
import sys,copy,json,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'research'))
import sleeve_ledger as ledger
import d2_sleeves as engine
checks=[]
def check(name,ok):assert ok,name;checks.append(name)
def fails(name,fn):
    try:fn()
    except ValueError:checks.append(name)
    else:raise AssertionError(name)
cal=[f'2026-01-{i+1:02}' for i in range(20)]
g=dict(id='a',decision=0,entry=2,exit=7,sleeve=0,settlement_close=8,securities=[1,2,3])
g2=dict(g,id='b',decision=7,entry=9,exit=14,settlement_close=15)
op={(t,s):'10' for t in range(20) for s in (1,2,3)};marks=dict(op)
r=ledger.simulate(cal,[g,g2],op,marks,fee='0')
n=F(1,7)/F('1.003');q=n/30
check('prior-close exact budget',r['budgets']['a']==n)
check('entry shares and fees',r['lots'][0]['quantity']==q and r['lots'][0]['entry_fee']==0)
check('sale creates receivable, not spendable cash',r['daily'][7]['receivables']==n and r['daily'][7]['sleeve_cash'][0]==F(1,7)-n)
check('receipt maturity conserves NAV',r['daily'][7]['nav']==r['daily'][8]['nav']==1 and r['daily'][8]['receivables']==0)
check('next cycle cash recycled only after maturity close',r['budgets']['b']==n and r['groups'][1]['state']=='entered')
check('no transfers to other sleeves',all(r['daily'][t]['sleeve_cash'][s]==F(1,7) for t in range(20) for s in range(1,7)))
check('cash plus receivables plus holdings equals NAV',all(d['cash']+d['receivables']+d['gross']==d['nav'] for d in r['daily']))
cost=ledger.simulate(cal,[g],op,marks,fee='.003')
check('actual maximum cost reserve prevents borrowing',cost['daily'][2]['sleeve_cash'][0]==0)
check('roundtrip flat-price fees exact',cost['daily'][-1]['nav']==1-2*n*F('.003'))
up=dict(op);up[7,1]='20';up[7,2]='20';up[7,3]='20'
gain=ledger.simulate(cal,[g,g2],up,marks,fee='0')
check('own realized gain sizes next close budget',gain['budgets']['b']==(F(1,7)+n)/F('1.003'))
down=dict(op);down.update({(7,s):'5' for s in (1,2,3)})
loss=ledger.simulate(cal,[g,g2],down,marks,fee='0')
check('own loss shrinks next budget',loss['budgets']['b']==(F(1,7)-n/2)/F('1.003'))
future=dict(op);future.update({(14,s):'1000' for s in (1,2,3)})
check('future exit cannot change earlier budget',ledger.simulate(cal,[g,g2],future,marks,fee='0')['budgets']==r['budgets'])
futuremark=dict(marks);futuremark[9,1]='1000'
check('future mark cannot change entry budget',ledger.simulate(cal,[g,g2],op,futuremark,fee='0')['budgets']==r['budgets'])
delayed=ledger.simulate(cal,[dict(g,settlement_close=9),g2],op,marks,fee='0')
check('settlement at entry close is too late for entry open',delayed['groups'][1]['state']=='unresolved_budget' and not delayed['complete'])
unknown=ledger.simulate(cal,[dict(g,settlement_close=None),g2],op,marks,fee='0')
check('unknown maturity blocks reuse but receipt remains valued',unknown['groups'][1]['state']=='unresolved_budget' and unknown['daily'][-1]['receivables']==n)
terminal=ledger.simulate(cal[:8],[dict(g,settlement_close=8)],op,marks,fee='0')
check('terminal known receivable remains in wealth',terminal['complete'] and terminal['daily'][-1]['nav']==1 and terminal['daily'][-1]['receivables']==n)
missing=dict(op);missing.pop((7,1))
censor=ledger.simulate(cal,[g,g2],missing,marks,fee='0')
check('censored old lot blocks sleeve reuse',not censor['complete'] and censor['groups'][1]['state']=='unresolved_budget')
missingentry=dict(op);missingentry.pop((2,1))
check('missing entry all-or-none',not ledger.simulate(cal,[g],missingentry,marks)['lots'])
missingmark=dict(marks);missingmark.pop((3,1))
check('missing holding mark unknown NAV',ledger.simulate(cal,[g],op,missingmark)['daily'][3]['nav'] is None)
event=dict(id='split',instrument_id=1,symbol='A',kind='split',ratio='10',cashflow='0',publication_date='2025-12-01',effective_date=cal[4],available_at='2025-12-01T23:59:59Z',source='synthetic',clock_assumption='synthetic',input_basis='raw_share_units')
splitop=dict(op);splitmarks=dict(marks)
for t in range(4,20):splitop[t,1]='1';splitmarks[t,1]='1'
split=ledger.simulate(cal,[g],splitop,splitmarks,fee='0',events=[event])
check('forward split shares conserve market value',split['lots'][0]['quantity']==10*q and all(d['nav']==1 for d in split['daily']))
reverse=dict(event,ratio='1/10');revop=dict(op);revmarks=dict(marks)
for t in range(4,20):revop[t,1]='100';revmarks[t,1]='100'
check('reverse split conservation',ledger.simulate(cal,[g],revop,revmarks,fee='0',events=[reverse])['daily'][-1]['nav']==1)
late=dict(event,available_at=cal[5]+'T23:59:59Z')
check('late split evidence never retrofills held lot',ledger.simulate(cal,[g],splitop,splitmarks,events=[late])['daily'][5]['nav'] is None)
pair=ledger.paired(cal,[g,g2],up,marks,'1','0',[],{('a',1)})
check('candidate cannot borrow to match sacrificed winner growth',pair['baseline']['complete'] and not pair['candidate']['complete'] and not pair['isolated_overlay_comparable'])
pair0=ledger.paired(cal,[g],op,marks,'1','0',[],{('a',1)})
check('retained original notionals not rescaled',pair0['isolated_overlay_comparable'] and all(l['notional']==n/3 for l in pair0['candidate']['lots']))
check('no-veto paired identity',ledger.paired(cal,[g],op,marks,'1','0',[],set())['baseline']==ledger.paired(cal,[g],op,marks,'1','0',[],set())['candidate'])
fails('same-day maturity rejected',lambda:ledger.simulate(cal,[dict(g,settlement_close=7)],op,marks))
fails('duplicate sleeve entry rejected',lambda:ledger.simulate(cal,[g,dict(g,id='z')],op,marks))
fails('lossy cash float rejected',lambda:ledger.simulate(cal,[g],op,marks,capital=1.0))
fails('fee above fixed reserve rejected',lambda:ledger.simulate(cal,[g],op,marks,fee='.004'))
fails('unknown veto rejected',lambda:ledger.simulate(cal,[g],op,marks,veto={('a',999)}))
fails('partial reference schedule rejected',lambda:ledger.simulate(cal,[g,g2],op,marks,reference={'a':n}))
navs=[F(1),F(11,10),F(99,100),F(6,5)]
logs=[engine.log_ratio(b,a) for a,b in zip(navs,navs[1:])]
check('log differences telescope within frozen tolerance',abs(sum(float(v) for v in logs)-math.log(1.2))<1e-12)
check('high-precision log matches independent math',abs(float(engine.log_ratio(F(2),F(3)))-math.log(2/3))<1e-12)
fails('nonpositive NAV rejected for logs',lambda:engine.log_ratio(0,1))
check('seeded compound uncertainty reproducible',engine.log_interval(logs)==engine.log_interval(logs))
check('positive constant block has positive endpoints',all(v>0 for v in engine.log_interval([Decimal('.1')]*25)))
check('negative constant block retains negative endpoints',all(v<0 for v in engine.log_interval([Decimal('-.1')]*25)))
print(json.dumps(dict(checks=len(checks),passed=True,scope='actual artificial ledger/compound uncertainty only; zero market experiments')))
