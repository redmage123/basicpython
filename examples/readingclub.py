#!/usr/bin/env python

memberlist=[]

while (1):
    member = raw_input("Please enter a member name (x to exit): ")
    if member == "x":
        break
    memberlist.append(member)

print memberlist

