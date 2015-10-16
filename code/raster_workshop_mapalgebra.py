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

dst_file = '/tmp/out_mapalgebra.tif'
src_file01 = '/home/cayetano/Dropbox/documentos/python/GIS/workshop_RasterGIS_data/data/temp_gfs/tmp_2m_k_20150903.tif'
src_file02 = '/home/cayetano/Dropbox/documentos/python/GIS/workshop_RasterGIS_data/data/temp_gfs/tmp_80m_k_20150903.tif'


with rasterio.open(src_file01) as src:
    for i in src.indexes:
        band = src.read(i)
        print(i, band.min(), band.max())


with rasterio.open(src_file01) as src:
    for i in src.indexes:
        band = src.read(i)
        print(type(band))
        print(band.shape, band.ndim, band.size)
        print(band)


with rasterio.open(src_file01) as src01:
    with rasterio.open(src_file02) as src02:
        for i in src01.indexes:
            band_src01 = src01.read(i)
            print(band_src01)
        for i in src02.indexes:
            band_src02 = src02.read(i)
            print(band_src02)


with rasterio.open(src_file01) as src01:
    with rasterio.open(src_file02) as src02:
        for i in src01.indexes:
            band_src01 = src01.read(i)
        for i in src02.indexes:
            band_src02 = src02.read(i)
        res = (band_src01 -273.15) - (band_src02 -273.15)
        print(res)


with rasterio.open(src_file01) as src01:
    with rasterio.open(src_file02) as src02:
        for i in src01.indexes:
            band_src01 = src01.read(i)
        for i in src02.indexes:
            band_src02 = src02.read(i)
        res = (band_src01 -273.15) - (band_src02 -273.15)
        kwargs = src.meta
        with rasterio.open(dst_file, 'w', **kwargs) as dst:
            dst.write_band(1, res)
