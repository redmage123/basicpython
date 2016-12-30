#!/usr/bin/env python



class Person():

    classcounter = 0
    def __init__(self,name,height,eyecolor,weight,haircolor):
        self.personname = name
        self.height = height
        self.eyecolor = eyecolor
        self.weight = weight
        self.haircolor = haircolor
        Person.classcounter +=1
    def  getName(self):
        return self.personname
    def changeName(self,newname):
        self.personname = personname
    def speak(self):
        return ("Hello")


#personlist = []
#personlist.append(Person("Jillian Kerr",1.5,"Hazel",105,"Brown"))
#personlist.append(Person("John Forde",1.8,"Blue",150,"Blonde"))
#print personlist[0].getName()," says: ",personlist[0].speak()


persondict = {}
personobj = Person("Jillian Kerr",1.5,"Hazel",105,"Brown")
persondict[personobj.getName()] = personobj
persondict["Jillian Kerr"].speak()

