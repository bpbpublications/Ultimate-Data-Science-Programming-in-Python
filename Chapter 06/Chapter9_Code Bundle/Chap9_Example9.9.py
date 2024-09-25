import pandas as mypd
mypd_dataframe = mypd.read_csv('rename_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
#print(help(mypd_dataframe.rename))
print(mypd_dataframe)
print('-'*50)
# Usage of mapper and axis parameters ----------
mypd_dataframe.rename(mapper={'Saurabh':'Yathartha', 'Nilesh':'Ramesh'},  inplace=True)
# axis=0 is default value. This will generate the same output for axis='rows' or axis='index ---> plz try on your own
print(mypd_dataframe)