#!/usr/bin/env python3
"""Performs a convolution on images using multiple kernels."""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Return the convolution of images with multiple kernels.

    images is a numpy.ndarray of shape (m, h, w, c) containing images
    with channels and kernels is a numpy.ndarray of shape
    (kh, kw, c, nc). padding is a tuple (ph, pw), 'same', or 'valid',
    and the images are padded with 0's. stride is a tuple (sh, sw).
    Returns a numpy.ndarray of shape (m, out_h, out_w, nc).
    """
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(np.ceil(((h - 1) * sh + kh - h) / 2))
        pw = int(np.ceil(((w - 1) * sw + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant')
    out_h = (h + 2 * ph - kh) // sh + 1
    out_w = (w + 2 * pw - kw) // sw + 1
    output = np.zeros((m, out_h, out_w, nc))
    for i in range(out_h):
        for j in range(out_w):
            patch = padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            for k in range(nc):
                output[:, i, j, k] = np.sum(patch * kernels[:, :, :, k],
                                            axis=(1, 2, 3))
    return output
