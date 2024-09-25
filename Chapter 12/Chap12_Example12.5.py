import seaborn as mysns
import matplotlib.pyplot as myplt
mysns_dset = mysns.load_dataset('planets')
mysns.set(style='ticks')
mysns.scatterplot(x='mass',y='distance',data=mysns_dset)
mysns.despine()
myplt.title('Only Left and Bottom spine')
myplt.show()