import scipy.interpolate as myscpy
import numpy as mynp
import matplotlib.pyplot as plt

# Creating Sample data points
myarr1 = mynp.array([0, 1, 2, 3, 4, 5, 6])
myarr2 = mynp.array([0, 1, 4, 9, 16, 25, 36])

myfunc = myscpy.UnivariateSpline(myarr1, myarr2, k=2)

mynew_x = mynp.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
mynew_y = myfunc(mynew_x)

print(mynew_y)
plt.plot(mynew_x, mynew_y,'ro-')
plt.scatter(mynew_x, mynew_y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Spline Interpolation with k=2')
plt.show()