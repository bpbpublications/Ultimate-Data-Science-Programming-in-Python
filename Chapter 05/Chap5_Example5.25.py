import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(100000)
y_axis = mynp.arange(100000)

myplt.plot(x_axis,y_axis)
myplt.grid()
myplt.xscale('linear')
myplt.yscale('log')
myplt.yscale('log')

myplt.title('Plot of Linear vs Log')
myplt.xlabel('Linear -------')
myplt.ylabel('Log -------')
myplt.show()