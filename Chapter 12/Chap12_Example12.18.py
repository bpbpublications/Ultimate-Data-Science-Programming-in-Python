import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd
import numpy as mynp
diamonds_dataset = mysns.load_dataset('diamonds')
mydiamonds = mypd.pivot_table(data=diamonds_dataset, index='cut', columns='color', values='depth')
colors = mysns.color_palette("Blues", as_cmap=True)
mytriudata = mynp.triu(mydiamonds)
print(mytriudata)
# where mask is False .i.e. 0 values will be plotted for those cells
mysns.heatmap(data=mydiamonds, cmap=colors, annot=True, fmt="0.2f", cbar_kws={'orientation':'horizontal'}, mask=mytriudata)
myplt.title('Diamonds Data')
myplt.ylabel('Cut')
myplt.xlabel('Color')
myplt.show()