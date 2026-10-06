"""Independent hand-derived synthetic reference checks; no market data."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'fixtures'))
from reference_machinery import available,daily_mean,holding_window,valid_daily_bar,Account

def main():
 checks=[]
 def check(n,v):checks.append({'name':n,'passed':bool(v)})
 def rejects(fn):
  try:fn()
  except (ValueError,KeyError):return True
  return False
 check('completed_received',available(1000,1001,1002) and not available(1002,1001,1002) and not available(1000,1003,1002))
 check('null_clock',not available(None,1001,1002) and not available(1000,None,1002))
 check('nanoseconds',1000001*1000==1000001000)
 check('warmup20',daily_mean([100.]*19,20) is None and daily_mean([100.]*20,20)==100.)
 check('warmup50_100',daily_mean([100.]*49,50) is None and daily_mean([100.]*99,100) is None)
 check('missing_warmup',daily_mean([100.]*19+[float('nan')],20) is None)
 ds=['01','02','03','04','05','06','07','08']
 check('next_fifth',holding_window(ds,1,5,'07')==['03','04','05','06','07'])
 check('boundary_purge',holding_window(ds,1,5,'06') is None and holding_window(ds,4,5,'08') is None)
 check('invalid_holding_request',holding_window(ds,-1,5,'08') is None and holding_window(ds,1,0,'08') is None)
 check('valid_ohlc',valid_daily_bar({'Open':100.,'High':105.,'Low':95.,'Close':102.}))
 check('inverted_ohlc',not valid_daily_bar({'Open':100.,'High':99.,'Low':101.,'Close':102.}))
 check('nonfinite_ohlc',not valid_daily_bar({'Open':100.,'High':105.,'Low':95.,'Close':float('nan')}))
 a=Account(100000);a.reserve('A',2,10000,100)
 check('reserve_cash',a.cash==100000 and a.reservations['A']==20100)
 check('duplicate_reservation',rejects(lambda:a.reserve('A',1,10000,100)))
 check('insufficient_overlap',rejects(lambda:a.reserve('B',8,10000,100)))
 a.reserve('B',1,10000,100);a.fail('B')
 check('failed_order_release',a.cash==100000 and 'B' not in a.reservations)
 check('integer_quantity',rejects(lambda:a.reserve('C',1.5,10000,100)))
 check('reservation_mismatch',rejects(lambda:a.fill('A',3,10000,100)))
 check('fractional_fill',rejects(lambda:a.fill('A',1.5,10000,100)))
 a.fill('A',2,10000,100)
 check('fill_cash',a.cash==79900 and a.positions=={'A':2} and not a.reservations)
 check('duplicate_position',rejects(lambda:a.reserve('A',1,10000,100)))
 check('unknown_mark',a.equity({'A':None}) is None)
 for label,mark in [('nan',float('nan')),('positive_infinity',float('inf')),('negative_infinity',float('-inf')),('zero',0),('negative',-10000),('fractional_cent',10000.5),('boolean',True),('string','10000'),('complex',complex(10000,0))]:
  check('invalid_mark_'+label,a.equity({'A':mark}) is None)
 check('mark_equity',a.equity({'A':11000})==101900)
 a.sell('A',11000,100);check('roundtrip_cash',a.cash==101800 and not a.positions)
 a=Account(100000);a.reserve('A',2,10000,0);a.fill('A',2,10000,0);a.dividend('A',100)
 check('dividend_cash',a.cash==80200)
 before=a.equity({'A':10000});a.split('A',2)
 check('split_conservation',a.positions['A']==4 and a.equity({'A':5000})==before==100200)
 out={'scope':'synthetic reference only; no production engine or market qualification','checks':checks,'passed':all(v['passed'] for v in checks)}
 print(json.dumps(out,indent=2));assert out['passed']
if __name__=='__main__':main()
