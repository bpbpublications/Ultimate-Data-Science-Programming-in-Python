import scipy.interpolate as myscpy
import numpy as mynp
import matplotlib.pyplot as myplt
#print(help(myscpy.UnivariateSpline))

myarr1 = mynp.array([0, 1, 2, 3, 4, 5, 6])
myarr2 = mynp.array([0, 1, 4, 9, 16, 25, 36])

myfunc = myscpy.UnivariateSpline(myarr1, myarr2, k=1)

mynew_x = mynp.array([.5, 1.5, 2.5, 3.5, 4.5, 5.5])
mynew_y = myfunc(mynew_x)

print(mynew_y)

myplt.plot(mynew_x, mynew_y,'ro-')
myplt.scatter(mynew_x, mynew_y)
myplt.xlabel('mynew_x')
myplt.ylabel('mynew_y')
myplt.title('Spline Interpolation with k=1')
myplt.show()