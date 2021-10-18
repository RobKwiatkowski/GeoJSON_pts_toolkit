import numpy as np


def generate(count):
    lon = [10*np.random.rand() for x in range(count)]
    lat = [10*np.random.rand() for x in range(count)]
    a = np.column_stack((np.array(lon), np.array(lat)))
    np.savetxt("dummy.txt", a, delimiter=",")


generate(50000)

