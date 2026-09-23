#!/usr/bin/env python3
"""Calculates a sum of squares."""


def summation_i_squared(n):
    """Return the sum of i^2 for i from 1 to n.

    n is the stopping condition. If n is not a valid number,
    return None.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
