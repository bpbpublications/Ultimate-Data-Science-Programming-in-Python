import pandas as mypd

# creating a Pandas Series from a dictionary
mydict = {'key1':1, 'key2':2, 'key3':3, 'key4':4, 'key5':5}
mypd_series = mypd.Series(mydict)
print(mypd_series)
