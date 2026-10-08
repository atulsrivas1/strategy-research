"""Research-only daily input normalization. No market reader or outcome evaluator."""
from copy import deepcopy
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation

UNDEF_PRICE = 9223372036854775807


def bounded_prior_sessions(signal_session, count=20):
    """Primary-source checked sample schedule only; no broad calendar claim.

    NYSE 2025 calendar and Nasdaq ETA2025-58 establish the Labor Day closure.
    Dates beyond this audited August/September interval fail closed.
    """
    try:
        signal = date.fromisoformat(signal_session)
        first, last = date(2025,8,13), date(2025,9,11)
        if type(count) is not int or not 1 <= count <= 20 or not first <= signal <= last:
            return None
        sessions=[]; day=first
        while day <= last:
            if day.weekday() < 5 and day != date(2025,9,1):
                sessions.append(day.isoformat())
            day += timedelta(days=1)
        if signal_session not in sessions:
            return None
        prior=[d for d in sessions if d < signal_session]
        return prior[-count:] if len(prior) >= count else None
    except (TypeError,ValueError):
        return None


def aware_utc(value):
    stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ValueError('Timezone-aware clock required')
    return stamp.astimezone(timezone.utc)


def price(value, unit):
    if isinstance(value, bool) or value is None:
        raise ValueError('Invalid price')
    if unit == 'integer_nanos':
        if type(value) is not int or value == UNDEF_PRICE:
            raise ValueError('Integer nanos required; undefined sentinel excluded')
        result = Decimal(value) / Decimal(1_000_000_000)
    elif unit == 'decimal_dollars':
        result = Decimal(str(value))
    else:
        raise ValueError('Explicit price unit required')
    if not result.is_finite() or result <= 0:
        raise ValueError('Finite positive equity price required')
    return result


def normalize_bar(row, unit, interval_basis):
    """Retain original values; ts_utc is interval start, not available-at."""
    try:
        if not isinstance(row['symbol'], str) or not row['symbol']:
            raise ValueError('Identity missing')
        if type(row['instrument_id']) is not int or row['instrument_id'] <= 0:
            raise ValueError('Identity missing')
        start = aware_utc(row['ts_utc'])
        if interval_basis != 'utc_day' or start.time().isoformat() != '00:00:00':
            raise ValueError('Only explicit UTC-midnight daily intervals supported')
        values = {k: price(row[k], unit) for k in ['open','high','low','close']}
        if not values['low'] <= min(values['open'], values['close']) <= max(values['open'], values['close']) <= values['high']:
            raise ValueError('OHLC bounds')
        if type(row['volume']) is not int or row['volume'] < 0:
            raise ValueError('Nonnegative integer volume required')
    except (KeyError, TypeError, ValueError, InvalidOperation, AttributeError) as e:
        return {'status':'blocked', 'reason':str(e)}
    return {'status':'normalized ingredient', 'original':deepcopy(row),
            'symbol':row['symbol'], 'instrument_id':row['instrument_id'],
            'utc_date':start.date().isoformat(), 'prices':values, 'volume':row['volume'],
            'interval_start':start, 'interval_end':start+timedelta(days=1),
            'interval_basis':'utc_day', 'available_at':None, 'clock_kind':'unknown',
            'regular_session_authority':False, 'empirical_admission':False}


def split_feature_view(bar, events, decision_at, decision_session, coverage):
    """Split-only feature view; never mutate prices used for execution.

    Factors multiply pre-effective-date prices; volumes use reciprocal factors.
    Cash dividends are explicitly excluded from this price-breakout basis.
    Caller must qualify dated event completeness, versions and historical clocks.
    """
    try:
        decision = aware_utc(decision_at)
        day = date.fromisoformat(decision_session)
        bar_day = date.fromisoformat(bar['utc_date'])
        if bar['status'] != 'normalized ingredient' or bar_day >= day or bar['interval_end'] > decision:
            raise ValueError('Incomplete or non-prior bar')
        if (coverage.get('authority') != 'qualified' or not coverage.get('source_id')
                or date.fromisoformat(coverage['start']) > bar_day
                or date.fromisoformat(coverage['end']) < day):
            raise ValueError('Action coverage unqualified')
        factor = Decimal(1); applied=[]; excluded=[]; identifiers=set()
        for event in events:
            if not event.get('id') or event['id'] in identifiers:
                raise ValueError('Unique event version required')
            identifiers.add(event['id'])
            if event.get('symbol') != bar['symbol']:
                raise ValueError('Event identity mismatch')
            effective = date.fromisoformat(event['effective_session'])
            if effective > day or effective <= bar_day:
                excluded.append(event['id']); continue
            if event.get('type') == 'cash_dividend':
                excluded.append(event['id']); continue
            if event.get('type') != 'split':
                raise ValueError('Unsupported action')
            if (event.get('clock_kind') not in {'observed','qualified_historical'}
                    or aware_utc(event['available_at']) > decision or not event.get('source_id')):
                raise ValueError('Historical action clock/source unqualified')
            adjustment = price(event['price_factor'], 'decimal_dollars')
            factor *= adjustment; applied.append(event['id'])
    except (KeyError, TypeError, ValueError, InvalidOperation, AttributeError) as e:
        return {'status':'blocked', 'reason':str(e)}
    return {'status':'split-only feature view', 'prices':{k:v*factor for k,v in bar['prices'].items()},
            'volume':Decimal(bar['volume'])/factor, 'factor':factor,
            'applied':applied, 'excluded':excluded, 'original':deepcopy(bar['original']),
            'execution_prices_changed':False, 'empirical_admission':False}


def availability_admission(interval_end, available_at, clock_kind, decision_at, interval_basis):
    """A completed UTC-day bar does not become a core-session bar by relabeling."""
    try:
        decision = aware_utc(decision_at)
        if (interval_basis != 'qualified_core_session'
                or clock_kind not in {'observed','qualified_historical'}):
            return False
        end, arrival = aware_utc(interval_end), aware_utc(available_at)
        return end <= arrival <= decision
    except (TypeError,ValueError,AttributeError):
        return False
