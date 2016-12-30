#!/usr/bin/env python
import json


f = open("json_dataexample.dat")
d=[] 

d = json.load(f)


print d[0]["color"]
print d[0]["value"]



