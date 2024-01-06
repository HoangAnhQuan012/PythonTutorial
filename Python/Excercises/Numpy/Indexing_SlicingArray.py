import numpy as np

product_array = np.array(['fruits', 'vegetables', 'cereal', 'dairy', 'eggs', 'snacks', 'beverages', 'coffee', 'tea', 'spices'])

print(product_array)

print(product_array[1])
print(product_array[-1])

print("Lấy ra 5 elements đầu tiên của array: ", product_array[:5])
print("Lấy ra element thứ 6 của array và cách 2 elements cho đến cuối array", product_array[5::2])

product_array2D = product_array.reshape(2, 5)
print(product_array2D)

print(product_array2D[1, 2])

print(product_array2D[:, 2:])

print(product_array2D[1:, :])