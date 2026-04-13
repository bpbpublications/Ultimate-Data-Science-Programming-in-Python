import pandas as mypd
mydict = {'myname': ['Alex', 'John', 'Michael', 'Tom'],
        'myage': [35, 45, 55, 65],
        'mycountry': ['UK', 'USA', 'Australia', 'Finland']}
mypd_dataframe = mypd.DataFrame(mydict)
print(mypd_dataframe)
print('-'*50)
# modifying the mycountry of the second row
mypd_dataframe.loc[1, 'mycountry'] = 'Russia'
print(mypd_dataframe)
print('-'*50)
# adding a new column to the DataFrame
mypd_dataframe['Hobby'] = ['Playing Cricket', 'Listening Music', 'Reading Books', 'Cooking']
print(mypd_dataframe)
print('-'*50)
# dropping the Hobby column from the DataFrame
my_df_drop = mypd_dataframe.drop(columns=['Hobby'])
print(my_df_drop)
print('-'*50)
# sorting the DataFrame by myname in descending order
my_df_sort = mypd_dataframe.sort_values(by='myname', ascending=False)
print(my_df_sort)
