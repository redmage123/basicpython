#!/usr/bin/python3

class Parent(object):
    def __init__(self):
        print("In parent\n")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print ("In child\n")

c = Child()
