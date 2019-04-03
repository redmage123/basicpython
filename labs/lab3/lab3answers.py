#!/usr/bin/env python3

import math
cartesian = [(1,3),(4,4),(2,6),(-5,2),(2,1),(1,3),(2,6)]
polar = []

def converttopolar(t):

    x = t[0]
    y = t[1]
    return (math.sqrt(x **2 + y **2),math.atan(y/x))

def calculateperfect(n):

    sum = 0
    for x in range(1,n):
        if n % x == 0:
            sum += x
        if sum ==  x:
            return x 
        else:
            return -1


# Calculate the polar coordinates from the given cartesian coordinate list.
# Remove duplicates from the cartesian list.

cartesian = list(set(cartesian))

         
for coord in cartesian:
    polar.append(converttopolar(coord))

print (polar) 

# Create a list of the first 10,000 integers and calculate which of them are perfect numbers.
possibleperfects =  []
for i in range(10):
    if (calculateperfect(i) == i):
        possibleperfects.append(i)

print (possibleperfects)





n = int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if n != 0:
        a[i].append(1)

print (a)
