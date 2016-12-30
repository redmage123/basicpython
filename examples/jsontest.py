#!/usr/bin/env python


import json

f = open("foo.out","w")
mylist = [1,2,3,4,5]
json.dump(mylist,f)
f.close()
