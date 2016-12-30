#!/usr/bin/env python


mylist = ["fee","fi","fo","fum"]
mynewlist = []

for mystring in mylist:
    mynewlist.append((mystring,mystring.upper(),len(mystring)))

print "The first time through with a standard for loop"
print mynewlist


mynewlist = [ (mystring,mystring.upper(),len(mystring)) for mystring in mylist]

print "The second time through with a list comprehension"
print mynewlist

def mytransformfunc(mystring):
    return(mystring,mystring.upper(),len(mystring))

mynewlist = map(mytransformfunc,mylist)
print "The third time through with a map"
print mynewlist



