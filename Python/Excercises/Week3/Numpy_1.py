import numpy as np

arrNum = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arrNum)

# - In ra phần tử ở dòng 2, cột 3 trong mảng. (Mở rộng: Hãy nhập giá trị cho các phần tử của mảng vào từ bàn phím)
row = int(input("Nhập phần tử ở dòng: "))
column = int(input("Nhập phần tử ở cột: "))
print("Phần tử ở dòng ", row, ", cột ", column, " là: ", arrNum[row][column])

# - Hãy in ra các giá trị min, max, sum của các trục của mảng (axis 0, axis 1)
print("Min axis0: ", arrNum.min(axis = 0))
print("Max axis0: ", arrNum.max(axis = 0))
print("Sum axis0: ", arrNum.sum(axis = 0))

print("Min axis1: ", arrNum.min(axis = 1))
print("Max axis1: ", arrNum.max(axis = 1))
print("Sum axis1: ", arrNum.sum(axis = 1))

# - Hãy in ra size và shape của mảng
print("Size: ", arrNum.size)
print("Shape: ", arrNum.shape)

# - Hãy in ra số chiều (ndim) của mảng.
print("ndim: ", arrNum.ndim)

# - Hãy thực hiện thao tác reshape để chuyển mảng này thành mảng gồm 4 dòng, 3 cột rồi in lại mảng.
arrNum = arrNum.reshape(4,3)
print("Change to 4 rows, 3 columns:\n", arrNum)

# - Lưu kết quả tính toán ra file text với tên là data.txt
file = open('./Excercises/Week3/data.txt', 'w')
file.write("Min axis0: " + str(arrNum.min(axis = 0)) + "\n")
file.write("Max axis0: " + str(arrNum.max(axis = 0)) + "\n")
file.write("Sum axis0: " + str(arrNum.sum(axis = 0)) + "\n")
file.write("Min axis1: " + str(arrNum.min(axis = 1)) + "\n")
file.write("Max axis1: " + str(arrNum.max(axis = 1)) + "\n")
file.write("Sum axis1: " + str(arrNum.sum(axis = 1)) + "\n")
file.write("Size: " + str(arrNum.size) + "\n")
file.write("Shape: " + str(arrNum.shape) + "\n")
file.write("ndim: " + str(arrNum.ndim) + "\n")
file.write("Change to 4 rows, 3 columns:\n" + str(arrNum))
file.close()


