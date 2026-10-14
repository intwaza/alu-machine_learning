#!/usr/bin/env python3
"""Calculates the mean and covariance of a data set."""
import numpy as np


def mean_cov(X):
    """Return the mean and covariance matrix of the data set X.

    X is a numpy.ndarray of shape (n, d). Returns mean of shape (1, d)
    and cov of shape (d, d).
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n = X.shape[0]
    if n < 2:
        raise ValueError("X must contain multiple data points")
    mean = np.mean(X, axis=0, keepdims=True)
    centered = X - mean
    cov = np.matmul(centered.T, centered) / (n - 1)
    return mean, cov
