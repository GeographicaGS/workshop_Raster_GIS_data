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

from landsat.downloader import Downloader
from landsat.search import Search


sr = Search()

def searchLandsat():
    """
    paths_rows (String) – A string in this format: “003,003,004,004”. Must be in pairs and separated by comma.
    lat (String, float, integer) – The latitude
    lon (String, float, integer) – The The longitude
    start_date (String) – Date string. format: YYYY-MM-DD
    end_date (String) – date string. format: YYYY-MM-DD
    cloud_min (float) – float specifying the minimum percentage. e.g. 4.3
    cloud_max (float) – float specifying the maximum percentage. e.g. 78.9
    limit (integer) – integer specigying the maximum results return.
    """
    return sr.search(paths_rows="201,035", start_date="2015-06-15", end_date="2015-10-14", cloud_max=10.)

# {'status': u'SUCCESS', 'total_returned': 1, 'total': 2, 'limit': 1, 'results': [{'sat_type': u'L8', 'sceneID': u'LC82010352015204LGN00', 'date': u'2015-07-23', 'path': '201', 'thumbnail': u'http://earthexplorer.usgs.gov/browse/landsat_8/2015/201/035/LC82010352015204LGN00.jpg', 'cloud': 4.08, 'row': u'035'}]}


dl = Downloader(verbose=True,download_dir="/home/cayetano/landsat/downloads/")

def dwldLandsat():
    dl.download("LC82010352015204LGN00")


res = searchLandsat()
print(res)
