import numpy as mynp

# print(help(mynp.dstack))

print("Eg1 dstack for 1-D array------------------------------")
myarr1 = mynp.array([1, 2, 3,])
myarr2 = mynp.array([11,12,13])
myarr3 = mynp.dstack((myarr1,myarr2))
print(f"dstack array is {myarr3}")
print(f"dstack 1-D array shape is {myarr3.shape}")

print("d stack for 2-D array------------------------------")
a = mynp.arange(11,17).reshape(3,2)
b = mynp.arange(1,7).reshape(3,2)
print(f" dstack 2-D array is : {mynp.dstack((a,b))}")
print(f" dstack 2-D array shape is : {mynp.dstack((a,b)).shape}")