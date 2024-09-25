# finding roots of an equation: x +  cos(x)
import scipy as myscpy
from math import cos
#print(help(myscpy.optimize.root))
def myeq_func(x):
    return 2*x + cos(x)

myrootvar = myscpy.optimize.root(myeq_func,1) # args as function and initial guess
print(myrootvar.x)
print('-'*50)
print(myrootvar) # information about whole root