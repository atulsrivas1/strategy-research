"""Synthetic-only foundations; no source loader or broker capability."""
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction

@dataclass(frozen=True)
class Field:
    value: Decimal | None
    session: str
    observed: int | None
    known: int | None
    completed: int
    qualified: bool

def available(field, expected, decision, max_age):
    if not field.qualified:return 'unqualified_source'
    if field.value is None or not field.value.is_finite() or field.value<=0:return 'missing_or_invalid_value'
    if field.session!=expected:return 'wrong_session'
    if field.observed is None or field.known is None:return 'missing_clock'
    if field.observed>field.known:return 'clock_order'
    if field.completed>field.known:return 'not_finalized_when_known'
    if field.completed>decision or field.observed>decision:return 'future_observation'
    if field.known>decision:return 'late'
    if max_age<0 or decision-field.observed>max_age:return 'stale'
    return None

def classify_stock(close,low,current,prior,decision,max_age):
    reasons=[available(close,current,decision,max_age),available(low,prior,decision,max_age)]
    if any(reasons):return {'state':'unknown','reasons':[x for x in reasons if x]}
    return {'state':'aligned' if close.value>low.value else 'conflicting' if close.value<low.value else 'neutral','reasons':[]}

def classify_market(close,s50,s100,current,prior,decision,max_age):
    reasons=[available(f,s,decision,max_age) for f,s in ((close,current),(s50,prior),(s100,prior))]
    if any(reasons):return {'state':'unknown','reasons':[x for x in reasons if x]}
    a,b,c=close.value,s50.value,s100.value
    return {'state':'aligned' if a>b>c else 'conflicting' if a<b<c else 'neutral','reasons':[]}

def gate(stock,market):return stock['state'] in ('aligned','neutral') and market['state']=='aligned'

def asof(fields,decision):
    # A late revision cannot replace an earlier available observation.
    eligible=[f for f in fields if f.known is not None and f.observed is not None and f.known<=decision and f.observed<=decision]
    return max(eligible,key=lambda f:(f.observed,f.known),default=None)

def pullback(close,close2,s50,s100,liquidity):
    vals=(close,close2,s50,s100,liquidity)
    return all(v is not None and v.is_finite() and v>0 for v in vals) and close>=10 and liquidity>=50_000_000 and close>s50>s100 and close<close2

def rank_weights(returns):
    n=len(returns)
    if n<2 or any(x is None for x in returns):raise ValueError('fixed scanner needs full pretrade universe')
    weights=[]
    for r in returns:
        below=sum(x<r for x in returns);ties=sum(x==r for x in returns)
        rank=Fraction(2*below+ties+1,2)
        tilt=(n+1-2*rank)/(n-1)
        weights.append((1+Fraction(1,2)*tilt)/n)
    return tuple(weights)

def compare(weights,keep,net_returns,differential_cost=Fraction(0)):
    if not len(weights)==len(keep)==len(net_returns):raise ValueError('unaligned opportunities')
    if any(w<0 for w in weights) or sum(weights)>1:raise ValueError('invalid weights')
    if differential_cost<0:raise ValueError('negative candidate disadvantage')
    retained=tuple(w if k else Fraction(0) for w,k in zip(weights,keep))
    censored=[i for i,r in enumerate(net_returns) if r is None]
    # Never replace censored scanner returns with zero or remove entered rows.
    base=None if censored else sum(w*r for w,r in zip(weights,net_returns))
    candidate=None if any(net_returns[i] is None and keep[i] for i in range(len(keep))) else sum(w*r for w,r in zip(retained,net_returns) if w)
    extra_cost=sum(retained)*differential_cost
    if candidate is not None:candidate-=extra_cost
    avoided=sum(-w*r for w,k,r in zip(weights,keep,net_returns) if not k and r is not None and r<0)
    sacrificed=sum(w*r for w,k,r in zip(weights,keep,net_returns) if not k and r is not None and r>0)
    return {'weights':weights,'retained':retained,'cash':1-sum(retained),'scanner':base,'candidate':candidate,
      'incremental':None if base is None or candidate is None else candidate-base,
      'avoided_losses':avoided,'sacrificed_winners':sacrificed,'differential_cost':extra_cost,'censored':censored,'opportunities':len(weights)}

class SyntheticAccount:
    def __init__(self,cash):self.cash=Decimal(cash);self.reserved=Decimal(0);self.positions={}
    def reserve(self,amount):
        amount=Decimal(amount)
        if amount<0 or amount>self.cash-self.reserved:raise ValueError('reservation exceeds free cash')
        self.reserved+=amount
    def cancel(self,amount):
        amount=Decimal(amount)
        if amount<0 or amount>self.reserved:raise ValueError('invalid release')
        self.reserved-=amount
    def buy(self,symbol,quantity,price,fee,reservation):
        if type(quantity) is not int or quantity<=0:raise ValueError('integer positive quantity required')
        price,fee,reservation=map(Decimal,(price,fee,reservation));cost=quantity*price+fee
        if price<=0 or fee<0 or reservation>self.reserved or reservation<cost:raise ValueError('invalid reserved execution')
        self.reserved-=reservation;self.cash-=cost;self.positions[symbol]=self.positions.get(symbol,0)+quantity
    def dividend(self,symbol,per_share):
        per_share=Decimal(per_share)
        if per_share<0:raise ValueError('invalid dividend')
        self.cash+=self.positions.get(symbol,0)*per_share
    def split(self,symbol,ratio):
        q=Fraction(self.positions[symbol])*Fraction(ratio)
        if q.denominator!=1:raise ValueError('fractional action needs separate cash-in-lieu contract')
        self.positions[symbol]=q.numerator
    def sell(self,symbol,quantity,price,fee):
        if type(quantity) is not int or quantity<=0 or quantity>self.positions.get(symbol,0):raise ValueError('invalid sale')
        price,fee=map(Decimal,(price,fee))
        if price<=0 or fee<0:raise ValueError('invalid execution')
        self.positions[symbol]-=quantity;self.cash+=quantity*price-fee
    def equity(self,marks):
        if any(s not in marks or marks[s] is None for s,q in self.positions.items() if q):return None
        return self.cash+sum(q*Decimal(marks[s]) for s,q in self.positions.items() if q)
