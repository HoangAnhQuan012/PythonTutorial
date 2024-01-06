# The sort() method will sort arrays in place
# • Use the axis argument to specify the dimension to sort by

import numpy as np

sales_array = np.array([
    [0, 5, 155, 0, 518],
    [0, 1827, 616, 317, 325]
])

# axis=1 by default, which sorts a 
# two-dimensional array row by row
sales_array.sort()
print(sales_array)

# axis=0 will sort by columns
sales_array.sort(axis=0)
print(sales_array)