import pandas as mypd
import numpy as mynp

# creating a Pandas Series from a numpy array
myndarray = mynp.array([11,12,13,14,15])
mypd_series = mypd.Series(myndarray)
print(mypd_series)
