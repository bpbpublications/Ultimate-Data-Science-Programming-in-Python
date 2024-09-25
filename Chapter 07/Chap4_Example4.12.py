import pandas as mypd
# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist)
print(mypd_series[[True, False, True, False, True]])
print(mypd_series.iloc[[True, False, True, False, True]])
print(mypd_series.loc[[True, False, True, False, True]])
print(mypd_series.get([True, False, True, False, True]))

