#!/usr/bin/env python



f = open ("subset")
w = open("newout","w")

header = f.readline()
for athelete in f:
    athelete_data = athelete.strip().split(",")
    outstring = "%s,%d\n" % (athelete_data[0],int(athelete_data[-1]))
    w.write(outstring)

f.close()
w.close()
