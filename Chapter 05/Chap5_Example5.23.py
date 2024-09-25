import matplotlib.pyplot as myplt
import numpy as mynp
myarr1 = mynp.linspace(0, 2*mynp.pi,100)

myplt.plot(myarr1, myarr1**2, label='MySquare')
myplt.plot(myarr1, mynp.sin(myarr1), label='MySine')
myplt.plot(myarr1, mynp.cos(myarr1), label='MyCos')
myplt.legend(title = "3 different plots", loc=6, ncol=3)

myleft,myright = myplt.xlim()
mybottom, mytop = myplt.ylim()
print('The Left limit value on the x-axis:',myleft)
print('The Right limit value on the x-axis:',myright)
print('The Bottom limit value on the y-axis:',mybottom)
print('The Top limit value on the y-axis:',mytop)
myplt.show()