import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.apply))
print(mypd_dataframe)
print('-'*50)
# tripling the salary of each name using series apply method since we are selecting a column
mypd_dataframe['mysalary'] = mypd_dataframe['mysalary'].apply(lambda sal: sal*3)
print(mypd_dataframe)
print('-'*50)
# Now, tripling the salary of country with 'India' using dataframe apply method
def india_triple_salary(myrow):
    mycountry = myrow[2]
    mysalary = myrow[3]
    if mycountry == 'India':
        myrow[3] = mysalary * 3
    return myrow # multiple columns data is returned so dataframe
print(mypd_dataframe.apply(india_triple_salary, axis='columns')) # to apply function row wise we have to use axis='columns' 
