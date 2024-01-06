import numpy as np

sales_array = np.array([
    [0, 5, 155, 0, 158],
    [0, 1827, 616, 317, 325]
])

print("This returns an array with elements equal to 2 or less than 6: ", sales_array[(sales_array == 616) | (sales_array < 100)])

print("This returns an array with elements greater than 100 and less than 500: ", sales_array[(sales_array > 100) & (sales_array < 500)])

mask = (sales_array) > 100 & (sales_array < 500)

print(sales_array[mask])

sales_array = np.array([0, 5, 155, 0, 158])

product_array = np.array(['fruits', 'vegetables', 'cereals', 'dairy', 'eggs'], dtype='<U10')
print(product_array)
print("This returns the elements from product_array where values in sales_array are greater than 0: ", product_array[sales_array > 0])

sales_array[1] = 25
print("This assigns a single value via indexing: ", sales_array)

sales_array[sales_array == 0] = 5
print("This filters the zero values in sales_array and assignsthem a new value of 5: ", sales_array)