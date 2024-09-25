import scipy.integrate as myscpy
#print(help(myscpy.nquad))
def myfunc(x, y):
    return x / y**2

x_lower = 1
x_upper = 2
y_lower = 4
y_upper = 6

myresult, myerror = myscpy.nquad(myfunc, [[x_lower, x_upper], [y_lower, y_upper]])
print("The result of the multiple integral using nquad is:", myresult)
print("The error of the multiple integral using nquad is:", myerror)
