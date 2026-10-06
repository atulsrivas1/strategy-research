"""Synthetic reference only; no source/market/production engine."""
from dataclasses import dataclass,field
from math import isfinite

def available(completed_ns,received_ns,cutoff_ns):
    return completed_ns is not None and received_ns is not None and completed_ns<cutoff_ns and received_ns<=cutoff_ns

def daily_mean(history,window):
    if len(history)<window:return None
    tail=history[-window:]
    if not all(isfinite(x) and x>0 for x in tail):return None
    return sum(tail)/window

def holding_window(sessions,signal,holding,split_end):
    if type(signal) is not int or type(holding) is not int or signal<0 or signal>=len(sessions) or holding<=0:return None
    future=sessions[signal+1:signal+1+holding]
    return future if len(future)==holding and future[-1]<=split_end else None

def valid_daily_bar(bar):
    fields=[bar.get(k) for k in ['Open','High','Low','Close']]
    if any(x is None or not isfinite(x) or x<=0 for x in fields):return False
    o,h,l,c=fields
    return l<=o<=h and l<=c<=h

@dataclass
class Account:
    cash:int
    reservations:dict=field(default_factory=dict)
    positions:dict=field(default_factory=dict)
    def reserve(self,key,qty,price,fee):
        if key in self.reservations or key in self.positions:raise ValueError('duplicate')
        if qty<=0 or price<=0 or fee<0 or not all(type(v) is int for v in [qty,price,fee]):raise ValueError('units')
        cost=qty*price+fee
        if cost>self.cash-sum(self.reservations.values()):raise ValueError('insufficient')
        self.reservations[key]=cost
    def fail(self,key):self.reservations.pop(key)
    def fill(self,key,qty,price,fee):
        if qty<=0 or price<=0 or fee<0 or not all(type(v) is int for v in [qty,price,fee]):raise ValueError('units')
        if key in self.positions or self.reservations.get(key)!=qty*price+fee:raise ValueError('reservation mismatch')
        self.cash-=self.reservations.pop(key);self.positions[key]=qty
    def sell(self,key,price,fee):
        if price<=0 or fee<0 or type(price) is not int or type(fee) is not int:raise ValueError('units')
        self.cash+=self.positions.pop(key)*price-fee
    def split(self,key,new_per_old):
        if type(new_per_old) is not int or new_per_old<=0:raise ValueError('unsupported fractional split')
        self.positions[key]*=new_per_old
    def dividend(self,key,cents_per_share):
        if type(cents_per_share) is not int or cents_per_share<0:raise ValueError('units')
        self.cash+=self.positions[key]*cents_per_share
    def equity(self,marks):
        if any(k not in marks or type(marks[k]) is not int or marks[k]<=0 for k in self.positions):return None
        return self.cash+sum(q*marks[k] for k,q in self.positions.items())
