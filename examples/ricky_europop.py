#!/usr/bin/env python3
fhand = open('Eur.pop.XL.zip.csv')
data = {}

foo = fhand.read()
print ("Foo = " + foo)
fhand.read()
fhand.read()

for line in fhand:
    print (line)
    if line == '':
        break
    record = line.strip().split(',')
    print (record)
    data[record[0]] = record[7] - record[1]

fhand.close() 
print (data) 
country = input('Please enter country: ')
if country in data:
    print (data[country])
else:
    print ('No such country')

