'''
Created on Jul 20, 2017

@author: Zach
'''

import os
from osgeo import gdal

input_dir = 'B:/Workspaces/GIS/VIRDE/NS67/tiff/'
output_dir = 'B:/Workspaces/GIS/VIRDE/NS67/geotiff/'

input_csv = 'B:/Workspaces/R/VIRDE/georeference.csv'

for row in open(input_csv, 'r').readlines():
    row_data = row.replace(' ', '').replace('"', '').replace('\n', '').split(',')
    input_path = input_dir + row_data[1]
    output_path = output_dir + row_data[1]
    if os.path.isfile(input_path) and 'NA' not in row_data:
        gcp_list = list()
        
        gcp_list.append(gdal.GCP(float(row_data[9]), float(row_data[10]), 0, 0, 0))
        gcp_list.append(gdal.GCP(float(row_data[11]), float(row_data[12]), 0, 3296, 0))
        gcp_list.append(gdal.GCP(float(row_data[13]), float(row_data[14]), 0, 0, 2464))
        gcp_list.append(gdal.GCP(float(row_data[15]), float(row_data[16]), 0, 3296, 2464))

        print "Translating %s to %s" % (input_path, output_path)

        gdal.Translate(srcDS = input_path, destName = output_path, GCPs = gcp_list, outputSRS = 'EPSG:4326')