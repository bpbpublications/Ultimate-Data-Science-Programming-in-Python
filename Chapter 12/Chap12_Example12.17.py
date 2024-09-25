import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd

diamonds_dataset = mysns.load_dataset('diamonds')
# Use pivot_table function for converting into a format useful for analysis
mydiamonds = mypd.pivot_table(data=diamonds_dataset, index='cut', columns='color', values='depth')
# Define a custom color palette ranging from dark blue to light blue
colors = mysns.color_palette("Blues", as_cmap=True)
# Plot the heatmap with the custom color palette
mysns.heatmap(data=mydiamonds, center=mydiamonds.loc['Good', 'H'], cmap=colors, annot=True, fmt="0.2f")
myplt.title('Diamonds Data')
myplt.ylabel('Cut')
myplt.xlabel('Color')
myplt.show()