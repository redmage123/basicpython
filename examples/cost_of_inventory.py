#!/usr/bin/env python

import sys

itemlist = []
itemdict = {}
try:
    f = open("inventory.dat")
except IOError:
    print "ERROR:  No such file!"
    sys.exit(1)

try:
    for item in f:
        itemlist = item.strip().split()
        try:
            itemdict[itemlist[0]] = int(itemlist[3]) * float(itemlist[2])
        except ValueError:
            continue
except IOError:
    print "Error in I/O!"
    sys.exit(1)
finally:
    f.close()




if (expr):
    try:
        do_something_that_raises_an_error
    except theerror:
        print something
else:
       
