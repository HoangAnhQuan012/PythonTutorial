# Bài 1: Viết một chương trình Python thực hiện vòng lặp for cho phép tính tổng
# và tổng bình phương của một trăm số nguyên đầu tiên

def sum_1():
    sum = 0
    for i in range(1, 101):
        sum += i
    print("Tổng của một trăm số nguyên đầu tiên là: ", sum)

def sum_2():
    sum = 0
    for i in range(1, 101):
        sum += i ** 2
    print("Tổng bình phương của một trăm số nguyên đầu tiên là: ", sum)

# Bài 2: Viết một chương trình Python tính trung bình cộng của 100 số nguyên đầu tiên.

def average():
    sum = 0
    for i in range(1, 101):
        sum += i
    average = sum / 100
    print("Trung bình cộng của 100 số nguyên đầu tiên là: ", average)

# Bài 3: Viết chương trình Python cho phép tính và in ra giai thừa của một số được nhập vào từ bàn phím

def factorial():
    number = int(input("Nhập số: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Giai thừa của ", number, " là: ", factorial)

print("Bài 1: For")
sum_1()
sum_2()
average()
factorial()
print("---------------------------------------------------")


# Hãy viết chương trình Python cho phép tính và in ra tổng của 100 số nguyên đầu tiên (1-100), dùng vòng lặp While.

def sum_3():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print("Tổng của 100 số nguyên đầu tiên là: ", sum)

# Viết chương trình Python có sử dụng vòng lặp While cho phép in ra những số chia hết cho 3 trong khoảng từ 20-50

def divisible():
    i = 20
    while i <= 50:
        if i % 3 == 0:
            print(i)
        i += 1

print("Bài 2: While")
sum_3()
divisible()
print("---------------------------------------------------")