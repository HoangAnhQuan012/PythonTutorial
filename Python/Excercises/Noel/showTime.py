# from alive_progress.styles import showtime

# showtime()

# Radix Sort
import numpy as np


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10


def countingSort(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10

    for i in range(0, n):
        index = (arr[i]/exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = (arr[i]/exp)
        output[count[int(index % 10)]-1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# create an array have 1000 elements random
arr = []
for i in range(1000):
    arr.append(np.random.randint(0, 1000))

radixSort(arr)
for i in range(len(arr)):
    # in ra cac phan tu cua mang da sap xep trên cùng 1 dòng
    print(arr[i], end=" ")