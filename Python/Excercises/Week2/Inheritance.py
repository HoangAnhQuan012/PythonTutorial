# Hãy phát triển chương trình Python cho phép cài đặt tính thừa kế. Định nghĩa một lớp 
# Vehicle thể hiện các phương tiện, trong lớp này gồm 2 thuộc tính là: price, color và một 
# method accelerate(). Tiếp theo, hãy định nghĩa 3 lớp con lần lượt là Bike, Car và Bus kế
# thừa lớp Vehicle. Mỗi lớp này hãy định nghĩa method printDetails() để hiển thị thông tin 
# chi tiết của đối tượng.
# Sau đó, hãy khởi tạo 3 đối tượng thuộc 3 lớp con và hiển thị thông tin chi tiết của từng 
# đối tượng này

class Vehicle:
    def __init__(self, price, color,):
        self.price = price
        self.color = color

    def accelerate(self):
        print("Accelerate")

class Bike(Vehicle):
    def __init__(self, price, color):
        super().__init__(price, color)

    def printDetails(self):
        print("Bike: ")
        print("Price: ", self.price)
        print("Color: ", self.color)

class Car(Vehicle):
    def __init__(self, price, color):
        super().__init__(price, color)

    def printDetails(self):
        print("Car: ")
        print("Price: ", self.price)
        print("Color: ", self.color)

class Bus(Vehicle):
    def __init__(self, price, color):
        super().__init__(price, color)

    def printDetails(self):
        print("Bus: ")
        print("Price: ", self.price)
        print("Color: ", self.color)

bike = Bike(100, "red")
car = Car(200, "blue")
bus = Bus(300, "green")
# print(bike.printDetails())
# print(car.printDetails())
# print(bus.printDetails())


# Hãy viết một chương trình Python cho phép tạo ra các class như hình sau, đồng thời in ra các giá trị của các thuộc tính.
# Vehicle: name, maxPassengers, maxSpeed
# LandVehicle: numWheels, drive() Kế thừa từ Vehicle
# SeaVessel: displacement, launch() Kế thừa từ Vehicle
#  Jeep: soundHorn() Kế thừa từ LandVehicle
# Hovercraft: enterLand(), enterSea() Kế thừa từ LandVehicle và SeaVessel
#  Frigate: fireGun() Kế thừa từ SeaVehicle
# Hãy định nghĩa các class với các thuộc tính và phương thức như hình trên, sau đó hãy 
# khởi tạo các đối tượng của các lớp, rồi hiển thị giá trị của các thuộc tính đó, cũng như gọi 
# các phương thức của các đối tượng. 
# Chú ý: Các lớp có kế thừa lẫn nhau như sơ đồ trên

class Vehicle:
    def __init__(self, name, maxPassengers, maxSpeed,**kwargs):
        self.name = name
        self.maxPassengers = maxPassengers
        self.maxSpeed = maxSpeed

class LandVehicle(Vehicle):
    def __init__(self, name, maxPassengers, maxSpeed, numWheels, **kwargs):
        super().__init__(name=name, maxPassengers=maxPassengers, maxSpeed=maxSpeed,**kwargs)
        self.numWheels = numWheels

    def drive(self):
        print("Drive")

class SeaVessel(Vehicle): 
    def __init__(self, name, maxPassengers, maxSpeed,displacement, **kwargs ):
        super().__init__(name=name, maxPassengers=maxPassengers, maxSpeed=maxSpeed, **kwargs)
        self.displacement = displacement

    def launch(self):
        print("Launch")

class Jeep(LandVehicle):
    def __init__(self, name, maxPassengers, maxSpeed, numWheels, **kwargs):
        super().__init__(name, maxPassengers, maxSpeed, numWheels, **kwargs)

    def soundHorn(self):
        print("Sound horn")

class Hovercraft(LandVehicle, SeaVessel):
    def __init__(self, name, maxPassengers, maxSpeed, numWheels, displacement, **kwargs):
        super(Hovercraft, self).__init__(name = name, maxPassengers = maxPassengers,maxSpeed=  maxSpeed,numWheels= numWheels, displacement = displacement, **kwargs)

    def enterLand(self):
        print("Enter land")

    def enterSea(self):
        print("Enter sea")

class Frigate(SeaVessel):
    def __init__(self, name, maxPassengers, maxSpeed, displacement, **kwargs):
        super().__init__(name=name, maxPassengers=maxPassengers, maxSpeed=maxSpeed, displacement=displacement)

    def fireGun(self):
        print("Fire gun")

jeep = Jeep("jeep", 5, 100, 4)
# print("jeep name:", jeep.name)
# print("jeep maxPassengers:", jeep.maxPassengers)
# print("jeep maxSpeed:", jeep.maxSpeed)
# print("jeep numWheels:", jeep.numWheels)
# jeep.drive()

hovercraft = Hovercraft("hovercraft", 10, 200, 4, 100)
# print("hovercraft name:", hovercraft.name)
# print("hovercraft maxPassengers:", hovercraft.maxPassengers)
# print("hovercraft maxSpeed:", hovercraft.maxSpeed)
# print("hovercraft numWheels:", hovercraft.numWheels)
# print("hovercraft displacement:", hovercraft.displacement)
# hovercraft.drive()
# hovercraft.launch()
# hovercraft.enterLand()
# hovercraft.enterSea()

frigate = Frigate("Frigate", 100, 30, 5000)
# print("frigate name:", frigate.name)
# print("frigate maxPassengers:", frigate.maxPassengers)
# print("frigate maxSpeed:", frigate.maxSpeed)
# print("frigate displacement:", frigate.displacement)
# frigate.launch()
# frigate.fireGun()




# Hãy phát triển một chương trình OOP trong đó có định nghĩa các class có kế thừa với 
# nhau theo quan hệ phân cấp như hình bên dưới. Học viên tự định nghĩa nội dung chi tiết 
# của từng class, bao gồm các thuộc tính và method tương ứng. Mỗi class sẽ bao gồm một
# method display() để hiển thị giá trị các thuộc tính của lớp.
# Sau đó hãy khởi tạo đối tượng của các class trên và gọi các method display(), rồi xem kết 
# quả
# class Shape:
# Class TwoDShape Kế thừa từ Shape
# Class ThreeDShape Kế thừa từ Shape
# Class Circle Kế thừa từ TwoDShape
# Class Square Kế thừa từ TwoDShape
# Class Triangle Kế thừa từ TwoDShape
# Class Sphere Kế thừa từ ThreeDShape
# Class Cube Kế thừa từ ThreeDShape
# Class Tetrahedron Kế thừa từ ThreeDShape

class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name: ", self.name)

class TwoDShape(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def display(self):
        super().display()
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("------------------------------------------")

class ThreeDShape(Shape):
    def __init__(self, name, length, width, height):
        super().__init__(name)
        self.length = length
        self.width = width
        self.height = height

    def display(self):
        super().display()
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Height: ", self.height)
        print("------------------------------------------")

class Circle(TwoDShape):
    def __init__(self, name, length, width):
        super().__init__(name, length, width)

class Square(TwoDShape):
    def __init__(self, name, length, width):
        super().__init__(name, length, width)

class Triangle(TwoDShape):
    def __init__(self, name, length, width):
        super().__init__(name, length, width)

class Sphere(ThreeDShape):
    def __init__(self, name, length, width, height):
        super().__init__(name, length, width, height)

class Cube(ThreeDShape):
    def __init__(self, name, length, width, height):
        super().__init__(name, length, width, height)

class Tetrahedron(ThreeDShape):
    def __init__(self, name, length, width, height):
        super().__init__(name, length, width, height)

circle = Circle("Circle", 10, 10)
circle.display()

square = Square("Square", 10, 10)
square.display()

triangle = Triangle("Triangle", 10, 10)
triangle.display()

sphere = Sphere("Sphere", 10, 10, 10)
sphere.display()

cube = Cube("Cube", 10, 10, 10)
cube.display()

tetrahedron = Tetrahedron("Tetrahedron", 10, 10, 10)
tetrahedron.display()