import pandas as mypd
mydf = mypd.read_csv('sample_dropna.csv')
mydf1 = mydf.dropna(how='all')
print(mydf1)
