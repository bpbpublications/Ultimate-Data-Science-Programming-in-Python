import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])

# Minimum value calculation of the Series
print(f" Minimum value is: {mypd_series.min()}")
# Maximum value calculation of the Series
print(f" Maximum value is: {mypd_series.max()}")
# Calculating the sum of the Series
print(f" Sum is: {mypd_series.sum()}")
# Calculating the mean of the Series
print(f" Mean is: {mypd_series.mean()}")
# Calculating the median of the Series
print(f" Median is: {mypd_series.median()}")
