#!/usr/bin/env python


class calculator():
    def __init__(self):
        pass
    def add(self,x,y):
        return(x+y)


calc_test = calculator()


try:
    assert(calc_test.add(1,1) == 2)
except AssertionError:
    print "Add Test failed!"
else:
    print "Test passed!"


