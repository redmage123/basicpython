#!/usr/bin/env python



# Recursive fibonacci sequence
def fib_recursive(n):

    if (n == 0):
        return 0;
    elif (n == 1):
        return(1)
    else:
        return(fib_recursive (n-2) + fib_recursive (n-1))

fib_list = []
for i in range (0,5):
    fib_list.append(fib_recursive(i))

print fib_list


