import numpy as np
rows = 6
columns = 5
array_2d = np.indices((rows, columns)).sum(axis=0) % 2
print(array_2d)

