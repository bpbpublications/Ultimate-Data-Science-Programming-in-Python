import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd
diamonds_datset = mysns.load_dataset('diamonds')
print(diamonds_datset.head(10))
print('-'*50)
# using pivot_table function for converting into a format useful for analysis
mydiamonds= mypd.pivot_table(data=diamonds_datset, index='cut', columns='color', values='depth')
print(mydiamonds)
print('-'*50)
# we will be having a heatmap that has transformed the numerical values in the mydiamonds
# dataframe into different colors
# print(help(mysns.heatmap))
mysns.heatmap(data = mydiamonds)
myplt.title('diamonds data')
myplt.ylabel('cut') # The index values from Ideal to Fair are used as y tick labels
myplt.xlabel('color') # The column names .i.e. color are used as x tick labels
myplt.show()
# heatmap will use dark colors to display low values . i.e. values below 61.5 are represented with dark colors
# values from 63.5, 64 and 64.5 are represented with light colors