'''
Created on Jul 20, 2017

@author: Zach

MUST BE RUN FROM OSGeo4W SHELL
'''

print "This script must be run within an OSGeo4W environment"

import os
import progressbar
from osgeo import gdal

parent_dir = 'B:/Workspaces/GIS/UMDBPP/VIRDE/NS67/'

input_dir = parent_dir + 'tiff/'
output_dir = parent_dir + 'geotiff/'

input_csv = 'B:/Workspaces/GIS/GEOG652/final_project/georeference.csv'

print "%s -> %s using %s" % (input_dir, output_dir, input_csv) 

# define column starting georeferenced points
starting_col = 9

temp_paths = []

# read input CSV
with open(input_csv, 'r') as input_file:
    lines = input_file.readlines()
    with progressbar.ProgressBar(max_value=len(lines)) as bar:
        row_num = 1
        prev_percent = 0
        for row in lines:
            row_data = row.replace(' ', '').replace('"', '').replace('\n', '').split(',')
            input_path = input_dir + row_data[1]
            temp_path = output_dir + "tmp_" + row_data[1]
            output_path = output_dir + row_data[1]
            
            if os.path.isfile(input_path) and 'NA' not in row_data:
                gcp_list = list()
                
                gcp_list.append(gdal.GCP(float(row_data[starting_col + 0]), float(row_data[starting_col + 1]), 0, 0, 0))
                gcp_list.append(gdal.GCP(float(row_data[starting_col + 2]), float(row_data[starting_col + 3]), 0, 3280, 0))
                gcp_list.append(gdal.GCP(float(row_data[starting_col + 4]), float(row_data[starting_col + 5]), 0, 0, 2464))
                gcp_list.append(gdal.GCP(float(row_data[starting_col + 6]), float(row_data[starting_col + 7]), 0, 3280, 2464))
    
                # print "Translating %s to %s" % (input_path, output_path)
                percent = (row_num * 100) / len(lines)
                if percent != prev_percent:
                    prev_percent = percent
                    bar.update(row_num)
                
                gdal.Translate(destName = output_path, srcDS = input_path, options = gdal.TranslateOptions(outputSRS = 'EPSG:4326', GCPs = gcp_list, noData = 0))
                
            row_num = row_num + 1

print "done"