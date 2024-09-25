# Line plot creation by passing 2 ndarrays with title, xlabel and ylabel
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis) # line plot is drawn
myplt.title('Cube Function Line Plot') # title is provided to the line plot
myplt.xlabel('X axis-Value -------') # information is described about x-axis data
myplt.ylabel('Cube of Y axis-Value -------') # information is described about y-axis data
myplt.show() # Display the line plot
