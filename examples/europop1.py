#!/usr/bin/env python

import sys

try:
    f = open ("Eur.pop.XL.zip")
except IOError:
    print ("ERROR:  Unable to open file!")
    sys.exit()

countrydata=  {}

# Skip the first three lines.  They're header information that we don't need.

for i in range (0,3):
    try:
        f.readline()
    except IOError:
        print "I got an IOError!"
        f.close()
        sys.exit()



# Now start reading the data from the file.  Build a list containing the tuple 
# (countryname,population delta)


countrydata = {data[0],data[7] - data [1]  for data in line.strip().split(',') if 'Sources' not in line} 

country_dictionary = {country_data[0]:country_data[7] -country_data[1] for country_data in .strip().split(",") in f if country_ 
for record in f:
    countrylist = record.strip().split(",")
    if len(countrylist[0]) == 0 or "Sources:" in countrylist[0]:
        continue
    countrydata[countrylist[0]] = int(countrylist[7]) - int (countrylist[1])
 #   countrydata.append((countrylist[0],int(countrylist[7]) - int(countrylist[1])))

usercountry = raw_input("Please enter the country: ")
print "For country ",usercountry," the population delta is: ",countrydata[usercountry]
