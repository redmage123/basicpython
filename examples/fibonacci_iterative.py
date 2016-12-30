#!/usr/bin/env python


def fib_iterative(n):
    a,b = 1, 1
    for i in range (n-1):
        a,b = b,a+b
        print b
    return b
print 0,1
print fib_iterative(8)


