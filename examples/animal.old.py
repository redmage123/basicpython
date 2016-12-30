#!/usr/bin/env python

class Owner: 

    def __init__(self,o_name,o_address,o_phone,**kwargs):
        self.name = o_name
        self.address = o_address
        self.phone = o_phone
        if kwargs[type] == "Dog":
            self.pet = Dog(name=kwargs[name],breed=kwargs[breed],age=kwargs[age])
        else:
            self.pet = Cat(name=kwargs[name],breed=kwargs[breed],age=kwargs[age])

    def getName(self):
        return(self.name)

    def getAddress(self):
        return(self.address)

    def getPhone(self):
        return(self.Phone)

    def getPet(self):
        return self.pet

class Animal:
    def __init__(self,name):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def GetName(self):
        return(self.name)

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return("Woof!")

class Cat(Animal):
    def speak(self):
        return("Meow!")


