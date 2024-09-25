import pandas as mypd
# creating a Pandas Series
mypd_series = mypd.Series(
    data=['Mango','Guava','Pear','Banana','Litchi'], 
    index = [1,2,3,4,5],
    name = '1-D data'
    )
# values
print(mypd_series.values)
print(type(mypd_series.values))
# index
print(mypd_series.index)
# dtype
print(mypd_series.dtype)
# size
print(mypd_series.size)
# shape
print(mypd_series.shape)
# ndim
print(mypd_series.ndim)
# name
print(mypd_series.name)
# is_unique
print(mypd_series.is_unique)
print('-'*50)
mypd_series2 = mypd.Series(
    data=['Mango','Guava','Pear','Banana','Litchi','Pear','Banana', mypd.NA])
print(mypd_series2.is_unique)
print(mypd_series2.nunique())
print(mypd_series2.nunique(dropna=False)) # want to consider NA values also the use dropna argument
# is_monotonic
print('-'*50)
mypd_series3 = mypd.Series([1,2,3,4,5])
mypd_series4 = mypd.Series([5,4,3,2,1])
print(mypd_series3.is_monotonic_increasing)
print(mypd_series3.is_monotonic_decreasing)
print(mypd_series4.is_monotonic_increasing)
print(mypd_series4.is_monotonic_decreasing)
print('-'*50)
# hasnans
mypd_series5 = mypd.Series(['Mango','Guava','Pear','Banana','Litchi','Pear','Banana', mypd.NA])
mypd_series6 = mypd.Series(['Mango','Guava','Pear','Banana','Litchi','Pear','Banana', None])
print(mypd_series.hasnans)
print(mypd_series5.hasnans)
print(mypd_series6.hasnans)