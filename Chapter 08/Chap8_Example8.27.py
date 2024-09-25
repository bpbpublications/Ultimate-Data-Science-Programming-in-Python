import pandas as mypd
mydf = mypd.read_csv('isnull_notnull_eg.csv')
print(mydf)
print('-'*50)
# Applying on series object ---------------------------------------
print(mydf['Employee Name'].isnull()) # will return Boolean series
print('-'*50)
print(mydf[mydf['Employee Name'].isnull()]) # selecting rows with True
print('-'*50)
print(mydf['Employee Name'].notnull()) # will return Boolean series
print('-'*50)
print(mydf[mydf['Employee Name'].notnull()]) # selecting rows with True
# Applying on dataframe object ---------------------------------------
print(mydf.isnull())
print('-'*50)
print(mydf.notnull())