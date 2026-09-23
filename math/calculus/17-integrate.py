#!/usr/bin/env python3
"""Calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Return the integral of poly as a new list of coefficients.

    poly is a list of coefficients representing a polynomial, where
    the index of the list represents the power of x that the
    coefficient belongs to. C is the integration constant. If poly
    or C are not valid, return None. The returned list is as small
    as possible, with whole-number coefficients stored as integers.
    """
    if not isinstance(poly, list) or len(poly) == 0 or \
            not all(isinstance(c, (int, float)) for c in poly) or \
            not isinstance(C, (int, float)):
        return None
    integral = [C]
    for power, coef in enumerate(poly):
        term = coef / (power + 1)
        if term == int(term):
            term = int(term)
        integral.append(term)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
