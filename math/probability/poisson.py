#!/usr/bin/env python3
"""Poisson distribution."""


class Poisson:
    """Represents a poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize with data or with an expected lambtha."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Return the PMF value for k successes."""
        k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        factorial = 1
        for i in range(2, k + 1):
            factorial *= i
        return (e ** -self.lambtha) * (self.lambtha ** k) / factorial

    def cdf(self, k):
        """Return the CDF value for k successes."""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
