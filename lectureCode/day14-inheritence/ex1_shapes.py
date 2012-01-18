import math

class Shape(object):
    x = 0
    y = 0

    def area(self):
        "Generic shaps don't really have an area function"
        return None

    def move(self, x, y):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)


r1 = Rectangle(4,5)
r2 = Rectangle(5,10)
print "r1 area: %d,  r2 area: %d" % (r1.area(), r2.area())
