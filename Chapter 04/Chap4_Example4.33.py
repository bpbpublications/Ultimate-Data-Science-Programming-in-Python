import scipy.integrate as myscpy
#print(help(myscpy.nquad))
def myfunc(x, y):
    return -4*(x + 5*y)

x_lower = 0
x_upper = 1
y_lower = lambda x:1
y_upper = lambda x: 1-x

myresult, myerror = myscpy.dblquad(myfunc, x_lower, x_upper, y_lower, y_upper)
print("The result of the multiple integral using dblquad is:", myresult)
print("The error of the multiple integral using dblquad is:", myerror)
