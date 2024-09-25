import pandas as mypd
mydf = mypd.read_csv('student.csv')
#print(help(mydf.sample))
print(mydf.sample()) # random data will be displayed to the console
# Using 'n' parameter to get multiple sample records
print('-'*50)
print(mydf.sample(n=2)) # everytime 2 different records
# Using 'frac' parameter to get specified fraction of random records from total
print('-'*50)
print(mydf.sample(frac=.2)) # 20% of total