# Array aggregation methods let you calculate metrics like sum, mean, and max
import numpy as np

sales_array = np.array([
    [0, 5, 155, 0, 518],
    [0, 1827, 616, 317, 325]
])

# array.sum() returns the sum of all elements in the array
print(sales_array.sum())

# array.mean() Returns the average of the values in an array
print(sales_array.mean())

# array.max() returns the largest value in the array
print(sales_array.max())

# array.min() returns the smallest value in the array
print(sales_array.min())

# You can also aggregate across rows or columns
# axis=0 aggregates across rows
print(sales_array.sum(axis=0))

# axis=1 aggregates across columns
print(sales_array.sum(axis=1))
