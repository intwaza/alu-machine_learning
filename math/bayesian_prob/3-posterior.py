#!/usr/bin/env python3
"""Calculates the posterior probability given the data."""
import numpy as np


def likelihood(x, n, P):
    """Return the likelihood of obtaining x and n for each probability in P."""
    comb = 1
    for i in range(1, x + 1):
        comb = comb * (n - x + i) // i
    return float(comb) * P ** x * (1 - P) ** (n - x)


def intersection(x, n, P, Pr):
    """Return the intersection of obtaining x and n with each P."""
    return likelihood(x, n, P) * Pr


def marginal(x, n, P, Pr):
    """Return the marginal probability of obtaining x and n."""
    return np.sum(intersection(x, n, P, Pr))


def posterior(x, n, P, Pr):
    """Return the posterior probability of each P given x and n.

    x is the number of patients that develop severe side effects, n is
    the total number of patients observed, P is a 1D numpy.ndarray of
    hypothetical probabilities, and Pr is a numpy.ndarray of the prior
    beliefs of P.
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    return intersection(x, n, P, Pr) / marginal(x, n, P, Pr)
