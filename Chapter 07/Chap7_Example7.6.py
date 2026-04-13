import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series_float = mypd.Series(mylist, dtype='float')
# assigning name to the series
mypd_series_float.name = "Series name"
# assigning name to the indexes
mypd_series_float.index.name = "Index name"
print(mypd_series_float)