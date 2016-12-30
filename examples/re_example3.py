#!/usr/bin/python3

import re
import sys

acctlist = []

try:
    f = open("acct.dat")
except IOError:
    print ("Error")
    sys.exit()

def getkey(item):
    print (item[3])
    return item[3]

for line in f:
    re_obj = re.search("^([0-9]{5})([a-zA-Z]+) ([a-zA-Z]+)(.*)",line.strip())
    if re_obj:
        acctlist.append((re_obj.group(1),re_obj.group(2),re_obj.group(3),float(re_obj.group(4))))
    else: 
        print ("Not matched")

print (sorted(acctlist,key=getkey,reverse=True))
