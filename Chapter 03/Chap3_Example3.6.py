import numpy as mynp

#print(help(mynp.transpose))

print("Eg1 transpose with non specified axis parameter of 2-D array ------------------------------")
a = mynp.arange(1,7).reshape(2,3)
myarr1 = a.transpose()
print(f"Original Array is : \n {a}")
print(f"Transposed Array is : \n {myarr1}")

print("Eg2 Transpose with specified axis parameter of 3-D array ------------------------------")
a = mynp.arange(1,25).reshape(2,3,4)
myarr2 = mynp.transpose(a,axes=(1,2,0))
print(f"Original 3-D Array is : \n {a}")
print(f"Transposed 3-D Array is : \n {myarr2}")
print(f"Shape of Original 3-D Array is : \n {a.shape}")
print(f"Shape of Transposed 3-D Array is : \n {myarr2.shape}")

print("Eg3 Using T variable------------------------------")
a = mynp.arange(1,25).reshape(2,3,4)
myarr3 = a.T
print(f"Transposed 3-D Array is : \n {myarr3}") # (4,3,2)