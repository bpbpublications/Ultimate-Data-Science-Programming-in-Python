# Line plot creation by passing 2 ndarrays with default color
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
myplt.plot(x_axis,x_axis) # blue
myplt.plot(x_axis,x_axis*2) # orange
myplt.plot(x_axis,x_axis*4) # green
myplt.plot(x_axis,x_axis*8) # red
myplt.title('Default color Line Plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Display of various calculations-------')
myplt.show()
