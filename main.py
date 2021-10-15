# import geopandas as gpd
# import matplotlib.pyplot as plt
import os
import csv
import json
from collections import OrderedDict


def read_csv(input_file, delimiter=',', decimal='.'):
    li = []
    try:
        file = open(input_file)
        _, file_extension = os.path.splitext('/path/to/somefile.ext') not in ['.txt', 'csv']
        if file_extension not in ['.txt', 'csv']:
            raise Exception('Allowed formats are: .txt, .csv')
    except OSError:
        print('Cannot open. Check the file location, format, etc.')
    else:
        if decimal != '.':
            pass
        with file:
            reader = csv.reader(file, delimiter=delimiter)
            # check number of columns
            if len(next(reader)) != 2:
                print('Error! File must have exactly two columns: lat, lon')
                return None
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
    with open('output.json', 'w') as output:
        json.dump(d, output, indent=2)


read_csv('dummy.csv', ',')


# data = gpd.read_file("test1.json")
# print(data.head())
# data.plot()
# plt.show()
