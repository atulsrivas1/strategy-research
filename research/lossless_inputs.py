"""Exploratory bars preserving identity, decimal text and uncertainty."""
from datetime import date, datetime
from decimal import Decimal, InvalidOperation


def price(value):
    if isinstance(value, (float, bool)) or not isinstance(value, (str, int, Decimal)):
        raise ValueError('price requires decimal text/integer/Decimal, never float')
    try:
        number = Decimal(value)
    except InvalidOperation as error:
        raise ValueError('invalid decimal price') from error
    if not number.is_finite() or number <= 0:
        raise ValueError('price must be positive and finite')
    return str(number)


def timestamp(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError('timestamp must be original ISO text')
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('timestamp requires timezone')
    return value


def normalize(rows):
    """No qualified flags inferred. Ambiguous cohort identities are rejected."""
    output, seen, symbols = [], set(), {}
    for row in rows:
        identity = row['instrument_id']
        if type(identity) is not int or identity <= 0:
            raise ValueError('positive integer security identity required')
        symbol = row['symbol']
        if not isinstance(symbol, str) or not symbol or symbol != symbol.strip():
            raise ValueError('explicit original symbol required')
        session = row['date']
        if not isinstance(session, str) or date.fromisoformat(session).isoformat() != session:
            raise ValueError('canonical ISO date required')
        if (identity, session) in seen or (symbol in symbols and symbols[symbol] != identity):
            raise ValueError('duplicate/ambiguous identity; quarantine before admission')
        seen.add((identity, session)); symbols[symbol] = identity
        prices = {key: price(row[key]) for key in ('open', 'high', 'low', 'close')}
        p = {key: Decimal(value) for key, value in prices.items()}
        if not p['low'] <= min(p['open'], p['close']) <= max(p['open'], p['close']) <= p['high']:
            raise ValueError('invalid OHLC bounds')
        required = ('source', 'units', 'actions', 'clock_assumption')
        if any(not isinstance(row.get(key), str) or not row[key] for key in required):
            raise ValueError('explicit uncertainty/units labels required')
        volume = row.get('volume')
        if volume is not None and (type(volume) is not int or volume < 0):
            raise ValueError('volume must be nonnegative integer or explicit unknown')
        output.append(dict(instrument_id=identity, symbol=symbol, date=session,
                           **prices, **{key: row[key] for key in required},
                           start=timestamp(row.get('start')),
                           available_at=timestamp(row.get('available_at')),
                           volume=volume,
                           evidence='exploratory-unqualified'))
    return sorted(output, key=lambda row: (row['instrument_id'], row['date']))


def history(rows, identity, decision_date, count, decision_at=None):
    """Reject short/nonunique history and never return post-decision rows."""
    if type(count) is not int or count <= 0:
        raise ValueError('positive history length required')
    if not isinstance(decision_date,str) or date.fromisoformat(decision_date).isoformat()!=decision_date:
        raise ValueError('canonical decision date required')
    if decision_at is not None:
        timestamp(decision_at)
        clock = datetime.fromisoformat(decision_at.replace('Z', '+00:00'))
    else:
        clock = None
    selected = sorted((row for row in rows if row['instrument_id'] == identity and row['date'] <= decision_date), key=lambda row: row['date'])
    if clock is None and any(row['available_at'] is not None for row in selected):
        raise ValueError('explicit decision clock required for timestamped rows')
    if clock is not None:
        selected = [row for row in selected if row['available_at'] is None or datetime.fromisoformat(row['available_at'].replace('Z', '+00:00')) <= clock]
    if len({row['date'] for row in selected}) != len(selected) or len(selected) < count:
        raise ValueError('ambiguous or insufficient history')
    return selected[-count:]
