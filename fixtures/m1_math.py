"""Sanitized numerical methodology witness, exact bodies from the frozen private runner.
Synthetic inputs only in public checks; no private data loader or market replication.
"""
from fractions import Fraction
def weights(returns):
    n=len(returns)
    if n<2:return {},{}
    ranks={s:Fraction(1+sum(r<value for r in returns.values()))+Fraction(sum(r==value for r in returns.values())-1,2) for s,value in returns.items()}
    w={s:float((1+Fraction(1,2)*Fraction(n+1-2*q,n-1))/n) for s,q in ranks.items()}
    b={s:1/n for s in returns}
    assert abs(sum(w.values())-1)<1e-12 and all(.5/n-1e-12<=v<=1.5/n+1e-12 for v in w.values())
    return w,b

def net(ratio,c):return ratio-1-c-c*ratio

def marked_value(ratios,weights_,cost,exited):return sum(weights_[s]*(ratio-1-cost-(cost*ratio if exited else 0)) for s,ratio in ratios.items())
