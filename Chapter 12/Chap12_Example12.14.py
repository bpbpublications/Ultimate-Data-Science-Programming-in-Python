import seaborn as mysns
import matplotlib.pyplot as myplt
#print(help(mysns.set_palette))
mycolor_palette = mysns.hls_palette(h=0.5, s=0.6, l=0.4)
mysns.set_palette(mycolor_palette, n_colors=7, desat=0.7)
mysns_dset = mysns.load_dataset('diamonds')
print(mysns_dset.head())
mysns.barplot(x='cut',y='carat',data=mysns_dset)
myplt.show()