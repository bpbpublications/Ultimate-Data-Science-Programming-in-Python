import pandas as mypd
mydf = mypd.read_csv('filter_eg.csv').dropna()
print(mydf)# displaying 1st dataframe
print('-'*50) 
mydf2 = mypd.read_csv('AQI_eg.csv')
print(mydf2)# displaying 2nd dataframe
print('-'*50) 
# selecting city name whose AQI > 105
myaqi = mydf2['AQI']>105
print(mydf2[myaqi])
print('-'*50)
print(mydf2[myaqi]['City'])
myaqicity = mydf2[myaqi]['City']
print('-'*50)
# selecting employee name who are residing in cities whose AQI > 105
myemp = mydf['City'].isin(myaqicity)
print(mydf[myemp]['Employee Name']) # getting the employee name only