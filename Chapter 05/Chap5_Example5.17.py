# plotting multiple lines in the same plot
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
y_axis1 = x_axis
y_axis2 = x_axis**2
y_axis3 = x_axis**3
myplt.plot(x_axis,y_axis1,'o:r')
myplt.plot(x_axis,y_axis2,'o:g')
myplt.plot(x_axis,y_axis3,'o:b')
# myplt.plot(x_axis,y_axis1,'o:r',x_axis,y_axis2,'o:g',x_axis,y_axis3,'o:b') # plotting 3 lines using single plot() function
myplt.title('Plotting multiple lines in the same plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Y axis-Value -------')
myplt.show()
