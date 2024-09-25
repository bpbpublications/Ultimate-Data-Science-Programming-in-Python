import pandas as mypd
mypd_dataframe = mypd.read_csv('cell_loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# changing the value of Nilesh myage to 45 from 43
mypd_dataframe.loc['Nilesh','myage'] = 45
# changing Mintoo and Priyanka salary to 600000 and 30000
mypd_dataframe.loc[['Mintoo','Priyanka'],'mysalary'] = [600000, 30000]
print(mypd_dataframe)
print('-'*50)
# changing [Divya , Priyanka] age to  [42,29] and country to [Russia , France]
mypd_dataframe.loc[['Divya','Priyanka'],['myage','mycountry']] = [[42,'Russia'],[29,'France']]
print(mypd_dataframe)
# replace every occurrence of 30000 to 77777 in myname column
print('-'*50)
mycond = mypd_dataframe['mysalary'] == 30000
# new dataframe is not created and view of the existing dataframe is returned , thus improving memory utlization
mypd_dataframe.loc[mycond,'mysalary'] = 77777 
print(mypd_dataframe)
print('-'*50)
# replacing name having Saurabh row with mycountry as Italy from its salary as 60000 to 99999 
mypd_dataframe.loc[(mypd_dataframe.index == 'Saurabh') & (mypd_dataframe['mycountry'] == 'Italy'), 'mysalary'] = 99999
print(mypd_dataframe)