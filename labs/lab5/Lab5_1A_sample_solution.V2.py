#!/usr/bin/python3

import math
import sys

class Shape(object):

    ''' This is the abstract base class shape.  All shapes should derive from this class
    '''

    def __init__():
        pass
    


class Sphere(Shape):

    ''' This is the class Sphere.  Sphere returns the Volume, Area and Circumference given a radius
    '''

    def __init__(self,radius):
        self.radius = radius

    def volume(self):
        return (4/3 * self.radius ** 3  * math.pi)

    def area(self):
        return (4 * self.radius ** 2  * math.pi)

    def circumference(self):
        return (2 * self.radius   * math.pi)

class Circle(Shape):

    ''' This is the class Circle.  Circle returns the Area and Circumference given a radius
    '''

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (self.radius **2 * math.pi)

    def circumference(self):
        return (2 * self.radius  * math.pi)


class Rectangle(Shape):

    ''' This is the class Rectangle.  Rectangle returns the Area given a width and length
    '''

    def __init__(self,**kwargs):
        self.length = kwargs['l']
        self.width = kwargs['w']

    def area(self):
        return (self.length * self.width)


class Square(Shape):

    ''' This is the class Square.  Square returns the Area given a side
    '''

    def __init__(self,side):
        self.side = side

    def area(self):
        return (self.side ** 2)

class Triangle(Shape):
       
    ''' This is the class Triangle.  Square returns the Area given a base and a height
    '''

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return (0.5 * self.base * self.height)

        




def doSphere():
    while (True):
        radius = input ("Please enter in the sphere's radius: ")
        try:
            radius = float(radius)
            break
        except ValueError:
            print ("Invalid value for radius %s!" % (radius))
    sphere = Sphere(radius)
    print ("Volume of sphere with radius %f is %.4f\n" % (radius,sphere.volume()))
    print ("Area of sphere with radius %f is %.4f\n" % (radius,sphere.area()))
    print ("Circumference of sphere with radius %f is %.4f\n" % (radius,sphere.circumference()))
    return

def doCircle():
    while (True):
        radius = input ("Please enter in the circle's radius: ")
        try:
            radius = float(radius)
            break
        except ValueError:
            print ("Invalid value for radius %s!" % (radius))
    circle = Circle(radius)
    print ("Area of sphere with radius %f is %.4f\n" % (radius,circle.area()))
    print ("Circumference of sphere with radius %f is %.4f\n" % (radius,circle.circumference()))
    return

def doRectangle():
    while (True):
        width = input ("Please enter in the rectangle's width: ")
        length = input ("Please enter in the rectangle's length: ")
        try:
            width = float(width)
            length = float(length)
            break
        except ValueError:
            print ("Invalid value for length or width %s %s!" % (width, length))

    rectangle = Rectangle(w = width ,l = length)
    print ("Area of rectangle with width %f and length %s is %.4f\n" % (width,length,rectangle.area()))
    return

def doSquare():
    while (True):
        side = input ("Please enter in the rectangle's width: ")
        try:
            side = float(side)
            break
        except ValueError:
            print ("Invalid value for side  %s!" % (side))

    square = Square(side)
    print ("Area of square with side %f  is %.4f\n" % (side,square.area()))
    return

def doTriangle():
    while (True):
        base = input ("Please enter in the triangle's base: ")
        height = input ("Please enter in the triangle's height: ")
        try:
            base = float(base)
            height = float(height)
            break
        except ValueError:
            print ("Invalid value for height %s  or base  %s!" % (height,base))

    triangle = Triangle(base,height)
    print ("Area of triangle with base %f and height %f is   is %.4f\n" % (base,height,triangle.area()))
    return

def Exit():
    sys.exit()

def main(): 
    shapesdict = {'Sphere':doSphere,
                  'Circle':doCircle,
                  'Rectangle':doRectangle,
                  'Square':doSquare,
                  'Triangle':doTriangle,
                  'Exit':Exit
                  }

    print ("Here")
    while (True):
        shapetouse = input ("Please enter the shape you want: ")
        if shapetouse in shapesdict:
            shapesdict[shapetouse]()
        else:
            print ("Invalid shape!")


if __name__ == '__main__':
    main()






