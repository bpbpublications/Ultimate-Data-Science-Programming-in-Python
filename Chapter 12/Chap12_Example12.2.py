import seaborn as mysns
import matplotlib.pyplot as myplt
# print(help(mysns.load_dataset))
# axes_style() returns a dictionary of rc parameters containing the current style settings for seaborn plots. 
print(mysns.axes_style())
'''
using set_style() sets the plot theme with default theme as darkgrid
The other themes available are whitegrid, dark, white and ticks
'''
print('-'*50)
mysns_dset = mysns.load_dataset('geyser') # EG2_T1
print(mysns_dset.head())# EG2_T2
mysns.set_style(style='ticks',rc={'axes.edgecolor': 'r','text.color': 'g','xtick.color': 'b','ytick.color': 'y'})# EG2_T3
mysns.scatterplot(x = 'duration',y ='waiting',data=mysns_dset)# EG2_T4
myplt.title('Selecting Ticks theme')# EG2_T5
myplt.show()# EG2_T6