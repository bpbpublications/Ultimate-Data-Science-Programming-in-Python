import pandas as mypd
mydf = mypd.read_csv('rank_eg.csv').dropna()
#print(help(mydf['Salary'].rank))
print(mydf['Salary'])
print('-'*50)
print(mydf['Salary'].rank()) # least salary has rank 1.0 in ascending order
print('-'*50)
print(mydf['Salary'].rank(ascending=False)) # Highest salary has rank 1.0