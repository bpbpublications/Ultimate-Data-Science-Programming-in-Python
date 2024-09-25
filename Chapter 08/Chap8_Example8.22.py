import pandas as mypd
mydf = mypd.read_csv('rank_eg.csv').dropna()
print(mydf)
print('-'*50)
mydf['SalaryRank'] = mydf['Salary'].rank(ascending=False)# Highest salary has rank 1.0
mydf.sort_values(by='SalaryRank',inplace=True)
print(mydf)