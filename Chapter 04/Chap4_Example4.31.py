import scipy.integrate as myscpy
def myfunc(x):
    return x**2
# print(help(myscpy.quad))
myresult, myerror = myscpy.quad(myfunc, 0, 1)

print("My answer if simple integral is:", myresult)
print("the error is:", myerror)