import pandas as mypd
mydf = mypd.read_csv('sample_fillna.csv')
# print(help(mydf.fillna))
print(mydf)
print('-'*50)
mydf1 = mydf.fillna(0) # replace/fill missing value with 0
print(mydf1)
print('-'*50)
# But replacing missing values with 0 is not meaningful
# Recommended to provide meaningful values on missing positions
# Based on column data type we can provide different fill values for different columns
# Now, we will be replacing every missing value of salary column with 20000
mydf['Salary'].fillna(20000, inplace=True)
print(mydf)
print('-'*50)
# Fill Employee Name with 'Dummy' value
mydf['Employee Name'].fillna('Dummy', inplace=True)
print(mydf)