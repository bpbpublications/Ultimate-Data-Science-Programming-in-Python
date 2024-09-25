import numpy as mynp
import scipy.spatial as myscpy
import matplotlib.pyplot as myplt

myarray = mynp.array([[3, 5],[4, 5],[4, 1],[3, 3],[5, 2],[2, 3],
                      [6, 1],[4, 2],[2, 3],[1, 3]])

myvar_simplices = myscpy.ConvexHull(myarray).simplices
myxcoordinate = myarray[:, 0]
myycoordinate = myarray[:, 1]

myplt.scatter(myxcoordinate, myycoordinate, color='b')
for mypoints in myvar_simplices:
    myplt.plot(myarray[mypoints,0], myarray[mypoints,1], 'g-')

myplt.show()