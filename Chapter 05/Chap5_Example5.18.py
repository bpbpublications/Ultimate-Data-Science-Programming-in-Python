import matplotlib.pyplot as myplt
import numpy as mynp
myarr1 = mynp.array([20,40,60,80,100])
myplt.figure(figsize=(7,4),facecolor='pink')
myplt.plot(myarr1,'o:r')
#print(help(myplt.title))
myplt.title('Line Plot creation by passing a single ndarray', 
            fontfamily='serif', 
            fontsize=18,
            fontweight='bold',
            loc='center',
            pad=10,
            color='white',
            backgroundcolor='green')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Y axis-Value -------')
myplt.show()