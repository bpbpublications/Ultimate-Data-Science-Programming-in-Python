import matplotlib.pyplot as myplt
import numpy as mynp
#print(help(myplt.grid))
myarr1 = mynp.array([20,40,60,80,100])

# Create a figure with subplots
myfig, myaxs = myplt.subplots(2, 2)

# displaying case-1 of grid lines visibility
myaxs[0, 0].plot(myarr1,'o:r')
myaxs[0, 0].set_title('Subplot 0-0')
myaxs[0, 0].grid()

# displaying case-2 of grid lines visibility
myaxs[0, 1].plot(myarr1,'o:r')
myaxs[0, 1].set_title('Subplot 0-1')
myaxs[0, 1].grid()
myaxs[0, 1].grid()

# displaying case-3 of grid lines visibility
myaxs[1, 0].plot(myarr1,'o:r')
myaxs[1, 0].set_title('Subplot 1-0')
myaxs[1, 0].grid()
myaxs[1, 0].grid(color='y')

# displaying case-4 of grid lines visibility
myaxs[1, 1].plot(myarr1,'o:r')
myaxs[1, 1].set_title('Subplot 1-1')
myaxs[1, 1].grid(visible = True)

# Adjust the spacing between subplots
myplt.tight_layout()
myplt.show()