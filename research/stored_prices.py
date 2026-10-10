"""Exact stored binary64 proxy; never restores original provider precision."""
from decimal import Decimal
from fractions import Fraction
import math


def encode(value):
    if type(value) is not float or not math.isfinite(value) or value <= 0:
        raise ValueError('positive finite stored binary64 required')
    return str(Decimal.from_float(value)), value.hex()


def verify(rows):
    for row in rows:
        witness=row.get('stored_binary64')
        if not isinstance(witness,dict) or set(witness)!={'open','high','low','close'}:
            raise ValueError('exact four-price stored-value witnesses required')
        for key in witness:
            if not isinstance(witness[key],str):
                raise ValueError('canonical binary64 hex witness required')
            value=float.fromhex(witness[key])
            text,hexadecimal=encode(value)
            if witness[key]!=hexadecimal or not isinstance(row[key],str) or row[key]!=text or Fraction(row[key])!=Fraction.from_float(value):
                raise ValueError('stored-value witness/decimal mismatch')
    return True
