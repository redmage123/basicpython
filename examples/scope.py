#!/usr/bin/env python

x = 1

def myfunc(paramx):
    paramx = paramx - 1
    print "Inside myfunc, the value of paramx is ",paramx
    return

myfunc(x)
print "Outside the function, even after calling myfunc, the value of x is ",x
