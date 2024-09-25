import seaborn as mysns
import matplotlib.pyplot as myplt
print(mysns.plotting_context())
mysns_dset = mysns.load_dataset('planets') # EG3_P1
mysns.set_context(context='poster',rc={'axes.labelsize': 10.0,'axes.titlesize': 15.0,'grid.linewidth': 3.0})# EG3_P2
mysns.scatterplot(x='mass',y='distance',data=mysns_dset)# EG3_P3
myplt.title('poster context')# EG3_P4
myplt.show()# EG3_P5