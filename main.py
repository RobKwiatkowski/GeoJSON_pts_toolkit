# import geopandas as gpd
# import matplotlib.pyplot as plt
import os
import csv
import json
from collections import OrderedDict


def read_csv(input_file, output_file='output.json', delimiter=','):
    li = []
    try:
        file = open(input_file)
        _, file_extension = os.path.splitext(input_file)
        if file_extension not in ['.txt', '.csv']:
            raise TypeError('Allowed formats are: .txt, .csv')
    except FileNotFoundError:
        print('Cannot open. Check the file location, format, etc.')
        raise
    else:
        with file:
            reader = csv.reader(file, delimiter=delimiter)
            # check number of columns
            if len(next(reader)) != 2:
                print('Error! File must have exactly two columns: lat, lon')
                return None
            # write the GeoJSON body
            for row in reader:
                try:
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
    with open(output_file, 'w') as output:
        json.dump(d, output, indent=2)


if __name__ == '__main__':
    read_csv('dummy.txt', 'output.json', delimiter=';')


# data = gpd.read_file("test1.json")
# print(data.head())
# data.plot()
# plt.show()
