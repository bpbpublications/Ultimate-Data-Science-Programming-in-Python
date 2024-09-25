import scipy.sparse as myscpy

# Creating a 3x3 CSC matrix
mydata = [11, 12, 13, 14, 15, 16]  # non-zero values in column-wise order
myrow_indices = [0, 1, 2, 0, 1, 2]  # row indices of non-zero values
mycol_pointers = [0, 2, 4, 6]  # index pointers to start of columns

mycsc_matrix = myscpy.csc_matrix((mydata, myrow_indices, mycol_pointers), shape=(3, 3))
print(mycsc_matrix)