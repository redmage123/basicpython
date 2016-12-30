#!/usr/bin/env python

import sys
from Vector import Vector


V1 = Vector(1,1)
V2 = Vector(2,2)


try:
    V3 = V1 + V2
except TypeError:
    print "Add Test failed!  Not defined"

try:
   assert(V3.getX() == 3 and V3.getY() == 3)
   print "Add Test succeeded!"
except AssertionError:
    print "Add Test failed!"


try:
    V3 = V1 - V2
except TypeError:
    print "Subtraction Test failed! Not defined"
try:
    assert(V3.getX() == -1 and V3.getY() == -1)
    print "Subtraction Test succeeded!"
except AssertionError:
    print "Subtraction Test failed!"
