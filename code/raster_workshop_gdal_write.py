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

input_filename = "/data/example_data"
src_ds = gdal.Open(input_filename)

out_format_r = "GTiff"
driver_r = gdal.GetDriverByName(out_format_r)

out_rasterfile = "/tmp/oufile.tif"
dst_ds = driver_r.CreateCopy(out_rasterfile, src_ds)

# Properly close the datasets to flush to disk
dst_ds = None
src_ds = None
