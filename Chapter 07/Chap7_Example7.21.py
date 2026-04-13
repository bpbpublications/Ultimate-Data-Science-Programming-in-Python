import pandas as mypd
import numpy as mynp
mys1 = mypd.Series(data = [1,2,3,4,5,mynp.NaN], index = ['r','s','t','u','v','y'])
mys2 = mypd.Series(data = [6,7,8,9,10], index = ['r','s','t','w','x'])
print(mys1.add(mys2, fill_value=0))