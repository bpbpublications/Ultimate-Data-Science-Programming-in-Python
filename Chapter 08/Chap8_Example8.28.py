import pandas as mypd
mydf = mypd.read_csv('duplicated_eg.csv')
#print(help(mydf['Employee Name'].duplicated))
print(mydf)
print('-'*50)
# here duplicates will be True except for the first occurrence
print(mydf['Employee Name'].duplicated()) # default value of keep = First
print('-'*50)
# here duplicates will be True except for the last occurrence
print(mydf['Employee Name'].duplicated(keep='last'))
print('-'*50)
# here all duplicates will be True 
print(mydf['Employee Name'].duplicated(keep=False))
print('-'*50)
# select all rows without Employee Name duplicates  
# and consider the Employee Name with only first occurrence if employees are having same name
mycond1 = ~mydf['Employee Name'].duplicated()
print(mydf[mycond1])
print('-'*50)
# select all rows with Employee Name having unique values .i.e. where names are not repeated
mycond2 = ~mydf['Employee Name'].duplicated(keep = False)
print(mydf[mycond2])