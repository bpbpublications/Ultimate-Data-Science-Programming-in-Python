import numpy as mynp
import scipy.interpolate as myscpy
#print(help(myscpy.Rbf))
myarr1 = mynp.array([0, 1, 2, 3, 4, 5])
myarr2 = mynp.array([0, 1, 4, 9, 16, 25])

myrbf = myscpy.Rbf(myarr1, myarr2)

mynew_x = 3.5
myestimated_y = myrbf(mynew_x)

print(myestimated_y)