import pandas as mypd
mydf = mypd.read_csv('filter_eg.csv').dropna()
# print(help(mydf['City'].between))
# select range of values between 100000 and 160000 without using between method
mycond1 = mydf['Salary'] >= 100000
mycond2 = mydf['Salary'] <= 160000
print(mydf[mycond1 & mycond2])
print('-'*50) 
# select range of values between 100000 and 150000 using between method
print(mydf[mydf['Salary'].between(100000,150000)]) # by default inclusive = both
print('-'*50) 
# select range of values between >=100000 and <150000 (150000 is exclusive) using between method
print(mydf[mydf['Salary'].between(100000,150000, inclusive='left')])
print('-'*50) 
# select range of values between >100000 and <=150000 (100000 is exclusive) using between method
print(mydf[mydf['Salary'].between(100000,150000, inclusive='right')])
print('-'*50) 
# select range of values between >100000 and <=150000 (both 100000 and 150000 are exclusive) using between method
print(mydf[mydf['Salary'].between(100000,150000, inclusive='neither')])