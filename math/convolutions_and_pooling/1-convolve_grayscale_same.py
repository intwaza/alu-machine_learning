#!/usr/bin/env python3
"""Performs a same convolution on grayscale images."""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Return the same convolution of images with kernel.

    images is a numpy.ndarray of shape (m, h, w) containing grayscale
    images and kernel is a numpy.ndarray of shape (kh, kw). The images
    are padded with 0's so the output has shape (m, h, w).
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2
    padded = np.pad(images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)),
                    mode='constant')
    output = np.zeros((m, h, w))
    for i in range(h):
        for j in range(w):
            patch = padded[:, i:i + kh, j:j + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
