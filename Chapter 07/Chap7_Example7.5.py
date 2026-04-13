import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist)
#print(help(mypd.RangeIndex))
mypd_series.index = mypd.RangeIndex(start=6, stop=11, step=1)
print(mypd_series)