#!/usr/bin/env python

i = 2
def isPrime(n):
    global i
    if n == 0 or n == 1:
        return(False)
    elif (n % i == 0) and (n == i):
        i = 2
        return(True)
    elif n % i  == 0:
        i = 2
        return(False)
    else:
        i += 1
        return(isPrime(n))

print isPrime(17)
print isPrime(4)
print isPrime(5)
