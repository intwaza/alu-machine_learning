#!/usr/bin/env python3
"""Performs element-wise addition, subtraction, multiplication, division."""


def np_elementwise(mat1, mat2):
    """Return a tuple of the element-wise sum, diff, product, quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
