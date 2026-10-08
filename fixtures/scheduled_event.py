"""Synthetic announced schedule ledger; no feed certification or trading policy."""

def scheduled_event(rows, event_id, decision, authority):
    required={'source','complete_ledger','historical_availability'}
    if (not isinstance(authority,dict) or set(authority)!=required
            or any(authority[k]!='qualified' for k in required)):
        return {'status':'blocked','reason':'authority'}
    try:
        if (not isinstance(rows,list) or not isinstance(event_id,str) or not event_id
                or type(decision) is not int):raise ValueError('scope')
        seen=set();sources=set();eligible=[]
        for row in rows:
            if (row['event_id']!=event_id or row['kind']!='scheduled_FOMC'
                    or row['status'] not in {'active','cancelled'}
                    or row['clock_kind'] not in {'observed','qualified_historical'}
                    or any(not isinstance(row[k],str) or not row[k] for k in ['version_id','source_id'])
                    or row['version_id'] in seen or row['source_id'] in sources
                    or any(type(row[k]) is not int for k in ['published_at','available_at','event_at'])
                    or row['published_at']>row['available_at']):raise ValueError('ledger')
            seen.add(row['version_id']);sources.add(row['source_id'])
            if row['available_at']<=decision:eligible.append(row)
        if not eligible:return {'status':'unknown','empirical_admission':False}
        latest=max(r['available_at'] for r in eligible)
        candidates=[r for r in eligible if r['available_at']==latest]
        if len(candidates)!=1:raise ValueError('ambiguous latest version')
        row=candidates[0]
        state=('cancelled' if row['status']=='cancelled' else
               'at_or_after_event' if row['event_at']<=decision else 'scheduled_future')
        result={'status':state,'version_id':row['version_id'],'source_id':row['source_id'],
                'empirical_admission':False}
        if state=='scheduled_future':result['seconds_to_event']=row['event_at']-decision
        return result
    except (KeyError,TypeError,ValueError):
        return {'status':'blocked','reason':'schedule contract'}
