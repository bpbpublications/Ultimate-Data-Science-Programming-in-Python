import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
mypd_dataframe.query(" mycountry == 'India' ", inplace=True)
print(mypd_dataframe)