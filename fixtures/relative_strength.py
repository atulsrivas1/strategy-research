"""Complete-denominator ranking ingredients; no market reader or trading evaluator."""
from decimal import Decimal, InvalidOperation


def rank_cohort(rows, eligible_ids, formation_start, formation_end, decision_at, authority):
    required={'universe','prices','actions','calendar','historical_availability'}
    if set(authority)!=required or any(authority[k]!='qualified' for k in required):
        return {'status':'blocked','reason':'authority'}
    if (any(type(v) is not int for v in [formation_start,formation_end,decision_at])
            or not 0<=formation_start<formation_end<decision_at):
        return {'status':'blocked','reason':'formation clocks'}
    if (not eligible_ids or any(not isinstance(i,str) or not i for i in eligible_ids)
            or len(eligible_ids)!=len(set(eligible_ids))):
        return {'status':'blocked','reason':'cohort'}
    observed={};problems=[]
    for r in rows:
        if not isinstance(r,dict) or not isinstance(r.get('security_id'),str):
            problems.append('invalid identity row');continue
        sid=r.get('security_id')
        if sid in observed or sid not in eligible_ids:
            problems.append('duplicate or unexpected identity');continue
        observed[sid]=r
    missing=sorted(set(eligible_ids)-set(observed))
    if missing or problems:
        return {'status':'blocked','reason':'denominator','expected':len(eligible_ids),'observed_unique':len(observed),'missing':missing,'problems':problems}
    scores={}
    for sid,r in observed.items():
        try:
            if (type(r['start_at']) is not int or type(r['end_at']) is not int
                    or r['start_at']!=formation_start or r['end_at']!=formation_end
                    or r['clock_kind'] not in {'observed','qualified_historical'}
                    or type(r['available_at']) is not int or not formation_end<=r['available_at']<=decision_at
                    or not r['source_id'] or r['price_basis']!='qualified_split_basis'):
                raise ValueError('Endpoint provenance/clock')
            if isinstance(r['start_price'],bool) or isinstance(r['end_price'],bool):
                raise ValueError('Price')
            start,end=Decimal(str(r['start_price'])),Decimal(str(r['end_price']))
            if not start.is_finite() or not end.is_finite() or min(start,end)<=0:
                raise ValueError('Price')
            scores[sid]=end/start-1
        except (KeyError,ValueError,TypeError,InvalidOperation) as e:
            problems.append({'security_id':sid,'reason':str(e)})
    if problems:
        return {'status':'blocked','reason':'invalid cohort member','expected':len(eligible_ids),'valid':len(scores),'problems':problems}
    ranked=[{'security_id':sid,'score':str(score),'rank':1+sum(s>score for s in scores.values())}
            for sid,score in sorted(scores.items(),key=lambda p:(-p[1],p[0]))]
    return {'status':'complete ranking ingredient','expected':len(eligible_ids),'valid':len(scores),
            'score_kind':'split-adjusted endpoint price return; dividend return not included',
            'ranked':ranked,'empirical_admission':False}


def select_top_k(ranking,k):
    if ranking.get('status')!='complete ranking ingredient' or type(k) is not int or not 1<=k<=len(ranking['ranked']):
        return {'status':'blocked','reason':'selection contract'}
    rows=ranking['ranked']
    if k<len(rows) and Decimal(rows[k-1]['score'])==Decimal(rows[k]['score']):
        return {'status':'blocked','reason':'tie at boundary'}
    return {'status':'synthetic selection ingredient','security_ids':[r['security_id'] for r in rows[:k]],'empirical_admission':False}
