"""D1 ingredient contract v1. Synthetic research machinery, not a market replay."""
from decimal import Decimal, InvalidOperation


def qualify_window(bars, expected_sessions, signal_session, close, close_available_at,
                   decision_at, authorities):
    """Return blocked rather than a trading decision when authority is incomplete.

    Session identifiers and clocks must already use one qualified, comparable basis.
    Callers supply the exact calendar; this function does not infer holidays.
    Future and signal-day bars cannot change the prior-window threshold.
    """
    required = {'calendar', 'universe', 'adjustment', 'historical_availability', 'source_parity'}
    if set(authorities) != required or any(authorities[k] != 'qualified' for k in required):
        return {'status': 'blocked', 'reason': 'authority'}
    if (len(expected_sessions) != 20 or len(set(expected_sessions)) != 20
            or expected_sessions != sorted(expected_sessions)
            or any(d >= signal_session for d in expected_sessions)):
        return {'status': 'blocked', 'reason': 'calendar'}
    try:
        if close_available_at is None or close_available_at > decision_at:
            return {'status': 'blocked', 'reason': 'close clock'}
        selected = [b for b in bars if b['session'] in expected_sessions]
        if len(selected) != 20 or {b['session'] for b in selected} != set(expected_sessions):
            return {'status': 'blocked', 'reason': 'coverage'}
        highs = []
        for b in selected:
            if b.get('available_at') is None or b['available_at'] > decision_at:
                return {'status': 'blocked', 'reason': 'bar clock'}
            high = Decimal(str(b['high']))
            if not high.is_finite() or high <= 0:
                return {'status': 'blocked', 'reason': 'price'}
            highs.append(high)
        completed_close = Decimal(str(close))
        if not completed_close.is_finite() or completed_close <= 0:
            return {'status': 'blocked', 'reason': 'price'}
    except (KeyError, TypeError, ValueError, InvalidOperation):
        return {'status': 'blocked', 'reason': 'invalid field'}
    threshold = max(highs)
    return {'status': 'qualified ingredient', 'prior20_high': str(threshold),
            'breakout': completed_close > threshold,
            'empirical_admission': False}
