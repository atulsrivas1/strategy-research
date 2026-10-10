"""Independent exact rational/hex witnesses; no market input."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal
import sys, math, struct
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import stored_prices as stored
import d2_funded as old
import d2_funded_v2 as new

def reject(function):
    try:function()
    except (ValueError,OverflowError):return
    raise AssertionError('expected rejection')

for value in (.1, .01, 101.123456789, math.nextafter(1.,2.), 1e-200, 1e200):
    text,hexadecimal=stored.encode(value)
    bits=struct.unpack('>Q',struct.pack('>d',value))[0]
    exp=(bits>>52)&2047; mantissa=(bits&((1<<52)-1))+(1<<52 if exp else 0)
    power=(exp-1023 if exp else -1022)-52
    rational=F(mantissa)*(F(2)**power)
    assert F(text)==rational and float.fromhex(hexadecimal)==value
    row={key:text for key in ('open','high','low','close')};row['stored_binary64']={key:hexadecimal for key in row}
    assert stored.verify([row])
    row['close']=str(Decimal(text)+Decimal('.0001'));reject(lambda:stored.verify([row]))
for value in (0., -1., float('inf'), float('nan'), True, 1, '1.0'):reject(lambda:stored.encode(value))
reject(lambda:stored.verify([dict(open='1',high='1',low='1',close='1')]))
assert new.interval([F(k-20,101+k*2) for k in range(1,40)])==old.interval([F(k-20,101+k*2) for k in range(1,40)])
before=old.protocol();after=new.protocol()
changed={key for key in before if before[key]!=after[key]}
assert changed=={'version','input_start','input_end','decision_start','decision_end'}
assert set(after)-set(before)=={'price_basis'}
print('Exact binary64 independent bit decomposition, mismatch rejection, unchanged strategic parameters and exact bootstrap parity pass')
