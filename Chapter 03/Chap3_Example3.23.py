import numpy as mynp

print("Finding matrix inverse")
myarr1 = mynp.arange(11,15).reshape(2,2)
print(mynp.linalg.inv(myarr1)) # only valid for square matrices

print("Finding power of a matrix with n=0")  # only valid for square matrices
print(mynp.linalg.matrix_power(myarr1,0))
print("Finding power of a matrix with n>0")
print(mynp.linalg.matrix_power(myarr1,2))
print("Finding power of a matrix with n<0")
print(mynp.linalg.matrix_power(myarr1,-2)) # first inverse then power

print("Finding matrix determinant") # only valid for square matrices
print(mynp.linalg.det(myarr1))

print("Finding Solving linear algebra equations")
myarr2 = mynp.array([[1,1],[2,6]])
myarr3 = mynp.array([6,24])
print(mynp.linalg.solve(myarr2,myarr3))