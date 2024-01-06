import numpy as np

prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])

prices.sort()
print(prices)
# First, grab the top 3 highest priced items in our list.

top3 = prices[-3:]
print(top3)

# Then, calculated the mean, min, max, and median of the top three prices.

print(top3.mean())
print(top3.min())
print(top3.max())
print(np.median(top3))


# Finally, calculate the number of unique price tiers in our price_tiers array.

price_tiers = np.array(["budget", "budget", "mid-tier", "luxury", "mid-tier", "luxury"])

print(np.unique(price_tiers))
