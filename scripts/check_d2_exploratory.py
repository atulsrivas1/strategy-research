from pathlib import Path
import sys,unittest,copy
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import d2_exploratory as d

class Checks(unittest.TestCase):
    def setUp(self):
        self.cal=[f'{i:02}' for i in range(30)];self.symbols=['A','B','C','D']
        self.bars={(s,day):dict(open=100,close=100) for s in self.symbols for day in self.cal}
        for s,p in zip(self.symbols,[120,110,105,90]):self.bars[(s,'20')]['close']=p
    def test_ranking_and_complete_denominator(self):
        r=d.choose(self.bars,self.cal,'20',self.symbols)
        self.assertEqual(r['selected'],['A','B','C']);self.assertEqual(r['scores']['A'],'0.2')
        self.assertEqual(d.choose(self.bars,self.cal,'20',self.symbols[::-1])['selected'],r['selected'])
        del self.bars[('D','00')];self.assertEqual(d.choose(self.bars,self.cal,'20',self.symbols)['status'],'unresolved')
    def test_tie_and_duplicate_block(self):
        self.bars[('D','20')]['close']=105
        self.assertEqual(d.choose(self.bars,self.cal,'20',self.symbols)['reason'],'boundary tie')
        self.assertEqual(d.choose(self.bars,self.cal,'20',['A','A','C','D'])['status'],'unresolved')
    def test_context_states(self):
        self.assertEqual(d.context(self.bars,self.cal,'20','A'),'aligned')
        self.assertEqual(d.context(self.bars,self.cal,'20','D'),'conflicting')
        self.bars[('A','20')]['close']=100;self.assertEqual(d.context(self.bars,self.cal,'20','A'),'neutral')
        del self.bars[('A','15')];self.assertEqual(d.context(self.bars,self.cal,'20','A'),'unknown')
    def test_timing_weights_fees_and_future_invariance(self):
        r=d.evaluate(self.bars,self.cal,['20'],self.symbols)
        self.assertEqual(r['events'][0]['entry_day'],'22');self.assertEqual(r['events'][0]['exit_day'],'27')
        self.assertAlmostEqual(sum(e['weight'] for e in r['events']),.2)
        self.assertAlmostEqual(sum(e['weight'] for e in r['benchmark_events']),.2)
        self.assertAlmostEqual(r['costs'][0]['baseline_contribution'],-.0004)
        self.assertAlmostEqual(r['secondary']['paired_delta'],0)
        future=copy.deepcopy(self.bars);future[('D','25')]['close']=999999
        self.assertEqual(d.choose(future,self.cal,'20',self.symbols),d.choose(self.bars,self.cal,'20',self.symbols))
    def test_veto_cash_counts_and_censoring(self):
        self.bars[('C','15')]['close']=110
        self.bars[('C','27')]['open']=90
        r=d.evaluate(self.bars,self.cal,['20'],self.symbols)
        self.assertEqual(r['costs'][0]['avoided_losses'],1);self.assertEqual(r['costs'][0]['sacrificed_winners'],0)
        self.assertAlmostEqual(r['candidate_proxy']['curve'][-1]-1,r['costs'][0]['candidate_contribution'])
        self.assertEqual(r['states']['market']['unknown'],3)
        del self.bars[('C','27')];self.assertEqual(d.evaluate(self.bars,self.cal,['20'],self.symbols)['verdict'],'inconclusive')

if __name__=='__main__':unittest.main()
