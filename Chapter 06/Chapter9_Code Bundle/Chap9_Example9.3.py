import pandas as mypd
mypd_dataframe = mypd.read_csv('loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# row selection with the matched index label --> single row associated so series object
print(mypd_dataframe.loc['Divya'])
print('-'*50)
# now multiple rows associated with the index specified ---> we are getting dataframe object
print(mypd_dataframe.loc['Saurabh'])
print('-'*50)
# unmatched index ---> KeyError
print(mypd_dataframe.loc['Johnny'])
