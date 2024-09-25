import matplotlib.pyplot as myplt
import numpy as mynp
# print(help(myplt.subplots))
myxaxis_data = mynp.arange(1,11)
my_y1 = myxaxis_data
my_y2 = myxaxis_data *2
my_y3 = myxaxis_data **2
my_y4 = myxaxis_data **3

myfig,myax = myplt.subplots(2,2)

myax[0,0].plot(myxaxis_data,my_y1,color='r',marker='o')
myax[0,0].set(xlabel='Xaxis data',ylabel='Yaxis data',title='Same Value Linearity')

myax[0,1].plot(myxaxis_data,my_y2,color='b',marker='o')
myax[0,1].set(xlabel='Xaxis data',ylabel='Yaxis data',title='Double of Xaxis')

myax[1,0].plot(myxaxis_data,my_y3,color='y',marker='o')
myax[1,0].set(xlabel='Xaxis data',ylabel='Yaxis data',title='Square function')

myax[1,1].plot(myxaxis_data,my_y4,color='g',marker='o')
myax[1,1].set(xlabel='Xaxis data',ylabel='Yaxis data',title='Cubic function')

myplt.tight_layout()
myplt.show()