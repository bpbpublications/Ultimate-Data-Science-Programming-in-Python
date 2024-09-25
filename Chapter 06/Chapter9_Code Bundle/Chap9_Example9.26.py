import pandas as mypd
mypd_dataframe = mypd.read_csv('df_string_eg.csv')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# to filter all row names which starts with letter 'S'
mycond = mypd_dataframe['myname'].str.startswith('S') # case sensitive
print(mypd_dataframe[mycond])
print('-'*50)
# to filter all row names which ends with letter 'r'
mycond = mypd_dataframe['myname'].str.endswith('r') # case sensitive
print(mypd_dataframe[mycond])
print('-'*50)
# to filter all row names which contains 'y' (lower case)
mycond = mypd_dataframe['myname'].str.contains('y') # case sensitive
print(mypd_dataframe[mycond]) # Here Yathartha was not displayed since it starts with UpperCase 'Y'
print('-'*50)
# if we want case insensitive data use case parameter
mycond = mypd_dataframe['myname'].str.contains('y',case=False) # case insensitive
print(mypd_dataframe[mycond]) # Here Yathartha will also be displayed since it starts with UpperCase 'Y'
