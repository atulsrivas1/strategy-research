"""Three preregistered close endpoints; not HTF range depth, scanner or labels."""
from decimal import Decimal,DecimalException,Context,localcontext

def flag_endpoints(rows, declared_sessions, decision, authority):
    required={'source','calendar','sessions','actions','historical_availability'}
    if (not isinstance(authority,dict) or set(authority)!=required
            or any(authority[k]!='qualified' for k in required)):
        return {'status':'blocked','reason':'authority'}
    try:
        if (type(decision) is not int or not isinstance(rows,list) or len(rows)!=3
                or not isinstance(declared_sessions,list) or len(declared_sessions)!=3
                or any(not isinstance(s,str) or not s for s in declared_sessions)
                or len(set(declared_sessions))!=3
                or [r['session'] for r in rows]!=declared_sessions):raise ValueError('fixed boundaries')
        seen=set();closes=[];times=[]
        with localcontext(Context(prec=50)):
            for row in rows:
                if (any(not isinstance(row[k],str) or not row[k] for k in ['source_id','security_id'])
                        or row['source_id'] in seen or row['security_id']!=rows[0]['security_id']
                        or row['basis']!='action_normalized_close' or row['complete'] is not True
                        or row['clock_kind'] not in {'observed','qualified_historical'}
                        or type(row['close_at']) is not int or type(row['available_at']) is not int
                        or not row['close_at']<=row['available_at']<=decision
                        or isinstance(row['close'],bool)):raise ValueError('endpoint contract')
                close=Decimal(str(row['close']))
                if not close.is_finite() or close<=0:raise ValueError('close')
                closes.append(close);times.append(row['close_at']);seen.add(row['source_id'])
            if not times[0]<times[1]<times[2]:raise ValueError('chronology')
            advance=closes[1]/closes[0]-1
            retreat=1-closes[2]/closes[1]
        return {'status':'fixed-close endpoint ingredient','advance':str(advance),
                'endpoint_retreat':str(retreat),'range_depth_authority':False,'empirical_admission':False}
    except (KeyError,ValueError,TypeError,DecimalException):
        return {'status':'blocked','reason':'fixed endpoint contract'}
