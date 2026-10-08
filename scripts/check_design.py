"""Independent hand-expected toy fixtures and source/requirement reconciliation.

No market loader, outcomes, data lake or production engine is used.
"""
from pathlib import Path
from decimal import Decimal as Q
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'docs/design'
matrix=json.loads((D/'APPLICABILITY.json').read_text())
requirements=json.loads((D/'REQUIREMENTS.json').read_text())['requirements']
req={r['id']:r for r in requirements}
assert len(req)==len(requirements)==24
assert set(req)=={f'R{n:02}' for n in range(1,25)}
for r in requirements:
    assert all(r[k] for k in ('need','existing_evidence','feasibility','owner_story','acceptance'))
    assert (ROOT/f"docs/stories/{r['owner_story']}_PLAN.md").is_file()
families=matrix['families']
assert len(families)==40 and {f['story'] for f in families}=={f'SR-{n:03}' for n in range(28,68)}
assert sum(f['release']=='M7' for f in families)==10 and sum(f['release']=='M4' for f in families)==30
actual={}
for f in families:
    assert set(f['required_contracts'])<=set(req) and 'R03' in f['required_contracts'] and 'R12' in f['required_contracts']
    assert f['next_qualification'] and f['blocker'] and f['canonical_family_scope']
    story=(ROOT/f"docs/stories/{f['story']}_PLAN.md").read_text()
    assert f"Release plan: [{f['release']}]" in story
    for v in f['versions']:
        path=D/v['path'];rel=path.resolve().relative_to(ROOT.resolve()).as_posix()
        assert rel not in actual
        assert hashlib.sha256(path.read_bytes()).hexdigest()==v['sha256']
        assert '../'+rel.removeprefix('docs/') in story,(f['story'],rel)
        text=path.read_text(encoding='utf-8')
        assert re.search(r'^## '+v['canonical_section']+r'[. ]',text,re.M)
        assert v['evidence_grade'] and v['adaptation_boundary']
        actual[rel]=f['story']
# Independently enumerate manifest dossier identities and existing canonical mappings.
expected={}
for lib in ['strategy-library','strategy-library-v2','strategy-library-v3','sigmatiq-strategy-library-v1']:
    folder=ROOT/'docs'/lib
    if (folder/'MAPPING.json').is_file():
        for r in json.loads((folder/'MAPPING.json').read_text()):expected[f"docs/{lib}/{r['file']}"]=r['story']
    else:
        for r in json.loads((folder/'MANIFEST.json').read_text()):
            name=Path(r['file']).name
            if lib=='strategy-library' and re.match('[A-E][1-4]-',name):
                code=name[:2];n=28+'ABCDE'.index(code[0])*4+int(code[1])-1
                expected[f"docs/{lib}/{r['file']}"]=f'SR-{n:03}'
            elif lib=='strategy-library-v3' and re.match(r'\d{2}-',name):expected[f"docs/{lib}/{r['file']}"]=f'SR-{47+int(name[:2]):03}'
assert actual==expected and len(actual)==76

def breakout(prior,close):
    if len(prior)!=20 or any(x is None for x in prior):return 'blocked_warmup'
    return 'admit' if close>max(prior) else 'reject'
history=list(range(1,21));signal_high=999;future_high=9999
assert breakout(history,21)=='admit'
assert breakout(history,20)=='reject'
assert breakout(history[:19],21)=='blocked_warmup'
assert breakout(history[:-1]+[None],21)=='blocked_warmup'
# Exclude signal/current and all future observations before applying rule.
combined=history+[signal_high,future_high]
assert breakout(combined[:20],21)==breakout(history,21)=='admit'
combined[21]=-9999
assert breakout(combined[:20],21)=='admit'
def admission(available,decision,age,max_age):
    return available is not None and available<=decision and age is not None and age<=max_age
assert admission(10,10,0,1)
assert not admission(11,10,0,1) and not admission(None,10,0,1)
assert not admission(9,10,2,1)
formation={'A':(100,110),'B':(100,105),'C':(100,99)}
ranking=sorted(formation,key=lambda s:Q(formation[s][1])/Q(formation[s][0])-1,reverse=True)
assert ranking==['A','B','C']
future={'A':1,'B':9999,'C':999999}
assert sorted(formation,key=lambda s:Q(formation[s][1])/Q(formation[s][0])-1,reverse=True)==ranking
weights={k:Q(v) for k,v in [('A','.5'),('B','.3'),('C','.2')]}
returns={k:Q(v) for k,v in [('A','.10'),('B','-.05'),('C','.02')]}
cost=Q('.001')
scanner=sum(weights[k]*(returns[k]-cost) for k in weights)
candidate=sum(weights[k]*(returns[k]-cost) for k in ['A'])
cash=sum(weights[k] for k in ['B','C'])
avoided=sum(-weights[k]*(returns[k]-cost) for k in ['B'])
sacrificed=sum(weights[k]*(returns[k]-cost) for k in ['C'])
assert scanner==Q('.0380') and candidate==Q('.0495') and cash==Q('.5')
assert avoided==Q('.0153') and sacrificed==Q('.0038')
assert candidate-scanner==Q('.0115')==avoided-sacrificed
assert candidate!=Q('.099') and sum(weights.values())==1
observed={'A':Q('.10'),'B':None,'C':Q('.02')}
known=sum(weights[k]*(r-cost) for k,r in observed.items() if r is not None)
censored=sum(weights[k] for k,r in observed.items() if r is None)
assert known==Q('.0533') and censored==Q('.3')
# A partially known subtotal is deliberately NOT a total strategy return.
total=None if censored else known
assert total is None
deferred=next(f for f in families if f['story']=='SR-028')
def admit_deferred(scope_amendment,order_evidence):return scope_amendment and order_evidence
assert deferred['disposition']=='deferred_scope' and 'R19' in deferred['required_contracts']
assert not admit_deferred(False,True) and not admit_deferred(True,False)
print(json.dumps({'families':40,'source_versions':76,'requirements':24,'independent_toy_cases':'D1, D2, deferred market making; boundaries, missingness and exact decimal arithmetic passed','historical_comparisons':0,'final_evaluations':0,'scope':'design verification only; not production-engine or market-data qualification'}))
