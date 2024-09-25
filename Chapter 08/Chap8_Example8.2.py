import pandas as mypd
import numpy as mynp
mydf = mypd.read_csv('student.csv')
print(mydf.dtypes)
print(mydf.dtypes.value_counts())

# column names
# dataframe creation using ndarray
myndarray = mynp.array([[1,2,3],[4,5,6],[7,8,9]])
mydf2 = mypd.DataFrame(myndarray)
print(mydf2) # with default column names 0 1 and 2
print('-'*50)
mydf3 = mypd.DataFrame(myndarray, columns=["a","b","c"])
print(mydf3)
print(mydf3.columns) # index object containing column names
print('-'*50)
# axes
print(mydf3.axes) # list of axes object is returned [rowindex, columnindex]