import pandas as mypd
mypd_dataframe = mypd.read_csv('loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
print(mypd_dataframe.loc[['Mintoo','Nilesh','Priyanka']])
print('-'*50)
# KeyError since Nivesh is unavailable
print(mypd_dataframe.loc[['Mintoo','Nilesh','Priyanka','Nivesh']])