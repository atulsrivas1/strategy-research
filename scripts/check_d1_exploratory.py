from pathlib import Path
import sys,unittest,copy
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import d1_exploratory as d

class Checks(unittest.TestCase):
    def test_known_threshold_context_and_equality(self):
        h=[dict(high=x,close=x) for x in [1]*10+[3]*10]
        neutral=d.screen(h,dict(close=4));self.assertTrue(neutral['signal']);self.assertEqual(neutral['stock'],'neutral')
        self.assertEqual(neutral['threshold'],3);self.assertEqual(neutral['context_boundary'],4)
        self.assertEqual(d.screen(h,dict(close=4.5))['stock'],'conflicting')
        self.assertEqual(d.screen(h,dict(close=3.5))['stock'],'aligned')
        self.assertFalse(d.screen(h,dict(close=3))['signal'])
    def test_independent_fee_and_cash_veto(self):
        self.assertAlmostEqual(d.net_return(100,110,.001),.0979)
        e=[dict(day='D',entry=100,exit=110,weight=.1,veto=True,outcome='filled'),dict(day='D',entry=100,exit=90,weight=.1,veto=True,outcome='filled')]
        s=d.summarize(e,['D'],.001)
        self.assertAlmostEqual(s['baseline_contribution'],-.0004)
        self.assertAlmostEqual(s['paired_delta'],.0004);self.assertEqual(s['candidate_contribution'],0)
        self.assertEqual(s['avoided_losses'],1);self.assertEqual(s['sacrificed_winners'],1)
    def test_entry_delay_prefix_invariance_and_missing_outcome(self):
        cal=[f'{i:02}' for i in range(30)]
        bars={('X',day):dict(open=2,high=3,low=1,close=2) for day in cal}
        bars[('X','20')]['close']=4
        rows,events=d.opportunities(bars,cal,['20'],['X'])
        self.assertEqual(events[0]['entry_day'],'22');self.assertEqual(events[0]['exit_day'],'27')
        future=copy.deepcopy(bars);future[('X','25')]['close']=100000
        self.assertEqual(d.opportunities(future,cal,['20'],['X'])[0],rows)
        del bars[('X','27')]
        self.assertEqual(d.evaluate(bars,cal,['20'],['X'])['verdict'],'inconclusive')
    def test_proxy_terminal_conservation_and_overlap(self):
        cal=['A','B','C'];bars={('X',day):dict(close=x) for day,x in zip(cal,[100,105,110])}
        e=[dict(symbol='X',entry_day='A',exit_day='C',entry=100,exit=110,weight=.1,outcome='filled',veto=False)]
        p=d.proxy_path(e,bars,cal,.001)
        self.assertAlmostEqual(p['curve'][-1]-1,.00979)
        self.assertEqual(p['max_reference_exposure'],.1)
        self.assertAlmostEqual(p['turnover'],.21)
        e[0]['veto']=True;self.assertEqual(d.proxy_path(e,bars,cal,.001,True)['curve'],[1,1,1])
    def test_unknown_and_empty_support(self):
        self.assertIsNone(d.screen([None]*20,dict(close=1))['signal'])
        self.assertEqual(d.evaluate({},['D'],['D'],['X'])['verdict'],'inconclusive')
        self.assertEqual(d.bootstrap({'D':0}),[0,0])

if __name__=='__main__':unittest.main()
