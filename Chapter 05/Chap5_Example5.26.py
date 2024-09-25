import matplotlib.pyplot as myplt
import numpy as mynp

my_x = mynp.arange(1,21)
my_y = my_x **3
# figure object creation ------------------------------
#print(help(myplt.figure))
myfig = myplt.figure()

# axis object creation ---------------------------
my_axes = myfig.add_subplot(111)  # 1 row, 1 column, plot number 1

# graph plotting ---------------------------
my_axes.plot(my_x, my_y)

# axes properties setting ---------------------------
my_axes.set(xlabel='X axis values', ylabel="Y axis values", title='Cubic Plot')
my_axes.grid()
myplt.show()