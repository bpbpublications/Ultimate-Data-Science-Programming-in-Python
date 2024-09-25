import pandas as mypd
mydf = mypd.read_csv('employees_salary2.csv')
print(mydf)
print('-'*50)
# if specified column is already available then old value is replaced with new value
mydf['salary'] = 20000
print(mydf)
print('-'*50)
# now trying to add City Column to the DataFrame object but all the rows under this column
# will have value as Durg
mydf['City'] = "Durg"
print(mydf)
print('-'*50)
# now will add Country Column with different countries to each row . Here there are 3 row values data
# So , 3 different countries we will be providing
mydf['Country'] = ['India','UK','Australia']
print(mydf)
print('-'*50)
# please note that if we are providing only 2 countries name here instead of 3, then we will be
# facing ValueError
mydf['Age'] = [10,20]
print(mydf)