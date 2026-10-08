"""Synthetic matched elapsed-window volume; no canonical EP rule or feed authority."""
from decimal import Decimal,DecimalException,Context,localcontext

def window_volume(current, references, declared_sessions, decision, authority):
    required={'source','calendar','sessions','actions','window','historical_availability'}
    if (not isinstance(authority,dict) or set(authority)!=required
            or any(authority[k]!='qualified' for k in required)):
        return {'status':'blocked','reason':'authority'}
    try:
        if (type(decision) is not int or not isinstance(references,list)
                or not isinstance(declared_sessions,list) or len(declared_sessions)!=2
                or any(not isinstance(s,str) or not s for s in declared_sessions)
                or len(set(declared_sessions))!=2
                or len(references)!=2 or {r['session'] for r in references}!=set(declared_sessions)
                or current['session'] in declared_sessions):raise ValueError('complete reference set')
        seen=set();volumes=[]
        with localcontext(Context(prec=50)):
            for row in [current]+references:
                if (any(not isinstance(row[k],str) or not row[k] for k in ['source_id','session','security_id','basis'])
                        or row['security_id']!=current['security_id'] or row['basis']!='action_normalized_shares'
                        or row['source_id'] in seen or row['complete'] is not True
                        or row['clock_kind'] not in {'observed','qualified_historical'}
                        or any(type(row[k]) is not int for k in ['start','end','available','offset','duration'])
                        or not row['start']<row['end']<=row['available']<=decision
                        or row['offset']!=0 or row['duration']!=30 or row['end']-row['start']!=30
                        or isinstance(row['volume'],bool)):raise ValueError('window contract')
                v=Decimal(str(row['volume']))
                if not v.is_finite() or v<0:raise ValueError('volume')
                volumes.append(v);seen.add(row['source_id'])
            if any(r['end']>=current['start'] for r in references):raise ValueError('reference chronology')
            intervals=sorted((r['start'],r['end']) for r in references)
            if intervals[0][1]>intervals[1][0]:raise ValueError('overlapping references')
            mean=(volumes[1]+volumes[2])/2
            if mean<=0:raise ValueError('denominator')
            ratio=volumes[0]/mean
        return {'status':'matched-window volume ingredient','mean_reference_volume':str(mean),
                'ratio':str(ratio),'empirical_admission':False}
    except (KeyError,TypeError,ValueError,DecimalException):
        return {'status':'blocked','reason':'matched-window contract'}
