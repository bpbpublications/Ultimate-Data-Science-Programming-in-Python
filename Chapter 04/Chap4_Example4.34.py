import scipy.interpolate as myscpy
import numpy as mynp
# print(help(myscpy.interp1d))

x = mynp.array([0, 2, 4, 6, 8, 10])
y = mynp.vectorize(lambda num: num**2)(x)
print(y)
myfunc = myscpy.interp1d(x, y, kind='linear')
print(myfunc(5))