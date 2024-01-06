# Viết chương trình Python cho phép thực hiện những công việc sau:
# a) Tính chu vi và diện tích hình chữ nhật (nhập chiều dài, rộng vào từ bàn phím
# b) Tính chu vi và diện tích hình tam giác (giá trị cạnh và chiều cao nhập vào từ bàn phím
# c) Tính chu vi và diện tích hình tròn (bán kính được nhập vào từ bàn phím)
# d) Tính chu vi và diện tích hình vuông (cạnh được nhập vào từ bàn phím)
# e) Tính chu vi và diện tích hình thang, với chiều dài cạnh và chiều cao được nhập vào từ bàn phím


# Tính chu vi và diện tích hình chữ nhật các giá trị được nhập vào từ bàn phím
def rectangle():
    length = int(input("Nhập chiều dài: "))
    width = int(input("Nhập chiều rộng: "))
    perimeter = (length + width) * 2
    area = length * width
    print("Chu vi hình chữ nhật là: ", perimeter)
    print("Diện tích hình chữ nhật là: ", area)


# Tính chu vi và diện tích hình tam giác
def triangle():
    side = int(input("Nhập cạnh tam giác: "))
    height = int(input("Nhập chiều cao tam giác: "))
    perimeter = side * 3
    area = (side * height) / 2
    print("Chu vi hình tam giác là: ", perimeter)
    print("Diện tích hình tam giác là: ", area)

# Tính chu vi và diện tích hình tròn
def circle():
    radius = int(input("Nhập bán kính hình tròn: "))
    perimeter = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    print("Chu vi hình tròn là: ", perimeter)
    print("Diện tích hình tròn là: ", area)

# Tính chu vi và diện tích hình vuông
def square():
    side = int(input("Nhập cạnh hình vuông: "))
    perimeter = side * 4
    area = side ** 2
    print("Chu vi hình vuông là: ", perimeter)
    print("Diện tích hình vuông là: ", area)

# Tính chu vi và diện tích hình thang
def trapezoid():
    side1 = int(input("Nhập cạnh thứ nhất: "))
    side2 = int(input("Nhập cạnh thứ hai: "))
    height = int(input("Nhập chiều cao: "))
    perimeter = side1 + side2 + 2 * height
    area = (side1 + side2) * height / 2
    print("Chu vi hình thang là: ", perimeter)
    print("Diện tích hình thang là: ", area)

# Gọi tất cả những hàm trên
rectangle()
triangle()
circle()
square()
trapezoid()

