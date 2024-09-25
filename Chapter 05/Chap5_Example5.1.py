# Line plot creation by passing 2 ndarrays
import matplotlib.pyplot as myplt
import numpy as mynp
#print(help(myplt.plot))
x_axis = mynp.arange(1,11)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis) #(1,1),(2,8),(3,27)
myplt.show()
