#!/usr/bin/python3

import sys

try:
    f = open('test.dat')
except IOError:
    print ("invalid file")
    sys.exit(1)

try:
    for line in f:
        try:
            x = int(line)
        except ValueError:
            print ('Invalid number')
            continue
except IOError:
    print ('IOError found')
    sys.exit(1)
finally:
    f.close()




