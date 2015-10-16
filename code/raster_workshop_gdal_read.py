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

from osgeo import gdal

input_filename = "/data/mde/h10_1050_2-2/h10_1050_2-2.tif"
src_ds = gdal.Open(input_filename)

src_crs = src_ds.GetProjection()
print(src_crs)

src_geot = src_ds.src_ds.GetGeoTransform()
print(src_geot)

count_bands = src_ds.RasterCount
print(count_bands)

for band in range(count_bands):
    src_band = src_ds.GetRasterBand(band + 1)
    stats = src_band.GetStatistics(True, True)
    if stats:
        print("Minimum={:,.4f}, Maximum={:,.4f}, Mean={:,.4f}, StdDev={:,.4f}".format(stats[0], stats[1], stats[2], stats[3]))

# Properly close the datasets to flush to disk
src_ds = None
