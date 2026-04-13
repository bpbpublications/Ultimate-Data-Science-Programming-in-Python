import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.nlargest))
# print(help(mypd_dataframe.nsmallest))
print(mypd_dataframe)
print('-'*50)
# finding 4 highest salaried names information
print(mypd_dataframe.nlargest(n=4, columns=['mysalary']))
print('-'*50)
# finding 4 lowest salaried names information
print(mypd_dataframe.nsmallest(n=4, columns=['mysalary']))