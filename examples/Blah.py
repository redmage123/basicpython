#!/usr/bin/env python



def HappyBirthday(n="Bob"):

    print "Happy Birthday to you, happy birthday to you! Happy Birthday dear " + n + " Happy Birthday to you!"


HappyBirthday()

name = raw_input("Please enter the name: ")
if (len(name) == 0):
    print "name = ",name
    HappyBirthday()
else:
    HappyBirthday(name)
