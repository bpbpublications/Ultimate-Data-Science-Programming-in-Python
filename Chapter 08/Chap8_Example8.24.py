import pandas as mypd
mydf = mypd.read_csv('filter_eg.csv').dropna()
print(mydf[mydf['City'].isin(['Hyderabad','Durg','Lara'])])