import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# to select all names where country is neither 'India' nor 'UK'
mypd_dataframe.query(" mycountry not in [ 'India', 'UK'] ", inplace=True)
print(mypd_dataframe)
