import pandas as mypd
# print(help(mypd.read_csv))
mydf = mypd.read_csv('employees_salary.csv')

# we will get a dataframe object here
print('The return type is', type(mydf))
print(mydf)
print('ndim: ', mydf.ndim)

# converting into series object
mydf1 = mypd.read_csv('employees_salary.csv', usecols=['Employee Name'])['Employee Name']
print('The return type is', type(mydf1))
print(mydf1)
print('ndim: ', mydf1.ndim)