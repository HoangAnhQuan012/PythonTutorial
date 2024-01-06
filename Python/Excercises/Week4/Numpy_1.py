# Hãy khởi tạo một mảng các số thực sử dụng NumPy, mảng 2 chiều gồm 3 dòng 4 cột, 
# sau đó thực hiện các thao tác sau:
# - Làm tròn số các phần tử của mảng rồi hiển thị.
# - Thực hiện làm tròn lên (ceil()) và làm tròn xuống (floor()) rồi hiển thị kết quả.
# - Hãy hiển thị các giá trị min, max của từng axis trong mảng
# - Tính tổng và trung bình cộng của các phần tử trong mảng
# - Hiển thị các giá trị thống kê: median, mean, average trong mảng
# - Hãy lưu các giá trị được tính toán ở các câu trên vào một file CSV với tên là 
# calculate.csv

import numpy as np

arr = np.array([[1.2, 2.3, 3.4, 4.5], [5.6, 6.7, 7.8, 8.9], [9.1, 10.2, 11.3, 12.4]])
print("Mảng 2 chiều gồm 3 dòng 4 cột: \n", arr)
print("Làm tròn số các phần tử trong mảng: \n", np.round(arr, 0).astype(int))
print("Làm tròn lên: \n", np.ceil(arr))
print("Làm tròn xuống: \n", np.floor(arr))
print("các giá trị min của từng axis: \n", np.min(arr, axis=0))
print("các giá trị max của từng axis: \n", np.max(arr, axis=0))
print("tổng của các phần tử trong mảng: \n", np.sum(arr))
print("trung bình cộng của các phần tử trong mảng\n", np.mean(arr))
print("median: \n", np.median(arr))
print("average: \n", np.average(arr))

# - Hãy lưu tất cả các giá trị được tính toán ở các câu trên vào một file CSV với tên là calculate.csv
import csv

with open('calculate.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Làm tròn số các phần tử trong mảng", "Làm tròn lên", "Làm tròn xuống", "các giá trị min của từng axis", "các giá trị max của từng axis", "tổng của các phần tử trong mảng", "trung bình cộng của các phần tử trong mảng", "median", "average"])
    writer.writerow([np.round(arr, 0).astype(int), np.ceil(arr).astype(int), np.floor(arr).astype(int), np.min(arr, axis=0), np.max(arr, axis=0), np.sum(arr), np.mean(arr), np.median(arr), np.average(arr)])

