import numpy as np
import json

# Hãy thử tạo ra mảng với các hàm zeros(), ones(), empty()
arr_zeros = np.zeros((3, 4))
arr_ones = np.ones((3, 4))
arr_empty = np.empty((3, 4))
print("Mảng với các hàm zeros(): \n", arr_zeros)
print("Mảng với các hàm ones(): \n", arr_ones)
print("Mảng với các hàm empty(): \n", arr_empty)

# Hãy khai báo 2 mảng gồm 3 dòng 4 cột, rồi thực hiện các thao tác cộng, trừ, nhân 2 mảng này.
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9 ,10, 11, 12]])
arr2 = np.array([[13, 14, 15, 16], [17, 18, 19, 20], [21 ,22, 23, 24]])
print("Mảng 1: \n", arr1)
print("Mảng 2: \n", arr2)
print("Tổng 2 mảng: \n", arr1 + arr2)
print("Hiệu 2 mảng: \n", arr1 - arr2)
print("Nhân 2 mảng: \n", arr1 * arr2)

# Hãy nối 2 mảng này theo 2 chiều dọc và chiều ngang, sử dụng 2 hàm vstack() và hstack().
vstack = np.vstack((arr1, arr2))
hstack = np.hstack((arr1, arr2))
print("Nối 2 mảng theo chiều dọc: \n", vstack)
print("Nối 2 mảng theo chiều ngang: \n", hstack)

# Hãy tính và in ra min, max, sum của mảng. Sau đó tìm và in ra min, max, sum của từng trục trong mảng (axis = 0, axis = 1)
print("min của mảng: \n", np.min(arr1))
print("max của mảng: \n", np.max(arr1))
print("sum của mảng: \n", np.sum(arr1))
print("min của mảng theo axis = 0: \n", np.min(arr1, axis=0))
print("max của mảng theo axis = 0: \n", np.max(arr1, axis=0))
print("sum của mảng theo axis = 0: \n", np.sum(arr1, axis=0))
print("min của mảng theo axis = 1: \n", np.min(arr1, axis=1))
print("max của mảng theo axis = 1: \n", np.max(arr1, axis=1))
print("sum của mảng theo axis = 1: \n", np.sum(arr1, axis=1))

# Tiếp theo, hãy ghi dữ liệu tính toán được ra file JSON với tên là dulieu.json.

data = {
    "zeros": arr_zeros.tolist(),
    "ones": arr_ones.tolist(),
    "empty": arr_empty.tolist(),
    "arr1": arr1.tolist(),
    "arr2": arr2.tolist(),
    "sum_arr1": np.sum(arr1).tolist(),
    "sum_arr2": np.sum(arr2).tolist(),
    "sum_arr1_axis0": np.sum(arr1, axis=0).tolist(),
    "sum_arr1_axis1": np.sum(arr1, axis=1).tolist(),
    "sum_arr2_axis0": np.sum(arr2, axis=0).tolist(),
    "sum_arr2_axis1": np.sum(arr2, axis=1).tolist(),
    "min_arr1": np.min(arr1).tolist(),
    "min_arr2": np.min(arr2).tolist(),
    "max_arr1": np.max(arr1).tolist(),
    "max_arr2": np.max(arr2).tolist(),
    "min_arr1_axis0": np.min(arr1, axis=0).tolist(),
    "min_arr1_axis1": np.min(arr1, axis=1).tolist(),
    "min_arr2_axis0": np.min(arr2, axis=0).tolist(),
    "min_arr2_axis1": np.min(arr2, axis=1).tolist(),
    "max_arr1_axis0": np.max(arr1, axis=0).tolist(),
    "max_arr1_axis1": np.max(arr1, axis=1).tolist(),
    "max_arr2_axis0": np.max(arr2, axis=0).tolist(),
    "max_arr2_axis1": np.max(arr2, axis=1).tolist()
}

# các kết quả trên sẽ được lưu vào file dulieu.json cách dòng
with open('dulieu.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# indent=4 là để thụt lề 4 khoảng trắng cho các dòng lệnh trong file dulieu.json