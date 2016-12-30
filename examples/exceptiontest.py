#!/usr/bin/env python




try:
    if (10/1 == 1):
        print "We never get here!"
    elif (int("blah")):
        print "We never get here either!"
except ValueError:
        print "We got a value error!"
except ZeroDivisionError:
        print "We got a division by zero error!"



