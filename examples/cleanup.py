#!/usr/bin/env python


f = open("ALbb.salaries.2003.csv")
offset = 3
salarylist = []
salary=""

for i in range(0,4):
    f.readline()

input=f.readline()

while (input != ",,,"):
    inputlist = input.split(",")
    salarylist.append(inputlist[offset].replace("\"",""))
    offset +=1
    while inputlist[offset].isdigit() == True:
        salarylist.append(inputlist[offset])
        offset +=1
    del (inputlist[3:offset+1])
    salarylist.append(inputlist[offset].replace("\"",""))
    print "salarylist = ",salarylist,"\n"
    print "salary =",salary,"\n"
    salary.join(salarylist)
    inputlist.insert(3,salary)
    salarylist=[]
    salary=""
    print inputlist
    offset=3
    input=f.readline()

#print inputlist

f.close() 


