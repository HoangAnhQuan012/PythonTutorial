# Viết một chương trình Python cho phép định nghĩa lớp. Tạo ra một lớp có tên là Person, 
# bao gồm 3 thuộc tính là name, address và age. Định nghĩa 2 method của lớp này có tên 
# là inputDetails() và displayDetails() để cho phép nhập các giá trị cho các thuộc tính, và 
# hiển thị giá trị của các thuộc tính của lớp.
# Tiếp theo, hãy khai báo 2 đối tượng của lớp, rồi gọi các method của 2 đối tượng này để xem kết quả.

class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    
    def inputDetails(self):
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")
        self.age = input("Enter age: ")

    def displayDetails(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Age: ", self.age)

# person = Person("","","")
# person.inputDetails()
# person.displayDetails()



# Viết một chương trình Python cho phép định nghĩa lớp. Tạo ra một lớp Calculator thể
# hiện máy tính điện tử. Định nghĩa 4 method add(), minus(), devide(), multiple() cho phép 
# thể hiện 4 phép tính cơ bản.
# Sau đó hãy định nghĩa method factorial() cho phép tính và in ra giai thừa của tham số.
# Tiếp theo hãy khởi tạo một đối tượng của lớp, rồi gọi 4 method của lớp để xem kết quả. 
# Chú ý: Hai số được nhập vào từ bàn phím

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def divide(self):
        return self.a / self.b

    def multiple(self):
        return self.a * self.b

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)
        
a = int(input("Enter a: "))
b = int(input("Enter b: "))
calculator = Calculator(a,b)
print(calculator.add())
print(calculator.minus())
print(calculator.divide())
print(calculator.multiple())
print(calculator.factorial(a))