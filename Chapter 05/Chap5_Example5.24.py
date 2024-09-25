import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,16)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis,'o:r', alpha = 0.6)# mlc form with alpha = 0.2
myplt.title('Cube Function Line Plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Cube of Y axis-Value -------')
myplt.grid()
myleft,myright = myplt.xlim()
mybottom, mytop = myplt.ylim()
print('The default Left limit value on the x-axis:',myleft)
print('The default Right limit value on the x-axis:',myright)
print('The default Bottom limit value on the y-axis:',mybottom)
print('The default Top limit value on the y-axis:',mytop)

# setting the new limit values
myplt.xlim(left = 0.7, right = 10)
myplt.ylim(bottom = 20, top = 3000)
myplt.show()