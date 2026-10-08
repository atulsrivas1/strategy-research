"""Minute interval aggregation only; never an official auction/core-close certificate."""
from datetime import timedelta
from decimal import Decimal, InvalidOperation
import re
from fixtures.daily_inputs import aware_utc, price


def minute_start(value):
    # datetime has microsecond precision; reject nonzero sub-second text before parsing.
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:00(?:\.0+)?(?:Z|[+-]\d{2}:\d{2})',value):
        raise ValueError('Exact aware minute boundary required; no truncation')
    stamp=aware_utc(value)
    if stamp.second or stamp.microsecond:
        raise ValueError('Minute boundary required')
    return stamp


def aggregate_minutes(rows, start, end, symbol, unit, source_id):
    """Preserve gaps and use [start,end); future/preopen prices cannot enter."""
    try:
        lower,upper=minute_start(start),minute_start(end)
        if upper<=lower or upper-lower>timedelta(days=1) or not source_id or not symbol:
            raise ValueError('Bounded interval and provenance required')
        selected=[];seen=set();identities=set()
        for row in rows:
            stamp=minute_start(row['ts_utc'])
            if stamp<lower or stamp>=upper:
                continue
            if stamp+timedelta(minutes=1)>upper:
                raise ValueError('Cross-boundary interval')
            if stamp in seen:
                raise ValueError('Duplicate interval')
            seen.add(stamp)
            if row['symbol']!=symbol or type(row['instrument_id']) is not int or row['instrument_id']<=0:
                raise ValueError('Identity mismatch')
            identities.add(row['instrument_id'])
            values={k:price(row[k],unit) for k in ['open','high','low','close']}
            if not values['low']<=min(values['open'],values['close'])<=max(values['open'],values['close'])<=values['high']:
                raise ValueError('OHLC bounds')
            if type(row['volume']) is not int or row['volume']<0:
                raise ValueError('Integer nonnegative volume required')
            selected.append((stamp,values,row['volume']))
        if not selected or len(identities)!=1:
            raise ValueError('Missing or ambiguous identity coverage')
        selected.sort(key=lambda x:x[0])
        expected=[];stamp=lower
        while stamp<upper:
            expected.append(stamp);stamp+=timedelta(minutes=1)
        gaps=[s.isoformat() for s in expected if s not in seen]
    except (KeyError,TypeError,ValueError,InvalidOperation,AttributeError) as e:
        return {'status':'blocked','reason':str(e)}
    return {'status':'half-open minute proxy','symbol':symbol,'instrument_id':next(iter(identities)),
            'source_id':source_id,'start':lower.isoformat(),'end':upper.isoformat(),
            'open':selected[0][1]['open'],'high':max(r[1]['high'] for r in selected),
            'low':min(r[1]['low'] for r in selected),'close':selected[-1][1]['close'],
            'volume':sum(r[2] for r in selected),'observed_minutes':len(selected),
            'expected_minutes':len(expected),'missing_minutes':gaps,
            'missingness_authority':'unknown; absent bars do not prove no trades',
            'auction_inclusion':'unqualified','official_close_authority':False,
            'available_at':None,'empirical_admission':False}
