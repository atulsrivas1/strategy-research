"""Toy normalized transaction-version ledger; not raw Form 4 or routine labels."""
def filing_purchase(rows, identity, decision, authority):
    required={'source','complete_ledger','identity','historical_availability','transaction_mapping'}
    if (not isinstance(authority,dict) or set(authority)!=required
            or any(authority[k]!='qualified' for k in required)):
        return {'status':'blocked','reason':'authority'}
    try:
        keys={'event_id','issuer_id','insider_id','transaction_id'}
        if (not isinstance(identity,dict) or set(identity)!=keys
                or any(not isinstance(v,str) or not v for v in identity.values())
                or not isinstance(rows,list) or type(decision) is not int):raise ValueError('scope')
        seen=set();sources=set();eligible=[]
        for row in rows:
            if (any(row[k]!=identity[k] for k in keys)
                    or any(not isinstance(row[k],str) or not row[k] for k in ['version_id','source_id'])
                    or row['version_id'] in seen or row['source_id'] in sources
                    or row['clock_kind'] not in {'observed','qualified_historical'}
                    or row['market_provenance']!='qualified'
                    or row['market'] not in {'open_market','private'}
                    or row['security'] not in {'common_stock','other'}
                    or row['table'] not in {'I','II'} or row['acquired_disposed'] not in {'A','D'}
                    or row['code'] not in {'P','S','A','M','J'}
                    or any(type(row[k]) is not int for k in ['trade_at','published_at','available_at'])
                    or not row['trade_at']<=row['published_at']<=row['available_at']):raise ValueError('ledger')
            seen.add(row['version_id']);sources.add(row['source_id'])
            if row['available_at']<=decision:eligible.append(row)
        if not eligible:return {'status':'unknown','empirical_admission':False}
        latest=max(r['available_at'] for r in eligible)
        candidates=[r for r in eligible if r['available_at']==latest]
        if len(candidates)!=1:raise ValueError('ambiguous version')
        row=candidates[0]
        purchase=(row['table']=='I' and row['security']=='common_stock' and row['code']=='P'
                  and row['acquired_disposed']=='A' and row['market']=='open_market')
        return {'status':'purchase ingredient' if purchase else 'ineligible',
                'version_id':row['version_id'],'source_id':row['source_id'],
                'routine_classification':'not implemented','empirical_admission':False}
    except (KeyError,ValueError,TypeError):
        return {'status':'blocked','reason':'filing contract'}
