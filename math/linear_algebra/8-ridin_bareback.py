#!/usr/bin/env python3
"""Performs matrix multiplication."""


def mat_mul(mat1, mat2):
    """Return a new matrix that is the product of mat1 and mat2."""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
            for row in mat1]
