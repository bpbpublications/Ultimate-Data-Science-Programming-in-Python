import pandas as mypd
import numpy as mynp
mydf = mypd.Series([20, mypd.NA, mynp.NaN, 25, None])
# arithmetic operations with scalar value
print(mydf*2)
# arithmetic operations between 2 series objects
mys1 = mypd.Series(data = [1,2,3,4,5], index = ['r','s','t','u','v'])
mys2 = mypd.Series(data = [6,7,8,9,10], index = ['r','s','t','u','v'])
print(mys1+mys2)
mys3 = mypd.Series(data = [1,2,3,4,5], index = ['r','s','t','u','v'])
mys4 = mypd.Series(data = [6,7,8,9,10], index = ['r','s','t','w','x'])
print(mys3+mys4)