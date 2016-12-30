#!/usr/bin/env python


import pandas as pd

BacteriaDF = pd.DataFrame({'value':[632,1638,569,115,433,1130,754,555],
                     'patient':[1,1,1,1,2,2,2,2],
                     'phylum':['Firmicutes','Proteobacteria','Actinobacteria','Bacteroidetes','Firmicutes','Proteobacteria','Actinobacteria','Bacteroides']})



print BacteriaDF[['phylum','value','patient']]

print "Printing the columns index"
print BacteriaDF.columns

print "Accessing the 'values' column of BacteriaDF"

print BacteriaDF['value']
