import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd
diamonds_datset = mysns.load_dataset('diamonds')
# using pivot_table function for converting into a format useful for analysis
mydiamonds= mypd.pivot_table(data=diamonds_datset, index='cut', columns='color', values='depth')
mysns.heatmap(data = mydiamonds, vmin=50, vmax=80,annot=True, fmt='0.2f',linewidth=0.4)
myplt.title('diamonds data')
myplt.ylabel('cut')
myplt.xlabel('color')
myplt.show()
