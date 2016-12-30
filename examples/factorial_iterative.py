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


for i in range(1,fact_num):
    fact_num = fact_num * i

print "fact_num = ", fact_num,"\n"



