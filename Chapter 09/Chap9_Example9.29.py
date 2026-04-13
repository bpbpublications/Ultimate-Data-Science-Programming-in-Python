import pandas as mypd
mydict = {
    'myname': ['Alex', 'John', 'Michael', 'Tom'],
    'myage': [35, 45, 55, 65],
    'mycountry': ['UK', 'USA', 'Australia', 'Finland']
}
mypd_dataframe = mypd.DataFrame(mydict)
# Convert 'myage' column to numeric data type
mypd_dataframe['myage'] = mypd.to_numeric(mypd_dataframe['myage'], errors='coerce')
print(mypd_dataframe)
print('-' * 50)
# Getting the mean age of the DataFrame
my_mean_age = mypd_dataframe['myage'].mean()
print(my_mean_age)
print('-' * 50)
# Getting the total number of rows in the DataFrame
my_num_row_count = len(mypd_dataframe.index)
print(my_num_row_count)
print('-' * 50)
# Grouping the DataFrame by country and getting the mean age for each group
mygroup = mypd_dataframe.groupby(['mycountry'])['myage'].mean()
print(mygroup)