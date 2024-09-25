import numpy as mynp
import scipy.interpolate as myscpy
import matplotlib.pyplot as myplt

# Specifying the known data points
myarr1 = mynp.array([1, 2, 3, 4, 5])
myarr2 = mynp.array([2, 4, 1, 5, 3])

# Performing spline interpolation with splrep
mytck = myscpy.splrep(myarr1, myarr2, k=2)

# Generating new x values for interpolation
myx_interp = mynp.linspace(1, 5, 100)

# Evaluating the spline at the new x values
myy_interp = myscpy.splev(myx_interp, mytck)

# Plotting the known data points
myplt.scatter(myarr1, myarr2, color='red', label='Data known')

# Plotting the interpolated values
myplt.plot(myx_interp, myy_interp, label='Interpolated')

# Assigning plot labels and title
myplt.xlabel('My x-axis')
myplt.ylabel('My y-axis')
myplt.title('Quadratic Interpolation with k=2')

# Adding legend
myplt.legend()

# Displaying the plot
myplt.show()