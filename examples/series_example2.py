#!/usr/bin/env python


import pandas as pd

loss_series = pd.read_table("lost_revenue.dat",header=False)
print loss_series
