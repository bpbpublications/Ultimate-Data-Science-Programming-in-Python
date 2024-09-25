import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd
import numpy as mynp
diamonds_dataset = mysns.load_dataset('diamonds')
mydiamonds = mypd.pivot_table(data=diamonds_dataset, index='cut', columns='color', values='depth')
colors = mysns.color_palette("Blues", as_cmap=True)
mytrildata = mynp.tril(mydiamonds)
print(mytrildata)
# values will be plotted for the cells where mask is False .i.e. 0
mysns.heatmap(data=mydiamonds, cmap=colors, annot=True, fmt="0.2f", cbar_kws={'orientation':'horizontal'}, mask=mytrildata)
myplt.title('Diamonds Data')
myplt.ylabel('Cut')
myplt.xlabel('Color')
myplt.show()