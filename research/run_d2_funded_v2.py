"""Explicit admitted-bundle CLI. No provider/lake access or implicit real-data run."""
import argparse
import hashlib
import json
import sys
from decimal import Decimal
from datetime import date
from pathlib import Path
import d2_funded_v2 as engine
import execution_guard as guard


def admission_check(admission, path):
    if admission.get('kind') not in ('synthetic','development') or admission.get('final_access') is not False:
        raise ValueError('explicit development/synthetic admission required')
    if Path(admission['bundle']).resolve()!=Path(path).resolve() or len(admission['sha256'])!=64:
        raise ValueError('exact bundle path/hash admission required')
    if admission.get('exposure')!='potentially exposed development' and admission['kind']!='synthetic':
        raise ValueError('cross-project development exposure declaration required')
    if admission['kind']=='development' and (admission.get('experiment_id')!='D2-FUNDED-DEV-1' or not Path(admission.get('registry','')).is_absolute()):
        raise ValueError('fixed experiment ID and private absolute trial registry required')
    if admission.get('protected_ranges_reviewed') is not True or 'protected_ranges' not in admission:
        raise ValueError('protected range map required before bundle reads')
    lower,upper=admission['start'],admission['end']
    if any(date.fromisoformat(value).isoformat()!=value for value in (lower,upper)):
        raise ValueError('canonical admitted dates required')
    if lower>upper:
        raise ValueError('invalid admitted bounds')
    p=engine.protocol()
    if admission['kind']=='development' and (lower<p['input_start'] or upper>p['input_end']):
        raise ValueError('outside frozen development bounds')
    for start,end in admission['protected_ranges']:
        if any(date.fromisoformat(value).isoformat()!=value for value in (start,end)):
            raise ValueError('canonical protected dates required')
        if start>end or max(start,lower)<=min(end,upper):
            raise ValueError('protected range intersects admitted input')


def load(snapshots):
    admission=json.loads(snapshots['admission'])
    if hashlib.sha256(snapshots['bundle']).hexdigest()!=admission['sha256']:
        raise ValueError('input differs from preregistered hash')
    bundle=json.loads(snapshots['bundle'],parse_float=Decimal)
    if bundle['kind']!=admission['kind'] or bundle['calendar'][0]!=admission['start'] or bundle['calendar'][-1]!=admission['end']:
        raise ValueError('bundle differs from admitted scope/bounds')
    return bundle


def evaluate(module, bundle):
    return module.evaluate(bundle)


def claim(admission, attempt):
    registry=Path(admission['registry'])
    registry.parent.mkdir(parents=True,exist_ok=True)
    with registry.open('x',encoding='utf-8') as file:
        json.dump({'experiment_id':'D2-FUNDED-DEV-1','attempt':str(Path(attempt).resolve()),'state':'claimed before bundle read','arm_fee_configurations':9,'primary_comparisons':1},file)
    return registry


def run(admission_path, attempt):
    try:
        admission_path=Path(admission_path).resolve()
        admission=json.loads(admission_path.read_bytes())  # Metadata only, no market rows.
        bundle_path=Path(admission['bundle']).resolve()
        admission_check(admission,bundle_path)
    except BaseException as error:
        failed=Path(attempt)
        failed.mkdir(parents=True,exist_ok=False)
        (failed/'receipt.json').write_text(json.dumps({'state':'failed','phase':'admission before bundle read','error_type':type(error).__name__}),encoding='utf-8')
        raise
    frozen=dict(design=engine.protocol(),admission=admission)
    registry=None
    try:
        if admission['kind']=='development':
            registry=claim(admission,attempt)
        result=guard.execute(attempt,engine,Path(__file__).resolve().parents[1],frozen,
                             {'bundle':bundle_path,'admission':admission_path},
                             {bundle_path,admission_path},load,evaluate)
    except BaseException as error:
        if registry is not None:
            record=json.loads(registry.read_text());record['state']='failed; budget consumed'
            registry.write_text(json.dumps(record),encoding='utf-8')
        elif not Path(attempt).exists():
            failed=Path(attempt);failed.mkdir(parents=True,exist_ok=False)
            (failed/'receipt.json').write_text(json.dumps({'state':'failed','phase':'budget before bundle read','error_type':type(error).__name__}),encoding='utf-8')
        raise
    if registry is not None:
        record=json.loads(registry.read_text());record['state']='complete; budget consumed'
        registry.write_text(json.dumps(record),encoding='utf-8')
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--admission',required=True)
    parser.add_argument('--attempt',required=True)
    args=parser.parse_args()
    sys.set_int_max_str_digits(0)  # Exact large rational receipts, no decimal rounding.
    result=run(args.admission,args.attempt)
    print(json.dumps({'state':'complete','verdict':result['verdict'],'final_access':False}))


if __name__=='__main__':
    main()
