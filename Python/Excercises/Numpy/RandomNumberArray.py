import numpy as np
from numpy.random import default_rng

rng = default_rng(12345)

random_array = rng.random(10)

print(random_array)

mean, stddev = 5, 1
random_normal = rng.normal(mean, stddev, size = 10)
print(random_normal)

rng = np.random.default_rng(616)
print(rng.random(10))

print(rng.integers(0, 10, 100))

print(rng.normal(50, 5, 10))