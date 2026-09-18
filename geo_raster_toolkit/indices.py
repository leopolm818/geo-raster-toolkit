"""
Remote sensing spectral indices.

This module provides functions for calculating common
spectral indices from raster arrays.
"""

import numpy as np


def ndvi(nir, red):
    """
    Calculate Normalized Difference Vegetation Index (NDVI).

    Parameters
    ----------
    nir : numpy.ndarray
        Near-infrared band.
    red : numpy.ndarray
        Red band.

    Returns
    -------
    numpy.ndarray
        NDVI values.

    Formula
    -------
    NDVI = (NIR - Red) / (NIR + Red)
    """

    nir = np.asarray(nir, dtype=float)
    red = np.asarray(red, dtype=float)

    denominator = nir + red

    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.where(
            denominator != 0,
            (nir - red) / denominator,
            np.nan
        )

    return result


def ndwi(green, nir):
    """
    Calculate Normalized Difference Water Index (NDWI).

    Parameters
    ----------
    green : numpy.ndarray
        Green band.
    nir : numpy.ndarray
        Near-infrared band.

    Returns
    -------
    numpy.ndarray
        NDWI values.

    Formula
    -------
    NDWI = (Green - NIR) / (Green + NIR)
    """

    green = np.asarray(green, dtype=float)
    nir = np.asarray(nir, dtype=float)

    denominator = green + nir

    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.where(
            denominator != 0,
            (green - nir) / denominator,
            np.nan
        )

    return result
