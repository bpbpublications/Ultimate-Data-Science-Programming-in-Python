import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.where))
print(mypd_dataframe)
print('-'*50)
# to return full dataframe we will be using where() method
mycond = mypd_dataframe['mycountry'] == 'India'
print(mypd_dataframe.where(mycond))