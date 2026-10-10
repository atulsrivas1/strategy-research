"""Causal pure-split share units; no inferred events or total-return claims."""
from datetime import date,datetime,timezone
from fractions import Fraction as F


def day(value):
    if not isinstance(value,str) or date.fromisoformat(value).isoformat()!=value:
        raise ValueError('canonical event date required')
    return value


def clock(value):
    if not isinstance(value,str):
        raise ValueError('explicit event/decision clock required')
    parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('timezone-aware clock required')
    return parsed


def normalize(events,names):
    result=[];seen=set();sessions=set()
    for event in events:
        identity=event['instrument_id'];symbol=event['symbol'];identifier=event['id']
        if type(identity) is not int or identity<=0 or names.get(identity)!=symbol:
            raise ValueError('event must match actual cohort identity/symbol')
        if not isinstance(identifier,str) or not identifier or identifier in seen:
            raise ValueError('unique explicit event identity required')
        effective=day(event['effective_date']);published=day(event['publication_date'])
        if (identity,effective) in sessions:
            raise ValueError('duplicate/conflicting share action on one session')
        if event.get('kind')!='split' or event.get('cashflow','0')!='0':
            raise ValueError('only pure splits supported; no cash action silently ignored')
        ratio=event.get('ratio')
        if ratio is not None:
            if isinstance(ratio,(float,bool)) or not isinstance(ratio,(str,int,F)):
                raise ValueError('exact split ratio required')
            ratio=F(ratio)
            if ratio<=0 or ratio==1:raise ValueError('positive nontrivial split ratio required')
        available=event.get('available_at')
        if available is not None and clock(available).astimezone(timezone.utc).date()<date.fromisoformat(published):
            raise ValueError('availability cannot predate public announcement')
        if any(not isinstance(event.get(key),str) or not event[key] for key in ('source','clock_assumption','input_basis')):
            raise ValueError('source/clock/input-basis labels required')
        if event['input_basis']!='raw_share_units':
            raise ValueError('known pre-adjusted/mixed basis cannot be adjusted twice')
        seen.add(identifier);sessions.add((identity,effective))
        result.append(dict(event,ratio=ratio))
    return sorted(result,key=lambda event:(event['effective_date'],event['instrument_id'],event['id']))


def factor(events,identity,row_date,asof_date,asof_clock):
    """Divide a raw historical price by effective known new/old share ratios."""
    day(row_date);day(asof_date);when=clock(asof_clock)
    if row_date>asof_date or when.astimezone(timezone.utc).date()<date.fromisoformat(asof_date):
        raise ValueError('future row or clock before as-of date')
    output=F(1)
    for event in events:
        if event['instrument_id']!=identity or not row_date<event['effective_date']<=asof_date:continue
        if event['ratio'] is None or event['available_at'] is None or clock(event['available_at'])>when:
            return None
        output*=event['ratio']
    return output


def price(value,events,identity,row_date,asof_date,asof_clock):
    if isinstance(value,(float,bool)):raise ValueError('exact raw price required')
    number=F(value)
    if number<=0:raise ValueError('positive raw price required')
    scale=factor(events,identity,row_date,asof_date,asof_clock)
    return None if scale is None else number/scale


def session_events(events,session,asof_clock):
    """Actual splits at this modeled session; unknown/late effective events unresolved."""
    day(session);when=clock(asof_clock)
    if when.astimezone(timezone.utc).date()<date.fromisoformat(session):
        raise ValueError('event-session clock precedes modeled session')
    return [(event,event['ratio'] if event['available_at'] is not None and clock(event['available_at'])<=when else None) for event in events if event['effective_date']==session]
