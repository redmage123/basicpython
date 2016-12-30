#!/usr/bin/env python

class Cat:

    catCounter=0

    def __init__(self,**kwargs):
        self.breed = kwargs["breed"]
        self.weight = kwargs["weight"]
        self.name = kwargs["name"]
        self.ownername = kwargs["ownername"]
        Cat.catCounter +=1


    def getBreed(self):
        return self.breed

    def setBreed(self,breed):
        self.breed = breed

    def getName(self):
        return self.name

    def getCatNumbers(self):
        return Cat.catCounter

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Name: " + self.name + " Breed: " + self.breed


c = Cat(name="Fluffy",breed="Calico",weight=8,ownername="Braun Brelin")
print c.catCounter
print c.getName()
c1 = Cat(name="Snoopy",breed="Siamese",weight=6,ownername="Braun Brelin")
print c.catCounter
print c1.getName()

