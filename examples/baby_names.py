#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here we create our simple data

names = ['Bob','Jessica','Mary','John','Mel']
births=[968,155,77,578,973]


# Use the zip() function to merge the two lists

BabyDataSet = zip(names,births)

#print BabyDataSet

babydf = pd.DataFrame(BabyDataSet)
babydf.columns=["Name","Births"]

#print babydf

# Raw data from dataframe
#print babydf.values,"\n"



# Let's find the most popular baby name (i.e. highest number of births)

# Method 1.  Use the sort feature of python

SortedBabyDF = babydf.sort(['Births'],ascending=False)
#print "Method 1 of getting the top birth name"
#print SortedBabyDF.head(1)  # Print only the first line

# Method 2.  Use the max() method from the dataframe object

#print "Method 2 of getting the top birth name"
#print "\n",babydf['Births'].max(),"\n"


# Let's plot the dataframe in a graph

babydf['Births'].plot()


MaxValue = babydf['Births'].max()
MaxName = babydf['Name'][babydf['Births'] == babydf['Births'].max()].values
Text = str(MaxValue) + " - " + MaxName

plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')

print "The most popular name", babydf[babydf['Births'] == babydf['Births'].max()]
plt.show()
