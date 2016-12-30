#!/usr/bin/env python


import sys

x = 1 
try:
    assert(x==0)
except AssertionError:
    print "X isn't zero!"
    sys.exit(1)

