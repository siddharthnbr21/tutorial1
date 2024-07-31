import numpy as np

def create_2d_array(rows, columns, filler):
    return np.full((rows, columns), filler)

array_2d = create_2d_array(6, 5, 7)

def print_slices(arr):
    print("Original Array:")
    print(arr)

    print("\nSlice [:]:")
    print(arr[:])

    print("\nSlice [2:5, 0:3]:")
    print(arr[2:5, 0:3])

    print("\nSlice [0:2, 0:5]:")
    print(arr[0:2, 0:5])

    print("\nSlice [-3:-1, 3:1]:")
    print(arr[-3:-1, 3:1])

    print("\nSlice [2:4, 2:4]:")
    print(arr[2:4, 2:4])

    print("\nSlice [-6:1, -4:1]:")
    print(arr[-6:1, -4:1])

print_slices(array_2d)
