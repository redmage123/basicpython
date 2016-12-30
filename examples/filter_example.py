#!/usr/bin/python3


def checkifint(s):

    try:
        s = int(s)
        return  False
    except ValueError:
        return True


mylist = ['fee','fi','fo','fum',1,2,3,4,5]

mystrlist = list(filter(checkifint,mylist))

print (mystrlist)


