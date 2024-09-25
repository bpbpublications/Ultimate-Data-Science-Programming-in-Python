import pandas as mypd
mydf = mypd.read_csv('sorting_example2.csv')
print(mydf)
print('-'*50)
mydf.sort_values(by = ['Employee Name','Salary'], inplace=True , ascending=False) # by default ascending order so sorting in descending order
print(mydf)