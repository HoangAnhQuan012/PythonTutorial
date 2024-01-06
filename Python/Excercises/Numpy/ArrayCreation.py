import numpy as np

# NumPy arrays have these key properties:
# • ndim – the number of dimensions (axes) in the array
# • shape – the size of the array for each dimension
# • size – the total number of elements in the array
# • dtype – the data type of the elements in the array

# Numpy Array and Array Properties
print("NUMPY ARRAY AND ARRAY PROPERTIES")
array = np.array(range(5))
print(array)

array_2d = np.array([range(5), range(5)])

print(array_2d + 1)

print("Array Shape: ", array.shape)
print("Array 2D Shape: ", array_2d.shape)
print("Array size: ", array.size)
print("Array 2D size: ", array_2d.size)
print("Array 2D T size: ", array_2d.T.size)
print("Array ndim: ", array.ndim)
print("Array 2D ndim: ", array_2d.ndim)
print("Array dtype: ", array.dtype)
print("Array 2D dtype: ", array_2d.dtype)
print("Array I love you: ", np.array(['I', 'Love', 'Python']))
print("-----------------------------------------")


# Array Creation
print("ARRAY CREATION")
print("np.ones(5): ", np.ones(5))
print("np.ones(2, dtype = 'int'): ", np.ones(2, dtype = 'int'))
print("np.zeros((5, 20), 'int'): ", np.zeros((5, 20), 'int'))
print("np.identity(10): ", np.identity(10))
print("np.linspace(10, 100, 10): ", np.linspace(10, 100, 10))
print("-----------------------------------------")



