import pandas as mypd
mydf = mypd.read_csv('sorting_example2.csv')
# print(help(mydf.sort_index))
print(mydf)
print('-'*50)
# sorting based on ascending order of Employee Name
mydf.sort_values(by ='Employee Name', inplace=True )
print(mydf)
print('-'*50)
# sorting based on descending order of index
mydf.sort_index(ascending=False, inplace=True )
print(mydf)