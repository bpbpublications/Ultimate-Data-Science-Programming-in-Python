# clm form
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis,'g:o')# clm form
myplt.title('Cube Function Line Plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Cube of Y axis-Value -------')
myplt.show()
