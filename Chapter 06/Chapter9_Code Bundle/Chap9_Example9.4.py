import pandas as mypd
mypd_dataframe = mypd.read_csv('loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
print(mypd_dataframe.loc['Mintoo':'Priyanka'])
print('-'*50)
print(mypd_dataframe.loc['Mintoo':'Priyanka':2])
print('-'*50)
# The begin index label is optional and default value is first index label
print('-'*50)
print(mypd_dataframe.loc[:'Priyanka'])
# The end index label is optional and default value is also end index label
print('-'*50)
print(mypd_dataframe.loc['Nilesh':])
# selection all rows
print('-'*50)
print(mypd_dataframe.loc[:])