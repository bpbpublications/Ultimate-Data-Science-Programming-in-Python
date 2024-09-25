import pandas as mypd
mydf = mypd.read_csv('employees_salary2.csv')
# print(help(mydf.insert))
print(mydf)
print('-'*50)
mydf.insert(1,'City',['Durg','Raipur','Bhilai'])
print(mydf)
print('-'*50)
# ValueError
mydf.insert(1,'City',['Hyderabad','Bhopal','Indore']) # if allow_duplicates = True, then new column City will be added
print(mydf)