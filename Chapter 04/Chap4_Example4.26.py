import numpy as mynp
import scipy.sparse as myscpy
 # Create an empty LIL matrix with shape (3, 3)
mymatrix = myscpy.lil_matrix((3, 3), dtype=mynp.float32)
 # Set some non-zero elements
mymatrix[0, 1] = 12.5
mymatrix[1, 2] = 11.3
mymatrix[2, 0] = 14.7
# elements access
print(mymatrix[0, 1])  # Output: 2.5
# Converting LIL matrix to a dense matrix
mydense_matrix = mymatrix.toarray()
print(mydense_matrix)
