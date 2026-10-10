"""Explicit admitted-bundle CLI. No provider/lake access or implicit real-data run."""
import argparse
import hashlib
import json
import sys
from decimal import Decimal
from datetime import date
from pathlib import Path
import d2_funded_v3 as engine
import execution_guard as guard


def admission_check(admission, path):
    if admission.get('kind') not in ('synthetic','development') or admission.get('final_access') is not False:
        raise ValueError('explicit development/synthetic admission required')
    if Path(admission['bundle']).resolve()!=Path(path).resolve() or len(admission['sha256'])!=64:
        raise ValueError('exact bundle path/hash admission required')
    if admission.get('exposure')!='potentially exposed development' and admission['kind']!='synthetic':
        raise ValueError('cross-project development exposure declaration required')
    if admission['kind']=='development' and (admission.get('experiment_id')!='D2-FUNDED-REPAIR-1' or not Path(admission.get('registry','')).is_absolute()):
        raise ValueError('fixed experiment ID and private absolute trial registry required')
    if admission.get('protected_ranges_reviewed') is not True or 'protected_ranges' not in admission:
        raise ValueError('protected range map required before bundle reads')
    lower,upper=admission['start'],admission['end']
    if any(date.fromisoformat(value).isoformat()!=value for value in (lower,upper)):
        raise ValueError('canonical admitted dates required')
    if lower>upper:
        raise ValueError('invalid admitted bounds')
    p=engine.protocol()
    if admission['kind']=='development' and (admission.get('protocol_version')!=p['version'] or admission.get('price_basis')!=p['price_basis'] or admission.get('action_basis')!=p['action_basis']):
        raise ValueError('explicit versioned repair protocol and action basis required')
    if admission['kind']=='development' and (lower<p['input_start'] or upper>p['input_end']):
        raise ValueError('outside frozen development bounds')
    for start,end in admission['protected_ranges']:
        if any(date.fromisoformat(value).isoformat()!=value for value in (start,end)):
            raise ValueError('canonical protected dates required')
        if start>end or max(start,lower)<=min(end,upper):
            raise ValueError('protected range intersects admitted input')


def registration_check(admission, raw=None):
    if admission['kind']=='synthetic':return None
    path=Path(admission.get('registration',''))
    if not path.is_absolute() or len(admission.get('registration_sha256',''))!=64:
        raise ValueError('explicit frozen correction registration required')
    raw=path.read_bytes() if raw is None else raw
    if hashlib.sha256(raw).hexdigest()!=admission['registration_sha256']:
        raise ValueError('registration bytes changed')
    record=json.loads(raw)
    if record.get('experiment_id')!='D2-FUNDED-REPAIR-1' or record.get('protocol')!=engine.protocol():
        raise ValueError('registered experiment/protocol differs from actual runner')
    if record.get('registry')!=admission['registry'] or record.get('bundle')!=admission['bundle'] or record.get('bundle_sha256')!=admission['sha256']:
        raise ValueError('registered fixed trial/input differs from admission')
    scope={key:value for key,value in admission.items() if key not in ('registration','registration_sha256')}
    if record.get('admission_scope')!=scope:
        raise ValueError('admitted chronology/protection metadata differs from registration')
    actual=guard.source_manifest(engine,Path(__file__).resolve().parents[1])
    actual.update(guard.source_manifest(sys.modules[__name__],Path(__file__).resolve().parents[1]))
    if set(actual)!=set(record['source']) or any(info['sha256_lf']!=record['source'][name]['sha256_lf'] for name,info in actual.items()):
        raise ValueError('actual source differs from registered correction')
    return record


def load(snapshots):
    admission=json.loads(snapshots['admission'])
    if admission['kind']=='development':registration_check(admission,snapshots['registration'])
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
        json.dump({'experiment_id':'D2-FUNDED-REPAIR-1','attempt':str(Path(attempt).resolve()),'state':'claimed before bundle read','arm_fee_configurations':9,'primary_comparisons':1},file)
    return registry


def run(admission_path, attempt):
    try:
        admission_path=Path(admission_path).resolve()
        admission=json.loads(admission_path.read_bytes())  # Metadata only, no market rows.
        bundle_path=Path(admission['bundle']).resolve()
        admission_check(admission,bundle_path)
        registration=registration_check(admission)
    except BaseException as error:
        failed=Path(attempt)
        failed.mkdir(parents=True,exist_ok=False)
        (failed/'receipt.json').write_text(json.dumps({'state':'failed','phase':'admission before bundle read','error_type':type(error).__name__}),encoding='utf-8')
        raise
    frozen=dict(design=engine.protocol(),admission=admission,registration=registration)
    registry=None
    try:
        if admission['kind']=='development':
            registry=claim(admission,attempt)
        paths={'bundle':bundle_path,'admission':admission_path}
        if admission['kind']=='development':paths['registration']=Path(admission['registration']).resolve()
        result=guard.execute(attempt,engine,Path(__file__).resolve().parents[1],frozen,
                             paths,set(paths.values()),load,evaluate)
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
