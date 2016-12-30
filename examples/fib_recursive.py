#!/usr/bin/env python

fib=0
while (1):
    try:
        fib_num = int(raw_input("Please enter length of fibonacci sequence: "))
    except ValueError:
        print "Error:  Not a number: "
        continue
    else:
        break


def fib(fn):
    if fn == 0:
        return 0
    elif fn  == 1:
        return 1
    else:
        return (fib(fn-1) + fib(fn-2)

