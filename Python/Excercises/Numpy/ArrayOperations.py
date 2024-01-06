import numpy as np

sales = [[0, 5, 155, 0, 518], [0, 1827, 616, 317, 325]]

sales_array = np.array(sales)
print(sales_array)
print(sales_array + 2)

quantity = sales_array[0, : ]
price = sales_array[1, : ]

print(quantity)
print(price)

print(quantity * price)