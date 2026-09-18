"""
Geo Raster Toolkit

An open-source Python toolkit for geospatial raster analysis
and remote sensing workflows.
"""

from .indices import ndvi, ndwi

__version__ = "0.1.0"

__all__ = [
    "ndvi",
    "ndwi",
]
