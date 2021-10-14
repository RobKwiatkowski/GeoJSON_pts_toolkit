# import geopandas as gpd
# import matplotlib.pyplot as plt
import csv
import json
from collections import OrderedDict


def read_csv(input_file):
    li = []
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            # check number of columns
            if len(row) != 2:
                print('Error! File must have exactly two columns: lat, lon')
                return None
            # check data type for each row
            try:
                # create a GeoJSON structure
                d = OrderedDict()
                d['type'] = 'Feature'
                d['geometry'] = {
                    'type': 'Point',
                    'coordinates': [float(row[0]), float(row[1])]
                }
                li.append(d)
            except ValueError:
                print('Error! Values must be of numeric type!')

    d = OrderedDict()
    d['type'] = 'FeatureCollection'
    d['features'] = li

    # write an output file
    with open('output.json', 'w') as output:
        json.dump(d, output, indent=2)


read_csv('input_1.csv')

# data = gpd.read_file("test1.json")
# print(data.head())
# data.plot()
# plt.show()



