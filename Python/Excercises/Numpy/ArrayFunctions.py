# Array functions let you perform other aggregations like median and percentiles

import numpy as np

sales_array = np.array([
    [0, 5, 155, 0, 518],
    [0, 1827, 616, 317, 325]
])

# np.median()  Returns the median value in an array
print(np.median(sales_array))

# np.percentile() Returns a value in the n^th percentile in an array
print(np.percentile(sales_array, 90))

# np.unique() Returns the unique values in an array
print(np.unique(sales_array))

#  np.sqrt() Returns the square root of each element in an array
print(np.sqrt(sales_array))