#!/usr/bin/env python

import pandas as pd


bacteria_series = pd.Series([632,1638,569,115],
                            index = ['Firmicutes','Proteobacteria','Actinobacteria','Bacteroidetes'])


print bacteria_series


print bacteria_series['Actinobacteria']
print "\n"

print "Print all elements of the bacteria_series that ends with the string 'bacteria'"
print bacteria_series[[name.endswith('bacteria') for name in bacteria_series.index]]



print "Tell me which of the elements of bacteria_series ends with 'bacteria'"
print [name.endswith('bacteria') for name in bacteria_series.index]




print "We can still use positional indexing with series"

print bacteria_series[2]


print "Here we give the data and the index a meaningful label"

bacteria_series.name = 'counts'
bacteria_series.index.name = "phylum"


print "Let's find all data values greater than 1000"

print sum(bacteria_series[bacteria_series > 1000])

print "Description of bacteria_series"
print bacteria_series.describe()




