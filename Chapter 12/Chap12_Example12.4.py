import seaborn as mysns
import matplotlib.pyplot as myplt
mysns_dset = mysns.load_dataset('planets')
mysns.set(style='white',context='talk',rc={'axes.edgecolor': 'g','axes.titlesize': 10.0})
mysns.scatterplot(x='mass',y='distance',data=mysns_dset)
myplt.title('talk context')
myplt.show()