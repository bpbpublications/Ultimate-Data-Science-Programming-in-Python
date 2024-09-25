import pandas as mypd
mydf = mypd.read_csv('sample_axis.csv')
print(mydf)
print('-'*50)
mydf1 = mydf.dropna(axis=1) # if 'Salary' has missing value, then only row will be deleted.
print(mydf1)
