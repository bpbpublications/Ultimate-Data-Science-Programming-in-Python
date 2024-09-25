import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])

# element access using index label
print(mypd_series['u'])

# element access using integer location
print(mypd_series[3])
