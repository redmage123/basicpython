#!/usr/bin/python3

PI = 3.1415927
shapetocalculate = input("Please enter in a shape to calculate: ")

if shapetocalculate == "Sphere":
    radius = float(input("Please enter in the radius of the sphere to calculate: "))
    volume = 4/3 * PI * radius ** 3
    area = 4 * PI * radius ** 2
    circumference = 2* PI * radius
    print ("Volume is %.2f, Area is %.2f, Circumference is %.2f" % (volume, area, circumference))

elif shapetocalculate == "Circle":
    radius = float(input("Please enter in the radius of the circle to calculate: "))
    area =  PI * radius **2
    circumference = 2 * PI * radius
    print ("Area is %.2f, Circumference is %.2f" % (area, circumference))

elif shapetocalculate == "Rectangle":
    width = float(input("Please enter the width: "))
    height = float(input("Please enter the height: "))
    area = width * height
    print ("Area is %.2f" % (area))

elif shapetocalculate == "Square":
    side = float(input("Please enter in the side of the square: "))
    area = side ** 2
    print ("Area is %.2f" % (area))

elif shapetocalculate == "Triangle":
    base = float(input("Please enter in the base of the triangle: "))
    height = float(input("Please enter in the height of the triangle: "))
    area = .5 * base  * height
    print ("Area is %.2f" % (area))
