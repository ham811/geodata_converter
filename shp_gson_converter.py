# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:05:32 2022

@author: Hamid
"""
import geopandas
import os

shp_file = geopandas.read_file("E:/Freelancing/Fiverr3_CZ/shapefile/mu_010122.shp")
shp_file.crs
shp_file.to_file('E:/Freelancing/Fiverr3_CZ/shapefile/myshpfile.geojson', driver='GeoJSON')



import shapefile
from json import dumps

# read the shapefile
reader = shapefile.Reader("E:/Freelancing/Fiverr3_CZ/shapefile.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
    geometry=geom, properties=atr)) 
   
    # write the GeoJSON file
   
geojson = open("pyshp-demo.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()