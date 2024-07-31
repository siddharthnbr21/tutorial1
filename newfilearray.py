import numpy as np

def create_2d_array(rows, columns, value):
    return np.full((rows, columns), value)

rows = 6
columns = 5
value = 2
array_2d = create_2d_array(rows, columns, value)

print(array_2d)
