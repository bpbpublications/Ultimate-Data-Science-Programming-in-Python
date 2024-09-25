import pandas as mypd
mydf = mypd.read_csv('duplicated_eg.csv')
# print(help(mydf.drop_duplicates))
mydf.drop_duplicates(inplace=True) # not talking about a particular but all the columns
print(mydf)
print('-'*50)
# to delete records if Employee Name column is duplicated. 
# Except first occurrence of Employee Name, every row will be deleted for duplicate Employee Name
mydf.drop_duplicates(subset=['Employee Name'], inplace=True) 
print(mydf)
