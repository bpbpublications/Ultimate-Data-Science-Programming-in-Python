import pandas as mypd
# Transforming series object without using update method
# we can update a particular element using normal indexing or loc/iloc indexers
mypd_series = mypd.Series([15,30,45,60])
mypd_series[1] = 25 
mypd_series[2] = 55 
print(mypd_series)
# Obs: We can see that we are using 'n' lines of code, in order to update 'n' elements

# Transforming series object without using update method
mypd_series2 = mypd.Series([15,30,45,60])
mypd_series2.update(mypd.Series([25,55], index=[1,2]))
print(mypd_series2)
#print(help(mypd_series2.update))