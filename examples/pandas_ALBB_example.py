#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


# Read the csv file into a pandas dataframe
bbdf = pd.read_csv("./ALbb.salaries.2003.formattted.csv")

# The file has no column headers, so we set them manually.
bbdf.columns=["Team Name","Player Name","Salary","Position"]

# Here we print the data frame
#print bbdf


# Group the data by team name

groupeddf = bbdf.groupby("Team Name").aggregate(sum).dropna().sort('Salary',ascending=False)
#print groupeddf


# Plot output as a bar chart

teamplot = groupeddf.plot(kind="bar")
teamplot.set_title("Salaries for American League Baseball teams in 2003")
teamplot.set_ylabel("Salary in USD (tens of millions)")
plt.yticks(np.arange(0,150000000,10000000))
plt.show()
