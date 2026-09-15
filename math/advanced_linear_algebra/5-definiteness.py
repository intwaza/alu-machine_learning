#!/usr/bin/env python3
"""Calculates the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Return the definiteness of matrix.

    matrix is a numpy.ndarray of shape (n, n) whose definiteness
    should be calculated. Returns one of "Positive definite",
    "Positive semi-definite", "Negative semi-definite",
    "Negative definite", "Indefinite", or None if matrix is not a
    valid matrix or does not fit any of the above categories.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or \
            matrix.shape[0] == 0:
        return None
    if not np.array_equal(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvals(matrix)
    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    return "Indefinite"
