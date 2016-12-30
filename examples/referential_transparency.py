#!/usr/bin/python3


counter=0

def referentiallyTransparent(x):
    return x+1


def referentiallyOpaque(x):
    global counter
    counter +=1
    return x+counter

print(referentiallyTransparent(5))
print(referentiallyOpaque(5))
