import pandas as mypd
mydf = mypd.read_csv('unique_eg.csv', index_col = "Employee Name")
#print(help(mydf.reset_index)) # Employee Name acts as index column
print(mydf)
print('-'*50)
# Employee Name column will be deleted
mydf.reset_index(drop=True, inplace=True)
print(mydf)