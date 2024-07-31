import numpy as np

def get_dimensions(arr):
    return arr.shape

array_2d = np.full((6, 5), 7)
dimensions = get_dimensions(array_2d)
print("Dimensions (rows, columns):", dimensions)
