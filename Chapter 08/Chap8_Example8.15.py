import pandas as mypd
mydf = mypd.read_csv('sample_fillna.csv')
mydf.dropna(inplace=True) 
print(mydf)
print(mydf.info())
print('-'*50)
mydf['Salary']=mydf['Salary'].astype('int')
print(mydf) # int type
print(mydf.info())