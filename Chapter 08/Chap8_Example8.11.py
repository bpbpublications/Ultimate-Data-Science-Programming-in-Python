import pandas as mypd
mydf = mypd.read_csv('Arithmetic_Example.csv')
print(mydf)
print('-'*50)
print("Addition:------------------")
print(mydf['Salary'].add(1000)) # print(mydf['Salary']+ 1000) 1000 is broadcasted to every value of the series
print("Subtraction:------------------")
print(mydf['Salary'].sub(1000))
print("Multiplication:------------------")
print(mydf['Salary'].mul(1000))
print("Division:------------------")
print(mydf['Salary'].div(1000))
