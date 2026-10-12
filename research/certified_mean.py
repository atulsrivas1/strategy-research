"""Certified interval for an exact rational mean without a collapsed denominator."""
from fractions import Fraction


def certified_mean(values, places=80):
    if type(places) is not int or not 1<=places<=120:
        raise ValueError('integer precision from1 through120 required')
    values=list(values)
    if not 1<=len(values)<=512:
        raise ValueError('one through512 terms required')
    scale=10**places;lower=upper=0
    for value in values:
        if type(value) not in (int,Fraction):
            raise ValueError('exact integer or Fraction terms required')
        value=Fraction(value)
        floor,remainder=divmod(value.numerator*scale,value.denominator)
        lower+=floor;upper+=floor+(remainder!=0)
    lo=Fraction(lower,len(values)*scale);hi=Fraction(upper,len(values)*scale)
    return dict(method='integer outward enclosure of exact rational mean',count=len(values),places=places,lower=lo,upper=hi,midpoint=(lo+hi)/2,maximum_absolute_error=(hi-lo)/2)
