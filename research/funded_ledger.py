"""Finite-cash fractional-share research ledger; no broker execution claims."""
from fractions import Fraction
from decimal import Decimal


def exact(value, positive=False):
    if isinstance(value, (float, bool)):
        raise ValueError('lossy float/bool input forbidden')
    if not isinstance(value, (str, int, Decimal, Fraction)):
        raise ValueError('explicit exact numeric input required')
    value = Fraction(value)
    if value < 0 or (positive and value == 0):
        raise ValueError('invalid nonnegative/positive value')
    return value


def simulate(calendar, orders, entry_prices, exit_prices, marks, capital, fee, veto=()):
    """Orders contain id/security/decision/entry/exit/notional; session indices.

    Entry batches are all-or-none, including fees. Exits occur at the modeled
    session open before entries; marks are session close. Missing planned exits
    remain open/censored. Veto changes no retained original notional. Price keys
    are (session index, stable security ID); unknown actions/clocks remain caller
    uncertainty, never evidence of real execution. No borrowing or cash interest.
    """
    if not calendar or len(set(calendar)) != len(calendar) or list(calendar) != sorted(calendar):
        raise ValueError('unique increasing calendar required')
    initial = cash = exact(capital, True)
    orders = list(orders)
    veto = frozenset(veto)
    cost = exact(fee)
    if cost >= 1:
        raise ValueError('fee must be below one')
    ids = [order['id'] for order in orders]
    if len(set(ids)) != len(ids) or not set(veto).issubset(ids):
        raise ValueError('duplicate order or unknown veto')
    prepared = []
    for order in orders:
        if type(order['security']) is not int or order['security'] <= 0:
            raise ValueError('stable security identity required')
        d, e, x = (order[key] for key in ('decision', 'entry', 'exit'))
        if any(type(t) is not int for t in (d, e, x)) or not 0 <= d < e < x:
            raise ValueError('causal session endpoints required')
        prepared.append(dict(order, notional=exact(order['notional'], True), state='vetoed' if order['id'] in veto else 'planned'))
    lots, daily = [], []
    for session in range(len(calendar)):
        for lot in lots:
            if lot['state'] != 'open' or lot['exit'] != session:
                continue
            value = exit_prices.get((session, lot['security']))
            if value is None:
                lot['state'] = 'censored'
                continue
            proceeds = lot['quantity'] * exact(value, True)
            cash += proceeds * (1-cost)
            lot.update(state='closed', proceeds=proceeds, exit_fee=proceeds*cost)
        batch = [order for order in prepared if order['entry'] == session and order['state'] == 'planned']
        missing = any(entry_prices.get((session, order['security'])) is None for order in batch)
        required = sum((order['notional']*(1+cost) for order in batch), Fraction(0))
        if missing or required > cash:
            for order in batch:
                order['state'] = 'unfilled_missing_price' if missing else 'unfilled_cash'
        else:
            for order in batch:
                purchase = order['notional']
                quantity = purchase / exact(entry_prices[(session, order['security'])], True)
                cash -= purchase*(1+cost)
                order['state'] = 'entered'
                lots.append(dict(order, quantity=quantity, state='open', entry_fee=purchase*cost))
        active = [lot for lot in lots if lot['state'] != 'closed']
        values = [marks.get((session, lot['security'])) for lot in active]
        gross = None if any(value is None for value in values) else sum((lot['quantity']*exact(value, True) for lot, value in zip(active, values)), Fraction(0))
        assert cash >= 0, 'cash conservation failure'
        daily.append(dict(session=session, cash=cash, gross=gross, nav=None if gross is None else cash+gross))
    for order in prepared:
        if order['state'] == 'planned':
            order['state'] = 'not_entered_calendar_end'
    return dict(initial=initial, daily=daily, orders=prepared, lots=lots,
                funding_feasible=not any(order['state'] == 'unfilled_cash' for order in prepared),
                complete=all(lot['state'] == 'closed' for lot in lots) and all(order['state'] in ('entered','vetoed') for order in prepared),
                assumptions='fractional shares; modeled open fills, close marks; proportional fees; zero interest; action treatment caller-declared')


def paired(calendar, orders, entry_prices, exit_prices, marks, capital, fee, veto):
    """Same originals in both arms; never call mismatched fills an overlay effect."""
    orders = list(orders)
    veto = frozenset(veto)
    baseline = simulate(calendar, orders, entry_prices, exit_prices, marks, capital, fee)
    candidate = simulate(calendar, orders, entry_prices, exit_prices, marks, capital, fee, veto)
    b = {order['id']: order for order in baseline['orders']}
    c = {order['id']: order for order in candidate['orders']}
    matched = all(b[key]['state'] == c[key]['state'] and b[key]['notional'] == c[key]['notional'] for key in b if key not in veto)
    comparable = matched and all(arm['funding_feasible'] and arm['complete'] for arm in (baseline, candidate))
    return dict(baseline=baseline, candidate=candidate, matched_retained_schedule=matched, isolated_overlay_comparable=comparable)
