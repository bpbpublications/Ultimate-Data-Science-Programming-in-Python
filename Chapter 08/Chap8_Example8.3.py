import pandas as mypd
# complete information of dataframe is displayed
mydf = mypd.read_csv('student.csv', index_col = ['id'])
print(mydf.info())
print('-'*50)
# verbose=False
print(mydf.info())
# verbose=False, memory_usage=False
print('-'*50)
print(mydf.info(verbose=False, memory_usage=False))
# show_counts=False
print('-'*50)
print(mydf.info(show_counts=False))