import pandas as mypd
mydf = mypd.read_csv('filter_eg.csv').dropna()
print(mydf) # selecting only City Column
print('-'*50)
print(mydf['City']) # selecting only City Column
print('-'*50)
# Displaying True if City is Durg else will be displaying False
print(mydf['City'] == 'Durg') # boolean series will be returned for boolean masking
print('-'*50)
# selection of all rows where True will be returned
print(mydf[mydf['City'] == 'Durg'])
# we can even use > , >= , < , <= operator also
print("-"*50)
print(mydf[mydf['Salary'] >= 130000])
# filtering data based on multiple conditions using & and | operators also
print("-"*50)
# selecting City as Durg and salary >=120000
mycond1 = mydf['City'] == "Durg"
mycond2 = mydf['Salary'] >= 120000
print(mydf[mycond1 & mycond2])
# selecting employee names which City as Durg and also those employees whose salary >=120000
print("-"*50)
print(mydf[mycond1 | mycond2])