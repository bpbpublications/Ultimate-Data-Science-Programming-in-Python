import pandas as mypd
mypd_dataframe = mypd.read_csv('cell_loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
print(mypd_dataframe.loc['Saurabh','mycountry'])
print('-'*50)
print(mypd_dataframe.loc['Saurabh','mycountry'].iloc[1] )# Value of only 1 column
print('-'*50)
print(mypd_dataframe.loc[['Mintoo','Priyanka'],['mycountry','mysalary']]) # will return rows with more than 1 column
print('-'*50)
print(mypd_dataframe.iloc[1,0])
print('-'*50)
print(mypd_dataframe.iloc[[1,3],[0,2]]) # accessing 1st and 3rd row and 0th, 2nd column data 
print('-'*50)
print(mypd_dataframe.iloc[2:,:2]) # from 2nd index to last, from 0th index to 1st index column
