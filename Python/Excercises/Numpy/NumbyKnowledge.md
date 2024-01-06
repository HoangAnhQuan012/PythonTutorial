NumPy is an open-source library that is the universal standard for working with
numerical data in Python, and forms the foundation of other libraries like Pandas
Pandas DataFrames are built on NumPy arrays and can leverage NumPy functions

NumPy arrays are fixed-size containers of items that are more efficient than
Python lists or tuples for data processing
• They only store a single data type (mixed data types are stored as a string)
• They can be one dimensional or multi-dimensional
• Array elements can be modified, but the array size cannot change

‘np’ is the standard alias for the NumPy library

ARRAY PROPERTIES
NumPy arrays have these key properties:
• ndim – the number of dimensions (axes) in the array
• shape – the size of the array for each dimension
• size – the total number of elements in the array
• dtype – the data type of the elements in the array

ARRAY CREATION
As an alternative to converting lists, you can create arrays using functions
![Array Creation properties](/Excercises/Numpy/img/ArrCreationProps.png)

As an alternative to converting lists, you can create arrays using functions
![Parameters](/Excercises/Numpy/img/ArrCreationParams.png)

RANDOM NUMBER ARRAYS

You can create random number arrays from a variety of distributions using
NumPy functions and methods (great for sampling and simulation!)
![Random Number Properties](/Excercises/Numpy/img/randomNumProps.png)

You can create random number arrays from a variety of distributions using
NumPy functions and methods (great for sampling and simulation!)

INDEXING & SLICING ARRAYS

Indexing & slicing one-dimensional arrays is the same as base Python
• array[index] – indexing to access a single element (0-indexed)
• array[start:stop:step size] – slicing to access a series of elements (stop is not inclusive)

Indexing & slicing two-dimensional arrays requires an extra index or slice
• array[row index, column index] – indexing to access a single element (0-indexed)
• array[start:stop:step size, start:stop:step size] – slicing to access a series of elements
commit
