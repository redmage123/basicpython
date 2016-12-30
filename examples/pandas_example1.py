#!/usr/bin/env python

import pandas as pd
import sys


# Create a small dataset
d = [0,1,2,3,4,5,6,7,8,9]

# Put the dataset into a Pandas dataframe
df = pd.DataFrame(d)
print df

# Change the column name

df.columns = ['Rev']
print df


# Add a new column

df['NewCol'] = 5
print df


# Modify the new column

df['NewCol'] = df['NewCol'] + 1
print df


# Now let's delete the new column

del df['NewCol']

#Add a couple of new colunns
df ['test'] = 3
df['col'] = df['Rev']


# Let's change the dataframe index from 0-9 to a-j

ilist = ['a','b','c','d','e','f','g','h','i','j']
df.index = ilist

print df

print df.loc['a']

# Let's take a slice of the dataframe...

print df.loc['a':'d']











