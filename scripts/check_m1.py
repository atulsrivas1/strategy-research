"""Public synthetic methodology checks, no private data or third-party dependencies."""
from pathlib import Path
from fractions import Fraction
import importlib.util,json,math
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('m1_math',ROOT/'fixtures/m1_math.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks={}
def check(name,ok):checks[name]=bool(ok);assert ok,name
w,b=m.weights({'loser':Fraction(-1,10),'winner':Fraction(1,10)})
check('two_name_capped_tilt',w=={'loser':.75,'winner':.25} and b=={'loser':.5,'winner':.5})
w,b=m.weights({'a':Fraction(0),'b':Fraction(0),'c':Fraction(0)})
check('all_ties_equal',w==b)
w,b=m.weights({'a':Fraction(-1,10),'b':Fraction(-1,10),'c':Fraction(1,10)})
check('partial_tie_average_rank',abs(w['a']-5/12)<1e-12 and abs(w['b']-5/12)<1e-12 and abs(w['c']-1/6)<1e-12)
check('same_total_exposure',abs(sum(w.values())-sum(b.values()))<1e-12)
check('one_name_no_opportunity',m.weights({'a':Fraction(0)})==({},{}))
check('exact_exit_proceeds_fee',abs(m.net(1.1,.0005)-.09895)<1e-12)
check('negative_return_cost',abs(m.net(.9,.0005)+.10095)<1e-12)
w,b=m.weights({'loser':Fraction(-1,10),'winner':Fraction(1,10)})
check('entry_mark_fee_only',abs(m.marked_value({'loser':1.,'winner':1.},w,.001,False)+.001)<1e-12)
check('exit_cash_reconciles',abs(m.marked_value({'loser':1.1,'winner':.9},w,.001,True)-.04795)<1e-12)
for file in ['reports/M1-development.md','reports/M1-methodology.md','reports/M1-feasibility.md']:
    check(file+'_exists',(ROOT/file).is_file())
report=(ROOT/'reports/M1-development.md').read_text(encoding='utf-8')
check('scoped_inconclusive','inconclusive' in report and 'not independent human' in report and 'no M1 release/Done' in report)
print(json.dumps({'passed':True,'checks':len(checks),'scope':'synthetic methodology witnesses and document assertions only; no market replay or hosted reviewer'},indent=2))
