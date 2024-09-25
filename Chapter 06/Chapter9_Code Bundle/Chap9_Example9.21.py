import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv')
mypd_dataframe.sort_index(inplace=True)
# print(help(mypd_dataframe.apply))
print(mypd_dataframe)
print('-'*50)
# Now, tripling the salary of country with 'India' using dataframe apply method
def designation_func(myrow):
    mysalary = myrow[3]
    if mysalary <25000:
        return 'Worker'
    elif mysalary <35000:
        return 'Artisan'
    elif mysalary <45000:
        return 'DGM'
    elif mysalary <55000:
        return 'AGM'
    else:
        return 'GM'
mypd_dataframe['MyDesignation'] = mypd_dataframe.apply(designation_func, axis='columns') # appltying func row wise
print(mypd_dataframe)
