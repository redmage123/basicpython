#!/usr/bin/env python
list2 = []
list1=[i for i in range(1,21)]
for i in xrange(0,len(list1),2):
    x = list1[i] 
    if x > len(list1):
        break
    y = list1[i+1]
    list2.append(x+y)

print list2

