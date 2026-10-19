#!/usr/bin/env python3
"""Performs pooling on images."""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Return the max or average pooling of images.

    images is a numpy.ndarray of shape (m, h, w, c), kernel_shape is a
    tuple (kh, kw), stride is a tuple (sh, sw), and mode is 'max' or
    'avg'. Returns a numpy.ndarray of shape (m, out_h, out_w, c).
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride
    out_h = (h - kh) // sh + 1
    out_w = (w - kw) // sw + 1
    operation = np.max if mode == 'max' else np.mean
    output = np.zeros((m, out_h, out_w, c))
    for i in range(out_h):
        for j in range(out_w):
            patch = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            output[:, i, j, :] = operation(patch, axis=(1, 2))
    return output
