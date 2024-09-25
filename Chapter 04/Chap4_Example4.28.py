import numpy as mynp
import scipy.spatial as myscpy
import matplotlib.pyplot as myplt

myarray = mynp.array([[2,5],[3,5],[3,3],[2,2],[4,1]])

myvar_simplices = myscpy.Delaunay(myarray).simplices
myxcoordinate = myarray[:, 0]
myycoordinate = myarray[:, 1]
myplt.triplot(myxcoordinate, myycoordinate, myvar_simplices)
myplt.scatter(myxcoordinate, myycoordinate, color='b')

myplt.show()