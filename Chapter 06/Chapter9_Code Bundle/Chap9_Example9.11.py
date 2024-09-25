import pandas as mypd
mypd_dataframe = mypd.read_csv('rename_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# Usage of mapper and axis parameters ----------
mypd_dataframe.rename(mapper={'myage':'my_age', 'mycountry':'my_country'}, axis=1,  inplace=True)
# Also if we write for axis='columns', same output will be generated ---> plz try on your own
print(mypd_dataframe)
print('-'*50)
# By using columns parameter
mypd_dataframe.rename(columns={'mysalary':'my_salary'},  inplace=True)
print(mypd_dataframe)
