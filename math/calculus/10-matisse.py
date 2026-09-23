#!/usr/bin/env python3
"""Calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """Return the derivative of poly as a new list of coefficients.

    poly is a list of coefficients representing a polynomial, where
    the index of the list represents the power of x that the
    coefficient belongs to. If poly is not valid, return None.
    """
    if not isinstance(poly, list) or len(poly) == 0 or \
            not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:
        return [0]
    derivative = [coef * power for power, coef in enumerate(poly)][1:]
    if all(coef == 0 for coef in derivative):
        return [0]
    return derivative
