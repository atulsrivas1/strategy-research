"""Independent rational arithmetic and causal guard checks, no market reader."""
from pathlib import Path
from copy import deepcopy
from decimal import Decimal, localcontext
from fractions import Fraction
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from fixtures.rsi2 import seeded_rsi2

authority={k:'qualified' for k in ['prices','actions','calendar','historical_availability','initialization']}
def rows(values):
    return [dict(session_id=i,security_id='toy',source_id='toy-source',price_basis='qualified_split_basis',
                 clock_kind='observed',close_at=10*i,available_at=10*i+1,close=str(v))
            for i,v in enumerate(values,1)]
base=rows([100,102,101,100,101]);sessions=[1,2,3,4,5]
def run(data=None, expected=None, start=1, decision=100, auth=authority):
    return seeded_rsi2(base if data is None else data, sessions if expected is None else expected,
                       start,decision,'toy','toy-source',auth)
checks=0
def check(value):
    global checks
    assert value
    checks+=1
r=run()
# Independently reduced fractions: seed gain1/loss1/2; next1/2,3/4; next3/4,3/8.
for item,expected in zip(r['series'],[Fraction(200,3),Fraction(40),Fraction(200,3)]):
    check(abs(Fraction(item['rsi'])-expected)<Fraction(1,10**45))
check(run(base[:3],[1,2,3])['series']==r['series'][:1])
check(run(base[:4],[1,2,3,4])['series']==r['series'][:2])
check(run(rows([100,101,102]),[1,2,3])['series'][0]['rsi']=='100')
check(run(rows([102,101,100]),[1,2,3])['series'][0]['rsi']=='0')
check(run(rows([100,100,100]),[1,2,3])['series'][0]['rsi'] is None)
check(run(rows([100,102,101,101]),[1,2,3,4])['series'][1]['rsi']==r['series'][0]['rsi'])
check(not r['provider_parity'] and not r['empirical_admission'])
with localcontext() as c:
    c.prec=3
    check(run()==r)
    check(c.prec==3)
check(run(base[:2],[1,2])['status']=='blocked')
check(run(base[:-1])['status']=='blocked')
check(run(list(reversed(base)))['status']=='blocked')
check(run(expected=[1,2,3,4,4])['status']=='blocked')
check(run(expected=[1,2,3,4,6])['status']=='blocked')
check(run(expected=[1,2,True,4,5])['status']=='blocked')
check(run(start=2)['status']=='blocked')
check(run(start=True)['status']=='blocked')
check(run(decision=51)['status']=='blocked')
check(run(decision=True)['status']=='blocked')
for key,value in [('security_id','other'),('source_id','other'),('session_id',True),
                  ('price_basis','unknown'),('clock_kind','reconstructed'),('available_at',100),
                  ('available_at',1),('close_at',True),('close_at',10),('close',0),
                  ('close',-1),('close',True),('close','NaN'),('close','Infinity')]:
    bad=deepcopy(base);bad[2][key]=value
    check(run(bad)['status']=='blocked')
for key in base[2]:
    bad=deepcopy(base);del bad[2][key]
    check(run(bad)['status']=='blocked')
for key in authority:
    check(run(auth=dict(authority,**{key:'unknown'}))['status']=='blocked')
check(run(auth={})['status']=='blocked')
check(run(base+[dict(base[-1],session_id=6,close_at=110,available_at=111)],sessions+[6])['status']=='blocked')
check(run([None]*5)['status']=='blocked')
check(run(rows([100,'1e1000000',100]),[1,2,3])['status']=='blocked')
print(f'{checks} hand-derived rational RSI/causal checks passed; empirical admission false')
