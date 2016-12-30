#!/usr/bin/env python


import urllib2
import operator
import collections

# This is a python program to do the following:
# Give me a list of manufacturers sorted by the average amount of sugar
# in their cereals. 

# Note, it seems as though we're doing a lot of steps with a lot of 
# intermediate data structures (indexdict, outd, etc.) This is because
# we're having to do a lot of stuff manually that something like 
# pandas would do automatically for you.  But you need to be able
# to understand this stuff before you start using advanced libraries
# like numpy and pandas.

# First thing we do, let's read the data in from the web site.

response =urllib2.urlopen("http://lib.stat.cmu.edu/datasets/1993.expo/cereal")


# Now we define our variables
# line_list:  This is the list that will contain the initial data read
# in by the program after it is 'stripped' and 'split'
line_list = []

# Cerealdict contains the data from the file with the key=> Manufacturer
# and the value being the rest of the data (i.e. line_list[1:]
cerealdict = {}

# outd is our dictionary that contains the key => Manufacturer and 
# value => a list containing the sum of the sugar in grams per cereal
# and a count of the number of cereals in the data for that manufacturer.

outd = {"American Home Food Products":[0,0],"General Mills":[0,0],"Kelloggs":[0,0],"Nabisco":[0,0],"Post":[0,0],"Quaker Oats":[0,0],"Ralston Purina":[0,0]}


# Sorted outlist will be a  sorted list of manufacturers and avg. grams of
# sugar
sorted_outd = []

# indexdict is a dictionary that will easily help us translate the one
# character Manufacturer code in to a real company name

indexdict = {"A":"American Home Food Products","G":"General Mills","N":"Nabisco","K":"Kelloggs","P":"Post","Q":"Quaker Oats","R":"Ralston Purina"}

# Now let's read the data we got from the HTTP response object into our 
# cerealdict object. Note that the key/value pairs here are the manufacturer's
# name as the key and everything else as the value

for line in response:
    line_list=line.strip().split()
    cerealdict[line_list[0]] = line_list[1:]


# Now we need to iterate through the dictionary (Hence the 'keys' method)
# and pull the data we want (i.e. the amount of sugar per cereal and 
# a count of the number of cereals in the data.  Note that this is a list
# not a tuple, because we can't modify the tuple later on. 
 

for key in cerealdict.keys():
    outd_key = indexdict[cerealdict[key][0]] 
    outd[outd_key][0] += int(cerealdict[key][8])
    outd[outd_key][1] += 1

# Note here that I'm re-using outd.  I'm iterating over every element
# of outd and changing it from the original  (key => Manufacturer's name 
# value => list containing [sugars][count] to (key => Manufacturer's name
# value => average amount of sugar

for key in outd:
    outd[key] = outd[key][0] / outd[key][1]


# Finally, we need to sort outd by the amount of sugar.  This is the only
# 'new' concept that we haven't discussed, although you can easily find
# this solution on the internet

# The 'sorted' builtin function returns a new sorted list given the old list
# Here we're telling it to sort on the outd values 
# 'key = operator.itemgetter(1) tells sorted to sort on element 1 of the 
# dictionary. outd.items() returns a list of tuples of the key,value
# in the dictionary. I.e. we're getting a list of the "Manufacturer's name
# and the Average amount of sugar in a list that's sorted by the sugar
# (element 1) and sorted it in descending order (reverse = True)

sorted_outlist= sorted(outd.items(),key=operator.itemgetter(1),reverse=True)
print sorted_outlist








