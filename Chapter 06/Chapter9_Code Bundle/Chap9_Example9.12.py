import pandas as mypd
mypd_dataframe = mypd.read_csv('rename_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.drop))
print(mypd_dataframe)
print('-'*50)
# to delete rows where index label is 'Saurabh' ---> all will generate the same output. Uncomment it and then check
# mypd_dataframe.drop(labels='Saurabh', inplace=True)
# mypd_dataframe.drop(labels='Saurabh',axis=0, inplace=True)
# mypd_dataframe.drop(labels='Saurabh',axis='index', inplace=True)
# mypd_dataframe.drop(labels='Saurabh',axis='rows', inplace=True)
mypd_dataframe.drop(index='Saurabh', inplace=True)
print(mypd_dataframe)
print('-'*50)
# to delete rows where index label is either 'Mintoo' or 'Nilesh'
# This will also generate the same output
mypd_dataframe.drop(index=['Mintoo','Nilesh'], inplace=True)
# mypd_dataframe.drop(labels=['Mintoo','Nilesh'], inplace=True)
print(mypd_dataframe)