import numpy as mynp
import scipy.sparse as myscpy
 # Creating a dense matrix
mydense_matrix = mynp.array([[11, 12, 0, 0],
                         [13, 14, 15, 0],
                         [0, 16, 71, 18],
                         [0, 0, 19, 100]])
 # Converting the dense matrix to BSR format
mybsr_matrix = myscpy.bsr_matrix(mydense_matrix, blocksize=(2, 2))
print(mybsr_matrix)
