import numpy as np

def create_2d_array(rows, columns, filler):
    return np.full((rows, columns), filler)
rows = 6
columns = 5
filler = 7
array_2d = create_2d_array(rows, columns, filler)
print(array_2d)
