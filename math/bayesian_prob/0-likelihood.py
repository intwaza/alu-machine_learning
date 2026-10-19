#!/usr/bin/env python3
"""Calculates the likelihood of data given hypothetical probabilities."""
import numpy as np


def likelihood(x, n, P):
    """Return the likelihood of obtaining x and n for each probability in P.

    x is the number of patients that develop severe side effects, n is
    the total number of patients observed, and P is a 1D numpy.ndarray
    of hypothetical probabilities. x is assumed binomially distributed.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    comb = 1
    for i in range(1, x + 1):
        comb = comb * (n - x + i) // i
    return comb * P ** x * (1 - P) ** (n - x)
