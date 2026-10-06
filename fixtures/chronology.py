"""Date-only evaluation admission; no price, outcome or holdout reader."""
MAX_HOLD=10
MIN_HOLD=2
EMBARGO=10
WINDOWS={'development':('2025-09-11','2025-12-31'),'validation':('2026-01-02','2026-06-30')}

def holding_path(sessions,decision,holding,window_start,window_end):
    if type(holding) is not int or not MIN_HOLD<=holding<=MAX_HOLD or decision not in sessions:return None
    if not window_start<=decision<=window_end:return None
    i=sessions.index(decision);future=sessions[i+1:i+1+holding]
    if len(future)!=holding or not all(window_start<=d<=window_end for d in future):return None
    return future

def embargo_dates(sessions):
    start,end=WINDOWS['validation']
    return [d for d in sessions if start<=d<=end][:EMBARGO]

def decision_admission(symbol,date,sessions,inputs):
    reasons=[]
    period=next((name for name,(start,end) in WINDOWS.items() if start<=date<=end),'warmup')
    if not inputs.get((symbol,date),False):reasons.append('input_not_admitted')
    if period=='warmup':reasons.append('outside_study_windows');path=None
    else:
        if period=='validation' and date in embargo_dates(sessions):reasons.append('validation_embargo')
        path=holding_path(sessions,date,MAX_HOLD,*WINDOWS[period])
        if path is None:reasons.append('maximum_path_crosses_boundary_or_missing')
        elif not all(inputs.get((symbol,d),False) for d in path):reasons.append('future_input_unavailable')
    return {'Symbol':symbol,'Date':date,'period':period,'evaluation_admitted':not reasons,'reasons':'|'.join(reasons),'entry_session':path[0] if path else '', 'maximum_exit_session':path[-1] if path else ''}

def guarded_confirmation_read(contract,loader):
    # This contract is intentionally disabled until a separately qualified plan exists.
    if contract.get('status')!='qualified' or not contract.get('access_enabled') or not contract.get('start') or not contract.get('end'):
        raise PermissionError('Final confirmation unqualified: no outcome access allowed')
    raise PermissionError('This development-only runner has no final-confirmation capability; qualify a separate evaluator')
