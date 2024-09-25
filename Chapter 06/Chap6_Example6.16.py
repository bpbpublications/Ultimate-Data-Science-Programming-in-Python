import matplotlib.pyplot as myplt
import numpy as mynp
# print(help(myplt.subplot))
myxaxis_data = mynp.arange(1,11)
my_y1 = myxaxis_data
my_y2 = myxaxis_data *2
my_y3 = myxaxis_data **2
my_y4 = myxaxis_data **3

myfig = myplt.figure(figsize=(8,6),num=1)
myax1 = myplt.subplot(2,2,1)
myax1.plot(myxaxis_data,my_y1,color='r',marker='o')
myax1.set(xlabel='Xaxis data',ylabel='Yaxis data',title='Same Value Linearity')

myax2 = myplt.subplot(2,2,2)
myax2.plot(myxaxis_data,my_y2,color='b',marker='o')
myax2.set(xlabel='Xaxis data',ylabel='Yaxis data',title='Double of Xaxis')

myax3 = myplt.subplot(2,2,3)
myax3.plot(myxaxis_data,my_y3,color='y',marker='o')
myax3.set(xlabel='Xaxis data',ylabel='Yaxis data',title='Square function')

myax4 = myplt.subplot(224) # comma can be removed
myax4.plot(myxaxis_data,my_y4,color='g',marker='o')
myax4.set(xlabel='Xaxis data',ylabel='Yaxis data',title='Cubic function')

myplt.tight_layout()
myplt.show()