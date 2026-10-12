"""Independent enclosure witnesses, no market inputs or implementation-mirroring tests."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import sys,random
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from certified_mean import certified_mean
checks=0
def check(ok):
    global checks
    assert ok;checks+=1
fixtures=[[0],[F(1,3),F(2,7)],[F(-1,3),F(2,7)],[10**100,-10**100,F(1,97)],[F(1,10**120),F(-1,10**121)],[F(-7,10),F(9,10)]]
rng=random.Random(251011)
for n in (7,31,128,512):fixtures.append([F(rng.randrange(-10000,10001),rng.randrange(1,10000)) for _ in range(n)])
for xs in fixtures:
    r=certified_mean(xs);exact=sum(xs,F(0))/len(xs)
    check(r['lower']<=exact<=r['upper']);check(abs(r['midpoint']-exact)<=r['maximum_absolute_error']);check(r['upper']-r['lower']<=F(1,10**80))
check(certified_mean([F(1,4),F(3,4)])['maximum_absolute_error']==0)
big=[F(rng.getrandbits(64000),rng.getrandbits(64000)|1) for _ in range(512)]
r=certified_mean(big)
with localcontext() as ctx:
    ctx.prec=160
    independent=sum((Decimal(x.numerator)/Decimal(x.denominator) for x in big),Decimal(0))/512
    lo=Decimal(r['lower'].numerator)/Decimal(r['lower'].denominator);hi=Decimal(r['upper'].numerator)/Decimal(r['upper'].denominator)
    check(lo-Decimal('1e-140')<=independent<=hi+Decimal('1e-140'))
check(r['maximum_absolute_error']<=F(1,2*10**80))
for values,places in [([],80),([1]*513,80),([.1],80),([True],80),([None],80),([1],True),([1],0),([1],121)]:
    try:certified_mean(values,places)
    except ValueError:checks+=1
    else:raise AssertionError('bad input accepted')
print({'checks':checks,'passed':True,'large_terms':512,'large_term_bits':64000,'market_rows':0})
