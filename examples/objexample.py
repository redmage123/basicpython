#!/usr/bin/env python



class FirstClass():

    classcounter = 0
    def __init__(self,name):
        self.yourname = name
        FirstClass.classcounter +=1
    def  getName(self):
        return self.yourname
    def changeName(self,newname):
        self.yourname = newname



c1 =  FirstClass("Braun Brelin")
print "Before name change, name = ", c1.getName()
print "Changing name now..."
c1.changeName("Barack Obama")
print "After name change, name = ", c1.getName()







