import pandas as mypd
mydf = mypd.read_csv('sample_dropna.csv')
mydf.dropna(inplace=True)
print(mydf)
