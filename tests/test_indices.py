import numpy as np

from geo_raster_toolkit import ndvi, ndwi


def test_ndvi_basic():
    """Test basic NDVI calculation."""

    nir = np.array([0.8])
    red = np.array([0.2])

    result = ndvi(nir, red)

    expected = np.array([(0.8 - 0.2) / (0.8 + 0.2)])

    np.testing.assert_allclose(result, expected)


def test_ndvi_zero_denominator():
    """Test NDVI when both bands are zero."""

    nir = np.array([0.0])
    red = np.array([0.0])

    result = ndvi(nir, red)

    assert np.isnan(result[0])


def test_ndwi_basic():
    """Test basic NDWI calculation."""

    green = np.array([0.6])
    nir = np.array([0.2])

    result = ndwi(green, nir)

    expected = np.array([(0.6 - 0.2) / (0.6 + 0.2)])

    np.testing.assert_allclose(result, expected)


def test_ndwi_zero_denominator():
    """Test NDWI when both bands are zero."""

    green = np.array([0.0])
    nir = np.array([0.0])

    result = ndwi(green, nir)

    assert np.isnan(result[0])
