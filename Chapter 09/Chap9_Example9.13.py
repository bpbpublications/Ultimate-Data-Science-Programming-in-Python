import pandas as mypd
mypd_dataframe = mypd.read_csv('rename_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.drop))
print(mypd_dataframe)
print('-'*50)
# to delete column name = 'myage'
mypd_dataframe.drop(labels='myage',axis=1, inplace=True)
# This will generate the same output
# mypd_dataframe.drop(columns='myage', inplace=True)
print(mypd_dataframe)
# By using pop method : we can delete only column at a time
print('-'*50)
mypd_dataframe.pop('mycountry')
print(mypd_dataframe)
# By using del keyword
del mypd_dataframe['mysalary']
print('-'*50)
print(mypd_dataframe)