#!/usr/bin/env python3
"""Calculates the determinant of a matrix."""


def determinant(matrix):
    """Return the determinant of matrix.

    matrix is a list of lists whose determinant should be calculated.
    The list [[]] represents a 0x0 matrix, whose determinant is 1.
    """
    if not isinstance(matrix, list) or len(matrix) < 1 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if size == 1:
        return matrix[0][0]
    if size == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return a * d - b * c
    det = 0
    sign = 1
    for col in range(size):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += sign * matrix[0][col] * determinant(sub)
        sign = -sign
    return det
