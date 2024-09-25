import pandas as mypd
mypd_dataframe = mypd.read_csv('text_eg.csv')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# Converting all the names in upper case
mypd_dataframe['myname'] = mypd_dataframe['myname'].str.upper()
print(mypd_dataframe)
print('-'*50)
# Replacing '$' with 'Rs' in salary column
mypd_dataframe['mysalary'] = mypd_dataframe['mysalary'].str.replace('$','Rs')
print(mypd_dataframe)
print('-'*50)
# Replacing middle spaces with underscore symbol in myname
mypd_dataframe['myname'] = mypd_dataframe['myname'].str.strip().str.replace(' ','_')
print(mypd_dataframe)
print('-'*50)
# Converting mysalary column to float type and dividing by 10000 and adding 'K' unit
mypd_dataframe['mysalary'] = (mypd_dataframe['mysalary'].str.replace('Rs','').astype(float)/1000).astype(str) + 'K'
print(mypd_dataframe)
