"""Explicit seeded Wilder RSI(2), synthetic source/clock contract; no scanner."""
from decimal import Decimal, DecimalException, Context, localcontext


def seeded_rsi2(rows, expected_sessions, history_start, decision_at, security_id, source_id, authority):
    required = {'prices', 'actions', 'calendar', 'historical_availability', 'initialization'}
    if (not isinstance(authority, dict) or set(authority) != required
            or any(authority[k] != 'qualified' for k in required)):
        return {'status': 'blocked', 'reason': 'authority'}
    if (not isinstance(rows, list) or not isinstance(expected_sessions, list)
            or len(expected_sessions) < 3 or len(rows) != len(expected_sessions)
            or any(type(s) is not int or s < 0 for s in expected_sessions)
            or expected_sessions != sorted(set(expected_sessions))
            or type(history_start) is not int or history_start != expected_sessions[0]
            or type(decision_at) is not int
            or not isinstance(security_id, str) or not security_id
            or not isinstance(source_id, str) or not source_id):
        return {'status': 'blocked', 'reason': 'session/initialization contract'}
    closes = []
    previous_close_at = -1
    try:
        with localcontext(Context(prec=50)):
            for row, session in zip(rows, expected_sessions):
                if (type(row['session_id']) is not int or row['session_id'] != session
                        or row['security_id'] != security_id or row['source_id'] != source_id
                        or row['price_basis'] != 'qualified_split_basis'
                        or row['clock_kind'] not in {'observed', 'qualified_historical'}
                        or type(row['close_at']) is not int or type(row['available_at']) is not int
                        or not previous_close_at < row['close_at'] <= row['available_at'] < decision_at
                        or isinstance(row['close'], bool)):
                    raise ValueError('price provenance or clock')
                value = Decimal(str(row['close']))
                if not value.is_finite() or value <= 0:
                    raise ValueError('positive finite close required')
                closes.append(value)
                previous_close_at = row['close_at']
            gains = [max(b-a, Decimal(0)) for a,b in zip(closes,closes[1:])]
            losses = [max(a-b, Decimal(0)) for a,b in zip(closes,closes[1:])]
            gain, loss = sum(gains[:2])/2, sum(losses[:2])/2
            output = []
            for i in range(2,len(closes)):
                if i > 2:
                    gain, loss = (gain+gains[i-1])/2, (loss+losses[i-1])/2
                rsi = None if gain+loss == 0 else str(100*gain/(gain+loss))
                output.append({'session_id':expected_sessions[i], 'rsi':rsi,
                               'state':'undefined flat seed' if rsi is None else 'defined'})
    except (KeyError, TypeError, ValueError, DecimalException):
        return {'status': 'blocked', 'reason': 'invalid price/clock input'}
    return {'status':'seeded RSI2 ingredient', 'period':2, 'history_start':history_start,
            'seed':'simple mean of first two changes', 'precision':50,
            'series':output, 'provider_parity':False, 'empirical_admission':False}
