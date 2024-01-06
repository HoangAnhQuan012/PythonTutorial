class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        print(" square entering")
        super().__init__(length=length, width=length, **kwargs)

class Triangle:
    def __init__(self, base, height, **kwargs):
        print(" triangle entering")
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
    
# x = RightPyramid(2, 4);
# print(x.length)


class Vehicle:
    def __init__(self, name, maxPassengers, maxSpeed, **kwargs):
        self.name = name
        self.maxPassengers = maxPassengers
        self.maxSpeed = maxSpeed
        # super().__init__(**kwargs)

class LandVehicle(Vehicle):
    def __init__(self, name, maxPassengers, maxSpeed, numWheels, **kwargs):
        print(numWheels)
        super().__init__(name=name, maxPassengers=maxPassengers, maxSpeed=maxSpeed,**kwargs)
        self.numWheels = numWheels

    def drive(self):
        print("Drive")

class SeaVessel(Vehicle): 
    def __init__(self, name, maxPassengers, maxSpeed,displacement, **kwargs):
        super().__init__(name=name, maxPassengers=maxPassengers, maxSpeed=maxSpeed,**kwargs)
        self.displacement = displacement

    def launch(self):
        print("Launch")

# class Jeep(LandVehicle):
#     def __init__(self, name, maxPassengers, maxSpeed, numWheels, **kwargs):
#         super().__init__(name, maxPassengers, maxSpeed, numWheels,**kwargs)

#     def soundHorn(self):
#         print("Sound horn")

class Hovercraft(LandVehicle, SeaVessel):
    def __init__(self, name, maxPassengers, maxSpeed, numWheels, displacement, **kwargs):
        super(Hovercraft, self).__init__(name = name, maxPassengers = maxPassengers,maxSpeed=  maxSpeed,numWheels= numWheels, displacement = displacement, **kwargs)

    def enterLand(self):
        print("Enter land")

    def enterSea(self):
        print("Enter sea")

# class Frigate(SeaVessel):
#     def __init__(self, name, maxPassengers, maxSpeed, displacement):
#         super().__init__(name, maxPassengers, maxSpeed)
#         super().__init__(name, maxPassengers, displacement)

#     def fireGun(self):
#         print("Fire gun")
        
hovercraft = Hovercraft("hovercraft", 10, 200, 4, 100)
# print("hovercraft name:", hovercraft.name)
# print("hovercraft maxPassengers:", hovercraft.maxPassengers)
# print("hovercraft maxSpeed:", hovercraft.maxSpeed)
# print("hovercraft numWheels:", hovercraft.numWheels)
# print("hovercraft displacement:", hovercraft.displacement)
hovercraft.drive()
hovercraft.launch()
hovercraft.enterLand()
hovercraft.enterSea()
print(hovercraft.displacement)





    
