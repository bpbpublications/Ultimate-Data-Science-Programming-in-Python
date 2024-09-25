import pandas as mypd
mydf = mypd.read_csv('unique_eg.csv')
# Displaying list of unique values
print(mydf['Employee Name'].unique())
# Displaying no. of unique values excluding NaN
print(mydf['Employee Name'].nunique())
# Displaying no. of unique values including NaN
print(mydf['Employee Name'].nunique(dropna=False))