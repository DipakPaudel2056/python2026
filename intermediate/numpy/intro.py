# what the f** is numpy?
# it is a python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.

import numpy as np
# creating a numpy array
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)

print(np.__version__) # prints the version of numpy


# array indexing
print("First element:", arr[0])  # accessing first element
print("Last element:", arr[-1])  # accessing last element
print("Slice of array:", arr[1:4])  # slicing the array from index 1 to 3

# array operations
print("Array after adding 5:", arr + 5)  # adding 5 to each element
print("Array after multiplying by 2:", arr * 2)  # multiplying each element by 2
print("Square of each element:", arr ** 2)  # squaring each element

# multidimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Numpy Array (Matrix):\n", matrix)

# accessing elements in 2D array
print("Element at (0,0):", matrix[0, 0])  # accessing element at first row, first column
print("First row:", matrix[0, :])  # accessing first row
print("Second column:", matrix[:, 1])  # accessing second column

# array shape
print("Shape of the matrix:", matrix.shape)  # prints the shape of the matrix
# reshaping array
reshaped_matrix = matrix.reshape(1, 9)
print("Reshaped Matrix (1x9):", reshaped_matrix)  # prints the reshaped matrix




