#!/usr/bin/env python3
"""Performs a strided convolution on grayscale images."""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Return the convolution of images with kernel.

    images is a numpy.ndarray of shape (m, h, w) containing grayscale
    images and kernel is a numpy.ndarray of shape (kh, kw). padding is
    a tuple (ph, pw), 'same', or 'valid', and the images are padded
    with 0's. stride is a tuple (sh, sw).
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(np.ceil(((h - 1) * sh + kh - h) / 2))
        pw = int(np.ceil(((w - 1) * sw + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')
    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1
    output = np.zeros((m, out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            patch = padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
