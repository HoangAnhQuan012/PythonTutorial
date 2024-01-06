# Viết một Chương trình Python cho phép tính toán các hình số học. Chương 
# trình sẽ bao gồm các chức năng như sau:
# 1. Tính diện tích hình tròn
# 2. Tính diện tích hình chữ nhật
# 3. Tính diện tích tam giác
# 4. Tính diện tích hình vuông
# 5. Tính diện tích hình thoi
# 6. Tính diện tích hình bình hành
# 7. Kết thúc
# Hãy định nghĩa các hàm nhận các giá trị tham số đầu vào và trả về diện tích 
# của các hình trên. Chương trình sẽ hiển thị menu như trên, mỗi khi người 
# dùng chọn một mục trên menu thì sẽ gọi hàm tương ứng để thực hiện rồi in 
# kết quả. Hãy cho phép nhập các giá trị vào từ bàn phím

def circle_area(r):
    return 3.14 * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

def square_area(a):
    return a * a

def rhombus_area(a, h):
    return a * h

def parallelogram_area(a, h):
    return a * h

def main(Menu1):
    while True:
        print("1. Tính diện tích hình tròn")
        print("2. Tính diện tích hình chữ nhật")
        print("3. Tính diện tích tam giác")
        print("4. Tính diện tích hình vuông")
        print("5. Tính diện tích hình thoi")
        print("6. Tính diện tích hình bình hành")
        print("7. Kết thúc")
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
            r = float(input("Nhập bán kính: "))
            print("Diện tích hình tròn là: ", circle_area(r))
        elif choice == 2:
            a = float(input("Nhập chiều dài: "))
            b = float(input("Nhập chiều rộng: "))
            print("Diện tích hình chữ nhật là: ", rectangle_area(a, b))
        elif choice == 3:
            a = float(input("Nhập cạnh đáy: "))
            h = float(input("Nhập chiều cao: "))
            print("Diện tích tam giác là: ", triangle_area(a, h))
        elif choice == 4:
            a = float(input("Nhập cạnh: "))
            print("Diện tích hình vuông là: ", square_area(a))
        elif choice == 5:
            a = float(input("Nhập cạnh: "))
            h = float(input("Nhập chiều cao: "))
            print("Diện tích hình thoi là: ", rhombus_area(a, h))
        elif choice == 6:
            a = float(input("Nhập cạnh: "))
            h = float(input("Nhập chiều cao: "))
            print("Diện tích hình bình hành là: ", parallelogram_area(a, h))
        elif choice == 7:
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")



# Viết một chương trình Python mô tả một chiếc máy tính (Calculator), trong đó có các hàm tính 
# toán đại số cơ bản như sau:
# Danh sách các hàm như sau:
# sum(int num1, int num2): Cộng giá trị của hai số, trả về tổng giá trị của hai số.
# minus(int num1, int num2): Trừ giá trị của hai số, trả về hiệu của hai số.
# divide(int num1, int num2): Chia giá trị của hai số, trả về kết quả phép chia giá trị của hai 
# số.
# multiple(int num1, int num2): Nhân giá trị của hai số, trả về kết quả phép nhân giá trị của 
# hai số.
# Giá trị của hai số sẽ được nhập vào từ bàn phím. Yêu cầu: Sau khi người dùng nhập 2 số vào từ 
# bàn phím, hãy gọi các hàm nói trên, sau đó in ra kết qua

def sum(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiple(num1, num2):
    return num1 * num2

def main_2(Menu2):
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhập số thứ hai: "))
    print("Tổng hai số là: ", sum(num1, num2))
    print("Hiệu hai số là: ", minus(num1, num2))
    print("Thương hai số là: ", divide(num1, num2))
    print("Tích hai số là: ", multiple(num1, num2))

# main_2()


# Hãy viết một chương trình Python cho phép sử dụng module. Hãy tạo một 
# module bao gồm các hàm sau:
# Tính diện tích hình chữ nhật
# Tính diện tích hình tròn
# Tính diện tích hình thang
# Tính diện tích hình tam giác vuông
# Tính diện tích hình thoi
# Tính diện tích hình tam giác cân
# Tính diện tích hình bình hành.
# Các hàm này sẽ trả về diện tích của hình tương ứng. 
# Sau đó, hãy import tất cả các hàm của module này (có tên là hinhhoc.py), rồi gọi 
# các hàm trong module ra để sử dụng

from Module import HinhHoc

def main_3(Menu3):
    print("Diện tích hình chữ nhật là: ", HinhHoc.rectangle_area(2, 3))
    print("Diện tích hình tròn là: ", HinhHoc.circle_area(3))
    print("Diện tích hình thang là: ", HinhHoc.trapezoid_area(2, 3, 4))
    print("Diện tích hình tam giác vuông là: ", HinhHoc.right_triangle_area(2, 3))
    print("Diện tích hình thoi là: ", HinhHoc.rhombus_area(2, 3))
    print("Diện tích hình tam giác cân là: ", HinhHoc.isosceles_triangle_area(2, 3))
    print("Diện tích hình bình hành là: ", HinhHoc.parallelogram_area(2, 3))

# main_3()

# Hãy viết một chương trình Python cho phép sử dụng module để tính toán diện tích của các hình 
# nâng cao. Hãy tạo một module bao gồm các hàm sau:
# Tính chu vi và diện tích hình bình hành (các cạnh được nhập vào từ bàn phím)
# Tính chu vi và diện tích hình trụ (chiều cao và thông số khác được nhập vào từ bàn phím)
# Tính chu vi và diện tích hình thoi
# Tính chu vi và diện tích hình ngũ giác đều
# Tính chu vi và diện tích hình thang cân
# Các hàm này sẽ trả về chu vi và diện tích của hình tương ứng. Mỗi hình sẽ bao gồm 2 hàm tính 
# chu vi và diện tích riêng.
# Sau đó, hãy import tất cả các hàm của module này (có tên là hinhhocnangcao.py), rồi gọi các 
# hàm trong module ra để sử dụng

from Module import HinhHocNangCao

def main_4(Menu4):
    # các cạnh được nhập vào từ bàn phím
    print("Nhập các cạnh của hình bình hành: ")
    a = float(input("Nhập cạnh thứ nhất: "))
    b = float(input("Nhập cạnh thứ hai: "))
    h = float(input("Nhập chiều cao: "))
    print("Diện tích hình bình hành là: ", HinhHocNangCao.parallelogram_area(a, h))
    print("Chu vi hình bình hành là: ", HinhHocNangCao.parallelogram_perimeter(a, b))
    # chiều cao và thông số khác được nhập vào từ bàn phím
    print("Nhập chiều cao và thông số khác của hình trụ: ")
    r = float(input("Nhập bán kính đáy: "))
    h = float(input("Nhập chiều cao: "))
    print("Diện tích hình trụ là: ", HinhHocNangCao.cylinder_area(r, h))
    print("Chu vi hình trụ là: ", HinhHocNangCao.cylinder_perimeter(r, h))
    # các cạnh được nhập vào từ bàn phím
    print("Nhập các cạnh của hình thoi: ")
    a = float(input("Nhập cạnh: "))
    h = float(input("Nhập chiều cao: "))
    print("Diện tích hình thoi là: ", HinhHocNangCao.rhombus_area(a, h))
    print("Chu vi hình thoi là: ", HinhHocNangCao.rhombus_perimeter(a))
    # các cạnh được nhập vào từ bàn phím
    print("Nhập các cạnh của hình ngũ giác đều: ")
    a = float(input("Nhập cạnh: "))
    print("Diện tích hình ngũ giác đều là: ", HinhHocNangCao.pentagon_area(a))
    print("Chu vi hình ngũ giác đều là: ", HinhHocNangCao.pentagon_perimeter(a))
    # các cạnh được nhập vào từ bàn phím
    print("Nhập các cạnh của hình thang cân: ")
    a = float(input("Nhập cạnh thứ nhất: "))
    b = float(input("Nhập cạnh thứ hai: "))
    c = float(input("Nhập cạnh thứ ba: "))
    print("Diện tích hình thang cân là: ", HinhHocNangCao.isosceles_trapezoid_area(a, b, c))
    print("Chu vi hình thang cân là: ", HinhHocNangCao.isosceles_trapezoid_perimeter(a, b, c))

# main_4()

# Người dùng truyền 1 lựa chọn từ bàn phím để chạy các main() tương ứng
def RunProgram():
    print("1. Tính diện tích các hình")
    print("2. Máy tính đơn giản")
    print("3. Tính diện tích các hình bằng module")
    print("4. Tính diện tích các hình nâng cao bằng module")
    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        main(choice)
    elif choice == 2:
        main_2(choice)
    elif choice == 3:
        main_3(choice)
    elif choice == 4:
        main_4(choice)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

RunProgram()