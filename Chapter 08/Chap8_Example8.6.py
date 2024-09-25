import pandas as mypd
mydf = mypd.read_csv('sample_dropna.csv')
#print(help(mydf.dropna))
print(mydf)
print('-'*50)
mydf1 = mydf.dropna()
print(mydf1)
