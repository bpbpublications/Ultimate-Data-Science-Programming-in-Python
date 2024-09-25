import scipy as myscpy
#print(help(myscpy.optimize.minimize))
def myfunc_eqn(x):
      return x**2 + 3*x + 5
myvarmin = myscpy.optimize.minimize(myfunc_eqn, 0, method='BFGS')
print(myvarmin)