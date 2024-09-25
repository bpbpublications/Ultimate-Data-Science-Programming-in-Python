import pandas as mypd
mydf = mypd.read_csv('sample_dropna.csv')
mydf1 = mydf.dropna(subset=['Salary']) # if 'Salary' has missing value, then only row will be deleted.
print(mydf1)
print('-'*50)
mydf2 = mydf.dropna(subset=['Location', 'Salary']) # if either 'Location' or 'Salary' has missing value, then only row will be deleted.
print(mydf2)