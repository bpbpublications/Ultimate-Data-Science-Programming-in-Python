import scipy.spatial as myscpy
import numpy as mynp
import matplotlib.pyplot as myplt

mypoints = mynp.array([[2, 3], [4, 1],[3, 6], [5, 6], [7, 2], [8, 9]])
mykdtree = myscpy.KDTree(mypoints)
myquery_point = mynp.array([5, 6])
mydistances, myindices = mykdtree.query(myquery_point, k=2)
mynearest_neighbors = mypoints[myindices]
print("Nearest neighbor value is as follows:", mynearest_neighbors)

myvar_simplices = myscpy.Delaunay(mypoints).simplices
myxcoordinate = mypoints[:, 0]
myycoordinate = mypoints[:, 1]
myplt.triplot(myxcoordinate, myycoordinate, myvar_simplices)
myplt.scatter(myxcoordinate, myycoordinate, color='b')
myplt.show()