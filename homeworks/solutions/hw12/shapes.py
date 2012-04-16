# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     
import math

class Shape(object):
    def area(self):
        pass

    def perimeter(self):
        pass


class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return self.w*2 + self.h*2

class Square(Rect):
    def __init__(self, side):
        self.w = self.h = side


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)

    def perimeter(self):
        return math.pi * (self.r * 2)

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
import math
def distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return math.sqrt((y2-y1)** 2 + (x2-x1)**2)

def area_of_tri(a,b,c):
    AB = distance(a,b)
    BC = distance(b,c)
    AC = distance(a,c)

    p = (AB+BC+AC) / 2.0
    return math.sqrt(p * (p - AB) * (p - AC) * (p - BC))

class Polygon(Shape):
    def __init__(self, *pts):
        self.pts = pts

    def perimeter(self):
        a = self.pts[0]
        total = 0
        for b in self.pts[1:]:
            total += distance(a,b)
            a = b
        total += distance(self.pts[0], self.pts[-1])
        return total

    def area(self):
        o = self.pts[0]
        area = 0
        for i in range(1, len(self.pts)-1):
            a = self.pts[i]
            b = self.pts[i+1]
            area += area_of_tri(o,a,b)

        return area


