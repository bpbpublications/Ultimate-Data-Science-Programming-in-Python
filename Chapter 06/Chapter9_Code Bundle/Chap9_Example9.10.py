import pandas as mypd
mypd_dataframe = mypd.read_csv('rename_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# Usage of index parameter ----------
mypd_dataframe.rename(index={'Saurabh':'Yathartha', 'Nilesh':'Ramesh'},  inplace=True)
print(mypd_dataframe)