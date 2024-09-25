import pandas as mypd
mydf = mypd.read_csv('category_example.csv')
print(mydf.info())
print('-'*50)
mydf['City'] = mydf['City'].astype('category')
print(mydf.info())