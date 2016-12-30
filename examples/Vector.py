#!/usr/bin/env python

class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __str__(self):
        return str(self.x) + "," + str(self.y)


V1 = Vector(1,2)
V2 = Vector(2,3)

V3 = V1 + V2
print V3


