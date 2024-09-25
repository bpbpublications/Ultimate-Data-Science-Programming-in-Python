import pandas as mypd
# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])

# using iloc---------------------------------------
# print(help(mypd_series.iloc))
print(mypd_series.iloc[1])
print(mypd_series.iloc[[1,3]])
print(mypd_series.iloc[1:3])
print(mypd_series.iloc[-1]) # we are able to access the last item
print('-'*50)
# using loc---------------------------------------
# print(help(mypd_series.loc))
# getting value associated with label 's'
print(mypd_series.loc['s'])
# getting values associated with label 's' and 'u'
print(mypd_series.loc[['s','u']])
# getting values from label 's' to 'u'
print(mypd_series.loc['s':'u'])