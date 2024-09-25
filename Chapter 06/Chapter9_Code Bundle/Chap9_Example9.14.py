import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.query))
print(mypd_dataframe)
print('-'*50)
mycond = mypd_dataframe['mycountry'] == 'India'
print(mypd_dataframe[mycond])