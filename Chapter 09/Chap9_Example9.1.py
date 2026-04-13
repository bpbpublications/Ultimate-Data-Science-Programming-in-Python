import pandas as mypd
mydf = mypd.read_csv('unique_eg.csv')
print(mydf)
print('-'*50)
# Approach-1
mydf1 = mypd.read_csv('unique_eg.csv', index_col = "Employee Name")
print(mydf1)
print('-'*50)
# Approach-2
# print(help(mydf1.set_index))
mydf.set_index(keys='Employee Name', inplace=True)
print(mydf)
