import matplotlib.pyplot as myplt
import numpy as mynp
myarr1 = mynp.array([20,40,60,80,100])
myplt.plot(myarr1,'o-.g',lw=5,markersize=5, mfc='magenta')
myplt.grid(color='r',lw=2)
myplt.minorticks_on()
myplt.grid(which='minor', color='y')
myplt.show()