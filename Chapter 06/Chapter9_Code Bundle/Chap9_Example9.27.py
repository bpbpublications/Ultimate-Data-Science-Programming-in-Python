import pandas as mypd
mypd_dataframe = mypd.read_csv('df_string_eg.csv')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# expand=True --> To get dataframe object otherwise series object containing list of strings get(0) --> 0th column value
mypd_dataframe.insert(loc=1, column='myfirstname', value =mypd_dataframe['myname'].str.strip().str.split(expand=True).get(0).str.title())
# get(1) --> 1st column value
mypd_dataframe.insert(loc=2, column='mysecondname', value =mypd_dataframe['myname'].str.strip().str.split(expand=True).get(1).str.title())
del mypd_dataframe['myname']
print(mypd_dataframe)