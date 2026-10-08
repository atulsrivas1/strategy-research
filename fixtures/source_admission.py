"""Receipt consistency ledger; qualifications require separately inspected evidence."""
import re
from fixtures.opening_gap import whole_second
GATES=['original_lineage','session_semantics','action_basis','historical_availability']

def source_admission(request, evidence):
    try:
        if (not isinstance(request,dict) or set(request)!={'scope_id','source_sha256','requirements'}
                or not isinstance(request['scope_id'],str) or not request['scope_id']
                or not isinstance(request['source_sha256'],str)
                or not re.fullmatch('[0-9a-f]{64}',request['source_sha256'])
                or request['requirements']!=GATES or not isinstance(evidence,list)):
            raise ValueError('frozen request')
        ids=set();entries={}
        for row in evidence:
            if (not isinstance(row,dict) or set(row)!={'gate','scope_id','source_sha256','evidence_id',
                                                      'reason','status','clock_kind','checked_at'}
                    or row['gate'] not in GATES or row['gate'] in entries
                    or row['scope_id']!=request['scope_id'] or row['source_sha256']!=request['source_sha256']
                    or any(not isinstance(row[k],str) or not row[k] for k in ['evidence_id','reason'])
                    or row['evidence_id'] in ids or row['status'] not in {'qualified','blocked','unknown'}
                    or row['clock_kind'] not in {'observed','qualified_historical','unknown','modeled'}):
                raise ValueError('evidence contract')
            whole_second(row['checked_at'])  # Inspection clock is not historical availability.
            ids.add(row['evidence_id']);entries[row['gate']]=row
        unmet=[];receipts=[]
        for gate in GATES:
            row=entries.get(gate)
            if row is None:unmet.append({'gate':gate,'evidence_id':None,'reason':'missing evidence'})
            else:
                receipts.append(row['evidence_id'])
                if row['status']!='qualified' or row['clock_kind'] not in {'observed','qualified_historical'}:
                    unmet.append({'gate':gate,'evidence_id':row['evidence_id'],'reason':row['reason']})
        return {'status':'blocked prerequisites' if unmet else 'receipt-consistent prerequisites',
                'unmet':unmet,'evidence_ids':receipts,'empirical_admission':False,
                'external_evidence_certified':False}
    except (KeyError,TypeError,ValueError,AttributeError):
        return {'status':'blocked','reason':'request/evidence contract','empirical_admission':False}
