#!/usr/bin/env python

import sys

def convert(temperature):
     converted_temperature = (float(temperature)-32) * (5.0/9.0)
     print "converted temperature = ",converted_temperature
     return(converted_temperature)

while (True):
    temp=raw_input("Please enter a temperature in Fahrenheit: ")
    if (temp == "x"):
        break
    celsius_temp = convert(temp)
    print celsius_temp

sys.exit(0)
