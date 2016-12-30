#!/usr/bin/env python

import sys

while (1):
    try:
       input = raw_input("Please enter a number: ")
       number = int(input)
    except ValueError:
        if (str(input).upper()  ==  "X"):
            sys.exit()
        else:
            print "You entered an invalid input!"
    else:
        output=0
        try:
            output = 10 / number
        except ZeroDivisionError:
            print "Illegal division by zero"
        print output
