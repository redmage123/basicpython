#!/usr/bin/env python

import json

# This program will, given a user input of a year that the olympic games
# were run, will dump a json dictionary object containing the following:
# key => Countryname, Value=> total medals won by the country for that year

athelete_dict = {}

# As usual, we open the data source. 
f = open("athelete_data_subset",'r+')

# The first line is header information, so let's skip that. 
f.readline()


# Let's ask the user to enter an olympic year.  Note we're not doing
# any validation on this, which is bad, but this program is really just
# showing the core concepts. 

year = raw_input("Please enter the year you want: ")


# Let's iterate over the data source.  We break up the string into a list
# using strip().

# Then we build our dictionary.  Note that if the key doesn't exist
# we have to create it first otherwise Python will give a ValueError about
# an undefined key/value pair. 

for data in f:
    athelete_data_list = data.strip().split(",")
    if athelete_data_list[3] == year:
        if not athelete_dict.has_key(athelete_data_list[2]):
            athelete_dict[athelete_data_list[2]]= 0
        athelete_dict[athelete_data_list[2]] += int(athelete_data_list[9])

# Now close the file and re-use the 'f' variable for our output 
# file descriptor. 

f.close()
f = open("athelete_data_subset.json","w")

# Dump the dictionary into the output file using 'json.dump()'

json.dump(athelete_dict,f)
 
# Close the output file's file object and we're done. 
f.close()
