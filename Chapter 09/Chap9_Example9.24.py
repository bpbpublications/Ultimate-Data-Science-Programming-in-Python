import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.where))
print(mypd_dataframe)
print('-'*50)
# if salary of the concerned person is more than 45000, we will replace it with 'Upper limit'
mypd_dataframe['mysalary'] = mypd_dataframe['mysalary'].where(lambda x: x<=45000, other='Upper limit')
print(mypd_dataframe)