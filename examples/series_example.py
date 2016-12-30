#!/usr/bin/env python


import pandas as pd

data = [0,1,2,3,4,5]
s_index = ['a','b','c','d','e','f']

s = pd.Series(data,index=s_index)

print "This is what a series looks like: "
print s



print "Accessing series elements via the index"
print s['a']
print s['e']

print "s.values is the actual raw data"
print s.values

print "This is the sum of series s and itself"
print s+s

print "This is the product of series s and itself"
print s*s
