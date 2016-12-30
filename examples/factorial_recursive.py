#!/usr/bin/env python


fact=0
while (1):
    try:
        fact_num = int(raw_input("Please enter factorial: "))
    except ValueError:
        print "Error:  Not a number: "
        continue
    else:
        break

fact = compute_factorial(fact_num)
print fact

def compute_factorial(f):
    if f == 1:
        return 1
    else:
        return f * compute_factorial(f-1)

