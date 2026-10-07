"""Separate saved-output arithmetic verifier, no foundation/check imports."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];j=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'));checks=[]
def require(name,ok):checks.append({'name':name,'passed':bool(ok)})
for name,digest in j['source_hashes'].items():require('hash_'+name,hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest)
require('all_cases_pass',len(j['checks'])==68 and all(c['passed'] for c in j['checks']))
r=j['outputs']['matched'];frac=lambda x:Fraction(str(x))
require('original_weights_handderived',[frac(x) for x in r['weights']]==[Fraction(1,2),Fraction(1,3),Fraction(1,6)])
require('original_weights_conserve',sum(frac(x) for x in r['weights'])==1)
require('retained_no_rescale',[frac(x) for x in r['retained']]==[0,Fraction(1,3),0])
require('retained_plus_cash',sum(frac(x) for x in r['retained'])+frac(r['cash'])==1)
# Hand arithmetic: -.0105+.003+.0031666667=-.0043333333; overlay .003.
require('scanner_handderived',frac(r['scanner'])==Fraction(-13,3000))
require('candidate_handderived',frac(r['candidate'])==Fraction(3,1000))
require('increment_handderived',frac(r['incremental'])==Fraction(11,1500))
require('avoided_loss',frac(r['avoided_losses'])==Fraction(21,2000))
require('sacrificed_winner',frac(r['sacrificed_winners'])==Fraction(19,6000))
require('stress_handderived',frac(j['outputs']['stressed']['incremental'])==Fraction(7,1000))
require('stress_cash_not_charged',frac(j['outputs']['stressed']['differential_cost'])==Fraction(1,3000))
c=j['outputs']['censored'];require('censored_denominator_preserved',c['opportunities']==3 and c['censored']==[0])
require('unknown_not_zero',c['scanner'] is None and c['incremental'] is None)
named={c['name']:c['actual'] for c in j['checks']}
# Account: 1000 -402 -201 +2 +438 +189 =1026.
require('account_cash_handderived',Decimal(named['final_cash'])==Decimal(1026))
require('split_dividend_handderived',Decimal(named['split_dividend_equity'])==Decimal(999))
require('overlap_equity_handderived',Decimal(named['overlap_equity_net_fees'])==Decimal(997))
require('no_marks_unknown',named['unmarked_position_unknown'] is None)
require('final_io_count',named['guard_before_io']==0)
require('scope_no_market',j['market_replays']==0)
# No output artifacts retained in public checkout.
print(json.dumps({'checks':len(checks),'failures':[c['name'] for c in checks if not c['passed']]}));assert all(c['passed'] for c in checks)
