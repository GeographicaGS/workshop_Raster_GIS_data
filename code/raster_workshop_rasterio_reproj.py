# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.
#  https://github.com/GeographicaGS
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


import rasterio
from rasterio.warp import calculate_default_transform, reproject, RESAMPLING

my_file='/tmp/example_data.tif'
dst_file='/tmp/example_data_new.tif'


dst_crs = 'EPSG:3857'

with rasterio.open(my_file) as src:

    affine, width, height = calculate_default_transform(
        src.crs, dst_crs, src.width, src.height, -179., -85., 179., 85.)
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': affine,
        'affine': affine,
        'width': width,
        'height': height
    })

    with rasterio.open(dst_file, 'w', **kwargs) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.affine,
            src_crs=src.crs,
            dst_transform=affine,
            dst_crs=dst_crs,
            resampling=RESAMPLING.nearest)
