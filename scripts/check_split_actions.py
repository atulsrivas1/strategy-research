"""Independent causal split and share/cash conservation witnesses; artificial."""
from pathlib import Path
from fractions import Fraction as F
from datetime import date,timedelta
import sys,copy
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import split_actions as actions
import funded_split_ledger as ledger
import funded_ledger as old_ledger
import d2_funded_v3 as engine
import d2_funded_v2 as old_engine

checks=[]
def check(name,value):assert value,name;checks.append(name)
def rejects(name,function):
    try:function()
    except (ValueError,KeyError):checks.append(name);return
    raise AssertionError(name)
def event(**kwargs):
    row=dict(id='S1',instrument_id=1,symbol='AAA',kind='split',ratio='10',cashflow='0',publication_date='2024-01-01',effective_date='2024-01-03',available_at='2024-01-01T23:59:59Z',source='artificial',clock_assumption='artificial modeled day start',input_basis='raw_share_units');row.update(kwargs);return row
names={1:'AAA',2:'BBB'};ev=actions.normalize([event()],names)
check('ten-for-one historical share normalization',actions.price('1000',ev,1,'2024-01-02','2024-01-03','2024-01-03T23:59:59Z')==100)
check('post-split row unchanged',actions.price('100',ev,1,'2024-01-03','2024-01-03','2024-01-03T23:59:59Z')==100)
check('future effective announcement does not alter past',actions.price('1000',ev,1,'2024-01-01','2024-01-02','2024-01-02T23:59:59Z')==1000)
check('other actual identity unchanged',actions.price('1000',ev,2,'2024-01-02','2024-01-03','2024-01-03T23:59:59Z')==1000)
reverse=actions.normalize([event(ratio='1/5')],names)
check('reverse split exact share basis',actions.price('20',reverse,1,'2024-01-02','2024-01-03','2024-01-03T23:59:59Z')==100)
multiple=actions.normalize([event(),event(id='S2',ratio='1/5',effective_date='2024-01-04')],names)
check('multiple splits compose in correct units',actions.factor(multiple,1,'2024-01-02','2024-01-04','2024-01-04T23:59:59Z')==2)
for field,value in [('available_at',None),('ratio',None),('available_at','2024-01-05T00:00:00Z')]:
    unknown=actions.normalize([event(**{field:value})],names)
    check('unknown/late effective event '+str(field)+str(value),actions.price('1000',unknown,1,'2024-01-02','2024-01-03','2024-01-03T23:59:59Z') is None)
for kwargs in [dict(ratio=10.),dict(ratio=True),dict(ratio='0'),dict(ratio='-1'),dict(ratio='1'),dict(instrument_id=True),dict(instrument_id=99),dict(symbol='BBB'),dict(input_basis='already_adjusted'),dict(kind='cash_dividend'),dict(cashflow='1'),dict(available_at='2023-12-31T00:00:00Z'),dict(available_at='2024-01-01T00:00:00'),dict(source='')]:
    rejects('reject invalid event '+str(kwargs),lambda:actions.normalize([event(**kwargs)],names))
rejects('duplicate/conflicting events',lambda:actions.normalize([event(),event(id='S2')],names))
rejects('future price row',lambda:actions.price('100',ev,1,'2024-01-04','2024-01-03','2024-01-03T23:59:59Z'))
rejects('decision clock before date',lambda:actions.price('100',ev,1,'2024-01-01','2024-01-03','2024-01-02T23:59:59Z'))
rejects('lossy raw price',lambda:actions.price(100.,ev,1,'2024-01-02','2024-01-03','2024-01-03T23:59:59Z'))
cal=['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05']
order=dict(id='L1',security=1,day=cal[0],decision=0,entry=1,exit=3,notional='1000')
opens={(i,1):'1000' if i<2 else '100' for i in range(5)};marks=dict(opens)
result=ledger.simulate(cal,[order],opens,opens,marks,'1100','0.001',events=ev)
check('same capital conserved through split net only fees',result['daily'][-1]['nav']==1098 and result['complete'] and result['lots'][0]['quantity']==10)
check('exact event-session mark no phantom loss',result['daily'][1]['gross']==result['daily'][2]['gross']==1000)
check('pure split cashflow zero',result['actions'][0]['cashflow']==0 and result['actions'][0]['before']==1 and result['actions'][0]['after']==10)
check('cash plus marked gross and fee conservation',all(row['cash']+row['gross']==row['nav'] and row['cash']>=0 for row in result['daily']))
exit_at_split=ledger.simulate(cal,[dict(order,exit=2)],opens,opens,marks,'1100','0',events=ev)
check('split before modeled open exit',exit_at_split['daily'][-1]['nav']==1100 and exit_at_split['lots'][0]['proceeds']==1000)
entry_at_split=ledger.simulate(cal,[dict(order,entry=2)],opens,opens,marks,'1100','0',events=ev)
check('post-split entry not multiplied twice',entry_at_split['lots'][0]['quantity']==10 and entry_at_split['actions']==[])
reverse_opens={(i,1):'20' if i<2 else '100' for i in range(5)}
reverse_result=ledger.simulate(cal,[dict(order,notional='100')],reverse_opens,reverse_opens,reverse_opens,'110','0',events=reverse)
check('reverse split share/value conservation',reverse_result['lots'][0]['quantity']==1 and reverse_result['daily'][-1]['nav']==110)
late=actions.normalize([event(available_at='2024-01-03T23:59:59Z')],names)
late_result=ledger.simulate(cal,[order],opens,opens,marks,'1100','0',events=late)
check('unknown at open does not use later knowledge',not late_result['complete'] and late_result['daily'][2]['nav'] is None and late_result['lots'][0]['state']=='unresolved_action')
missing=dict(opens);missing.pop((2,1))
censored=ledger.simulate(cal,[dict(order,exit=2)],opens,missing,marks,'1100','0',events=ev)
check('split applies to missing/censored exit without fabrication',not censored['complete'] and censored['lots'][0]['state']=='censored' and censored['lots'][0]['quantity']==10)
pair=ledger.paired(cal,[order],opens,opens,marks,'1100','0.001',['L1'],ev)
check('matched veto remains cash no reinvestment',pair['isolated_overlay_comparable'] and pair['candidate']['daily'][-1]['nav']==1100)
plain=ledger.simulate(cal,[order],opens,opens,marks,'1100','0.001')
old=old_ledger.simulate(cal,[order],opens,opens,marks,'1100','0.001')
check('no-event old ledger arithmetic unchanged',all(plain[key]==old[key] for key in ('daily','orders','lots','complete','funding_feasible')))
p=engine.protocol();oldp=old_engine.protocol()
check('strategic rules not retuned',{k for k in oldp if oldp[k]!=p[k]}=={'version','price_basis'} and set(p)-set(oldp)=={'action_basis','experiment_id'})
calendar=[(date(2023,1,1)+timedelta(days=i)).isoformat() for i in range(270)]
rows={(s,d):dict(instrument_id=s,symbol=str(s),date=d,close=str(F(100+s)+F(i*s,100)),available_at=None) for s in range(1,19) for i,d in enumerate(calendar)}
split_day=calendar[250];d=calendar[252]
for i,day in enumerate(calendar):rows[1,day]['close']='1000' if i<250 else '100'
e=actions.normalize([event(effective_date=split_day,publication_date=calendar[1],available_at=calendar[2]+'T00:00:00Z')],names)
rank=engine.select(rows,calendar,252,list(range(1,19)),e)
check('formation and context split neutral, no phantom loss',F(rank['scores']['1'])==0 and rank['stock'][1]=='neutral')
unresolved=actions.normalize([event(effective_date=split_day,publication_date=calendar[1],available_at=None)],names)
check('known unknown action ranking unresolved',engine.select(rows,calendar,252,list(range(1,19)),unresolved)['status']=='unresolved')
print({'checks':len(checks),'passed':True,'scope':'artificial causal/action/funding witnesses; no market run'})
