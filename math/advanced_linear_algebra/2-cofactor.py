#!/usr/bin/env python3
"""Calculates the cofactor matrix of a matrix."""


def determinant(matrix):
    """Return the determinant of matrix."""
    if matrix == [[]]:
        return 1
    size = len(matrix)
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


def minor(matrix):
    """Return the minor matrix of matrix."""
    size = len(matrix)
    if size == 1:
        return [[1]]
    result = []
    for i in range(size):
        row_minors = []
        for j in range(size):
            sub = [row[:j] + row[j + 1:]
                   for k, row in enumerate(matrix) if k != i]
            row_minors.append(determinant(sub))
        result.append(row_minors)
    return result


def cofactor(matrix):
    """Return the cofactor matrix of matrix.

    matrix is a list of lists whose cofactor matrix should be calculated.
    """
    if not isinstance(matrix, list) or len(matrix) < 1 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 0 or matrix == [[]] or \
            any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    minors = minor(matrix)
    return [[minors[i][j] * (-1) ** (i + j) for j in range(size)]
            for i in range(size)]
