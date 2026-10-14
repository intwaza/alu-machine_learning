#!/usr/bin/env python3
"""Multivariate Normal distribution."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize with data, a numpy.ndarray of shape (d, n)."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Return the PDF value at x, a numpy.ndarray of shape (d, 1)."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))
        diff = x - self.mean
        exponent = -0.5 * np.matmul(
            diff.T, np.matmul(np.linalg.inv(self.cov), diff))
        norm = np.sqrt((2 * np.pi) ** d * np.linalg.det(self.cov))
        return float(np.exp(exponent)[0][0] / norm)
