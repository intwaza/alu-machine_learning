#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a new numpy.ndarray that is mat1 concatenated with mat2."""
    return np.concatenate((mat1, mat2), axis=axis)
