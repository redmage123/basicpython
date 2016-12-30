#!/usr/bin/env python


start = int(raw_input("Please enter the start:"))
end = int(raw_input("Please enter the end:"))

original_list = []
squares_list = []
cubes_list = []

original_list = range(start,end+1)

for i in range(0,(end-start)+1):
    original_list[i] = start
    start +=1


while (start <= end):
    original_list.append(start)
    start +=1

print original_list

for i in range (0,len(original_list)):
    squares_list.append(original_list[i] ** 2)
    cubes_list.append(original_list[i] ** 3)

print squares_list
print cubes_list

start = int(raw_input("Please enter the start of the slice:"))
end = int(raw_input("Please enter the end of the slice:"))

print original_list[start:end]
print squares_list[start:end]
print cubes_list[start:end]


