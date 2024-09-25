import pandas as mypd
mydf = mypd.read_csv('sorting_example.csv')
# print(help(mydf.sort_values))
print(mydf)
print('-'*50)
mydf.sort_values(by = 'Salary', inplace=True , ascending=False) # by default ascending order so sorting in descending order
print(mydf)
print('-'*50)
# sorting values based on reverse of alphabetical order of City column 
mydf2 = mydf.sort_values(by = "City", ascending=False)
print(mydf2)
print('-'*50)
# By default NaN came at last position. But suppose we want to place NAs at first, we will be using na_position = 'first'
mydf3 = mydf.sort_values(by = "City", ascending=False, na_position='first')
print(mydf3)