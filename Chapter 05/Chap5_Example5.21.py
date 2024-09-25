import matplotlib.pyplot as myplt
import numpy as mynp
myarr1 = mynp.linspace(0, 2*mynp.pi,100)
# Create a figure with subplots
myfig, myaxs = myplt.subplots(3, 1)

myaxs[0].plot(myarr1, myarr1**2, label='MySquare')
myaxs[0].plot(myarr1, mynp.sin(myarr1), label='MySine')
myaxs[0].plot(myarr1, mynp.cos(myarr1), label='MyCos')
myaxs[0].legend()

myaxs[1].plot(myarr1, myarr1**2)
myaxs[1].plot(myarr1, mynp.sin(myarr1))
myaxs[1].plot(myarr1, mynp.cos(myarr1))
myaxs[1].legend(['MySquare','MySine','MyCos'])

# Create a list of handles and labels
myline1, = myplt.plot(myarr1, myarr1**2)
myline2, = myplt.plot(myarr1, mynp.sin(myarr1))
myline3, = myplt.plot(myarr1, mynp.cos(myarr1))
myhandles = [myline1,myline2,myline3]
mylabels = ['MySquare','MySine','MyCos']

# Add a legend with handles and labels
myaxs[2].legend(myhandles, mylabels)
myplt.show()