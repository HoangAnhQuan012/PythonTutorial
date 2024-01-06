# Tính chu vi và diện tích hình bình hành (các cạnh được nhập vào từ bàn phím)
def parallelogram_perimeter(a, b):
    return 2 * (a + b)

def parallelogram_area(a, h):
    return a * h

# Tính chu vi và diện tích hình trụ (chiều cao và thông số khác được nhập vào từ bàn phím)
def cylinder_perimeter(r, h):
    return 2 * 3.14 * r * h

def cylinder_area(r, h):
    return 2 * 3.14 * r * (r + h)

# Tính chu vi và diện tích hình thoi
def rhombus_perimeter(a):
    return 4 * a

def rhombus_area(a, h):
    return a * h

# Tính chu vi và diện tích hình ngũ giác đều
def pentagon_perimeter(a):
    return 5 * a

def pentagon_area(a):
    return 1.72 * a * a

# Tính chu vi và diện tích hình thang cân
def isosceles_trapezoid_perimeter(a, b, c):
    return a + b + 2 * c

def isosceles_trapezoid_area(a, b, h):
    return (a + b) * h / 2
