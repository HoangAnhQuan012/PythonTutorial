import numpy as np
products = np.array(
    ["salad", "bread", "mustard", "rare tomato", "cola", "gourmet ice cream"]
)

# Filter the product array to only include those with prices greater than 25.
prices = np.array([15, 20, 5, 30, 10, 40])
print(products[prices > 25])

# Modify your logic to include cola, despite it not having a price greater than 25.
# Store the elements returned in an array called fancy_feast_special.
print(products[(prices > 25) | (products == "cola")])

# Next, create a shipping cost array where the cost is 0 if price is greater than 20, and 5 if not.

shipping_cost = np.where(prices > 20, 0, 5)
print(shipping_cost)