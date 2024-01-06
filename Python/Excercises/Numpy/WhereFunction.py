# The where() NumPy function performs a logical test and returns a given value if 
# the test is True, or another if the test is False

# np.where(logical test,
        # value if True,
        # value if False)

# A logical expression that evaluates to True or False
# A value to be returned if the expression evaluates to True
# A value to be returned if the expression evaluates to False
# np Calls the NumPy function library

import numpy as np

inventory_array = np.array([12, 102, 18, 0, 0])
product_array = np.array(['fruits', 'vegetables', 'cereals', 'dairy', 'eggs'], dtype='<U10')

print(np.where(inventory_array <= 0, "Out of stock", "In stock"))
print(np.where(inventory_array <= 0, "Out of stock", product_array))