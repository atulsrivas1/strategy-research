"""Split-only opening price gap with synthetic calendar/source authority guards."""
from datetime import date
from decimal import Decimal, DecimalException, Context, localcontext
import re
from fixtures.daily_inputs import aware_utc


def whole_second(value):
    if (not isinstance(value,str) or not re.fullmatch(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.0+)?(?:Z|[+-]\d{2}:\d{2})',value)):
        raise ValueError('Aware whole-second timestamp required; no truncation')
    return aware_utc(value)


def opening_gap(previous, current, calendar, actions, decision_at, authority):
    required={'source','calendar','endpoints','actions','historical_availability'}
    if (not isinstance(authority,dict) or set(authority)!=required
            or any(authority[k]!='qualified' for k in required)):
        return {'status':'blocked','reason':'authority'}
    try:
        sessions=calendar['sessions']
        if (not isinstance(sessions,list) or len(sessions)!=2
                or any(not isinstance(s,str) or date.fromisoformat(s).isoformat()!=s for s in sessions)
                or sessions!=sorted(set(sessions))
                or [previous['session'],current['session']]!=sessions):
            raise ValueError('Exact adjacent exchange-session ledger required')
        close_at,open_at=whole_second(calendar['close_at']),whole_second(calendar['open_at'])
        decision=whole_second(decision_at)
        if not close_at<open_at<decision:
            raise ValueError('Endpoint chronology')
        for item,role,event_at in [(previous,'official_close',close_at),(current,'official_open',open_at)]:
            if (item['role']!=role or item['price_basis']!='raw_unadjusted'
                    or item['source_id']!=calendar['endpoint_sources'][role]
                    or item['clock_kind'] not in {'observed','qualified_historical'}
                    or any(not isinstance(item[k],str) or not item[k] for k in ['security_id','currency','source_id'])
                    or whole_second(item['event_at'])!=event_at
                    or not event_at<=whole_second(item['available_at'])<decision):
                raise ValueError('Endpoint scope/availability')
        if (previous['security_id']!=current['security_id'] or previous['currency']!=current['currency']
                or not whole_second(previous['available_at'])<open_at
                or actions['security_id']!=current['security_id'] or actions['complete'] is not True
                or whole_second(actions['from_at'])!=close_at or whole_second(actions['to_at'])!=open_at
                or not isinstance(actions['rows'],list)):
            raise ValueError('Identity/action coverage')
        with localcontext(Context(prec=50)):
            prices=[]
            for item in [previous,current]:
                if isinstance(item['price'],bool):raise ValueError('Price')
                p=Decimal(str(item['price']))
                if not p.is_finite() or p<=0:raise ValueError('Price')
                prices.append(p)
            ratio=Decimal(1);seen=set()
            for action in actions['rows']:
                if (action['kind']!='split' or action['security_id']!=current['security_id']
                        or any(not isinstance(action[k],str) or not action[k] for k in ['action_id','source_id'])
                        or action['action_id'] in seen or action['clock_kind'] not in {'observed','qualified_historical'}
                        or not close_at<whole_second(action['effective_at'])<=open_at
                        or not whole_second(action['available_at'])<decision
                        or isinstance(action['new_per_old'],bool)):
                    raise ValueError('Unsupported or unqualified action')
                r=Decimal(str(action['new_per_old']))
                if not r.is_finite() or r<=0:raise ValueError('Split ratio')
                ratio*=r;seen.add(action['action_id'])
            aligned=prices[0]/ratio
            gap=prices[1]/aligned-1
    except (KeyError,TypeError,ValueError,DecimalException):
        return {'status':'blocked','reason':'endpoint/calendar/action contract'}
    return {'status':'split-only opening gap ingredient','sessions':sessions[:],
            'previous_close_in_current_share_units':str(aligned),'split_ratio':str(ratio),
            'gap':str(gap),'measure':'price gap; no cash-distribution or trading return',
            'open_fill_authority':False,'empirical_admission':False}
