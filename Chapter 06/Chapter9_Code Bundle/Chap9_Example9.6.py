import pandas as mypd
mypd_dataframe = mypd.read_csv('loc_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
print(mypd_dataframe)
print('-'*50)
# Syntax-1:
print(mypd_dataframe.iloc[1]) # returns 2nd row in the form of series object
# You please uncomment it and then try the below code
#print(mypd_dataframe.iloc[10]) # returns IndexError: single positional indexer is out-of-bounds
print('-'*50)
# Syntax-2:
print(mypd_dataframe.iloc[1:4]) # returns rows from 1st index position to 3rd index position
print('-'*50)
# Syntax-3:
print(mypd_dataframe.iloc[[1,2,4]]) # returns rows present at indexes 1,2,4
print(mypd_dataframe.iloc[[1,2,9]]) # returns IndexError