"""Synthetic as-of version selection, not source certification or a scanner."""
from decimal import Decimal, InvalidOperation


def select_vintage(rows, security_id, period_end, metric, decision_at, authority):
    required = {'ledger_completeness', 'historical_availability', 'source'}
    if (set(authority) != required
            or any(authority[k] != 'qualified' for k in required)):
        return {'status': 'blocked', 'reason': 'authority'}
    if (not isinstance(security_id, str) or not security_id
            or not isinstance(metric, str) or not metric
            or type(period_end) is not int or type(decision_at) is not int
            or not 0 <= period_end <= decision_at):
        return {'status': 'blocked', 'reason': 'query'}
    versions = set()
    eligible = []
    for r in rows:
        try:
            if (r['security_id'] != security_id or r['metric'] != metric
                    or type(r['period_end']) is not int or r['period_end'] != period_end
                    or not isinstance(r['version_id'], str) or not r['version_id']
                    or r['version_id'] in versions
                    or not isinstance(r['source_id'], str) or not r['source_id']
                    or r['clock_kind'] not in {'observed', 'qualified_historical'}
                    or type(r['published_at']) is not int
                    or type(r['available_at']) is not int
                    or not period_end <= r['published_at'] <= r['available_at']
                    or isinstance(r['value'], bool)):
                raise ValueError('version provenance')
            value = Decimal(str(r['value']))
            if not value.is_finite():
                raise ValueError('nonfinite value')
            versions.add(r['version_id'])
            if r['available_at'] <= decision_at:
                eligible.append((r['available_at'], r, value))
        except (KeyError, TypeError, ValueError, InvalidOperation):
            return {'status': 'blocked', 'reason': 'invalid or duplicate vintage'}
    if not eligible:
        return {'status': 'unknown', 'reason': 'no available vintage'}
    latest = max(t for t, _, _ in eligible)
    selected = [(r, v) for t, r, v in eligible if t == latest]
    if len(selected) != 1:
        return {'status': 'blocked', 'reason': 'ambiguous latest vintage'}
    r, value = selected[0]
    return {'status': 'synthetic as-of ingredient', 'value': str(value),
            'version_id': r['version_id'], 'source_id': r['source_id'],
            'available_at': latest, 'empirical_admission': False}
