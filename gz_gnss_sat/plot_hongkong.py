# import gmplot package
import gmplot
import numpy as np
import csv
import pandas as pd

df = pd.read_csv('UrbanNav_raw.csv')
csvdata = df.values

raw_data = {
        "lat": [],
        "lon": [],
        "alt": [],
        "heading": [],
    }

for i, a in enumerate(csvdata):
    if (i==0): 
        pass
    else:
        data = np.char.split(a[0]).tolist()
        data= [float(i) for i in data]

        lat = data[3]+data[4]/60 + data[5]/3600
        lon = data[6]+data[7]/60 + data[8]/3600
        raw_data["lat"].append(lat)
        raw_data["lon"].append(lon)
        raw_data["heading"].append(data[-1])

import json
with open("hk_raw.json", "w") as f:
        json.dump(raw_data, f)



gmap4 = gmplot.GoogleMapPlotter(raw_data["lat"][0],raw_data["lon"][0], 10,  map_type='satellite')

# heatmap plot heating Type
# points on the Google map
for i in range(0, len(raw_data["lat"])):
    gmap4.marker( raw_data["lat"][i], raw_data["lon"][i] )
  
gmap4.draw("waypoints_hk.html" )