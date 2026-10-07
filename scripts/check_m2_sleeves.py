from pathlib import Path
from fractions import Fraction as F
import sys,json
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'fixtures'))
from m2_sleeves import decision,simulate,fixture
checks=[]
def check(name,condition):
    checks.append({'name':name,'passed':bool(condition)})
    if not condition:raise AssertionError(name)
opens,close=fixture()
for scanner,base,candidate in [('pullback',F(4999,500),F(201979,20000)),('rank',F(201959,20000),F(405937,40000))]:
    d=[decision(t,scanner) for t in [0,1]]
    b=simulate(d,opens,close);c=simulate(d,opens,close,True)
    check(scanner+'_hand_terminal',b['daily'][-1]['cash']==base and c['daily'][-1]['cash']==candidate)
    check(scanner+'_next_fifth',[(s['entry'],s['exit']) for s in b['sleeves']]==[(1,5),(2,6)])
    check(scanner+'_overlap',[r['active_sleeves'] for r in b['daily']]==[0,1,2,2,2,1,0])
    check(scanner+'_cash_no_rescale',all(s['retained'][0]==s['original_weights'][0] and s['retained'][1]==0 for s in c['sleeves']))
    missing=[dict(x) for x in close];missing[3]['A']=None
    check(scanner+'_unknown_mark',simulate(d,opens,missing)['daily'][3]['equity'] is None)
    missing=[dict(x) for x in close];missing[5]['B']=None
    check(scanner+'_censored_exit',simulate(d,opens,missing)['sleeves'][0]['state']=='censored')
    no_open=dict(opens);no_open[(1,'A')]=None
    check(scanner+'_unfilled_preserved',simulate(d,no_open,close)['sleeves'][0]['state']=='unfilled')
    check(scanner+'_late_market',decision(0,scanner,True)['keep']==[False,False])
print(json.dumps({'checks':len(checks),'passed':True,'scope':'artificial method witness, no market replay/clock/fill qualification'}))
