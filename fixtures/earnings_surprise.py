"""Synthetic first-print EPS/strict pre-release consensus pairing; no scanner."""
from decimal import Decimal, InvalidOperation
from fixtures.fundamental_vintages import select_vintage


def earnings_difference(actual, consensus_ledger, decision_at, authority):
    required = {'ledger_completeness', 'historical_availability', 'source',
                'actual_first_print', 'release_clock', 'basis'}
    if (not isinstance(authority, dict) or set(authority) != required
            or any(authority[k] != 'qualified' for k in required)):
        return {'status': 'blocked', 'reason': 'authority'}
    basis_keys = ['security_id', 'metric', 'currency', 'share_basis', 'accounting_basis', 'units']
    try:
        if (any(not isinstance(actual[k], str) or not actual[k] for k in basis_keys)
                or actual['metric'] != 'eps' or actual['units'] != 'currency_per_share'
                or actual['first_print'] is not True
                or not isinstance(actual['event_id'], str) or not actual['event_id']
                or not isinstance(actual['version_id'], str) or not actual['version_id']
                or not isinstance(actual['source_id'], str) or not actual['source_id']
                or actual['clock_kind'] not in {'observed', 'qualified_historical'}
                or any(type(actual[k]) is not int for k in
                       ['period_end', 'published_at', 'release_at', 'available_at'])
                or type(decision_at) is not int
                or not 0 <= actual['period_end'] < actual['release_at']
                or actual['published_at'] != actual['release_at']
                or not actual['release_at'] <= actual['available_at'] <= decision_at
                or isinstance(actual['value'], bool)):
            raise ValueError('first-print provenance or clock')
        value = Decimal(str(actual['value']))
        if not value.is_finite():
            raise ValueError('nonfinite actual')
        for row in consensus_ledger:
            if any(row[k] != actual[k] for k in basis_keys):
                raise ValueError('consensus basis mismatch')
    except (KeyError, TypeError, ValueError, InvalidOperation):
        return {'status': 'blocked', 'reason': 'actual or pairing contract'}
    # Toy integer clocks make release-1 the strict pre-release cutoff, not a latency model.
    prior = select_vintage(consensus_ledger, actual['security_id'], actual['period_end'],
                           'eps', actual['release_at'] - 1,
                           {k: authority[k] for k in ['ledger_completeness', 'historical_availability', 'source']})
    if prior['status'] != 'synthetic as-of ingredient':
        return {'status': prior['status'], 'reason': 'pre-release consensus: ' + prior['reason']}
    difference = value - Decimal(prior['value'])
    return {'status': 'synthetic EPS difference ingredient', 'event_id': actual['event_id'],
            'actual_version': actual['version_id'], 'consensus_version': prior['version_id'],
            'consensus_available_at': prior['available_at'], 'difference': str(difference),
            'direction': 'positive' if difference > 0 else 'negative' if difference < 0 else 'zero',
            'measure': 'raw currency-per-share difference; not percentage surprise or SUE',
            'empirical_admission': False}
