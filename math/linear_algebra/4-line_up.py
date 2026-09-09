#!/usr/bin/env python3
"""Adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return a new list with arr1 and arr2 added element-wise."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
