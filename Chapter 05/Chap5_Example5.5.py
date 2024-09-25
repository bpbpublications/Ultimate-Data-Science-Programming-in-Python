# Line plot creation by passing 2 ndarrays with title, xlabel , ylabel ,marker , linestyle and color
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis,marker='o',linestyle='-.', color='g')
myplt.title('Cube Function Line Plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Cube of Y axis-Value -------')
myplt.show()
