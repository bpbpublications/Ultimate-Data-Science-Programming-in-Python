import numpy as mynp

# print(help(mynp.vstack))

print("Eg1 vstack for 1-D array------------------------------")
myarr1 = mynp.array([1, 2, 3,])
myarr2 = mynp.array([11,12,13])
myarr3 = mynp.vstack((myarr1,myarr2))
print(f"Vstack array is {myarr3}")

print("Eg2 2-D array shape with (3,3) and (2,3)------------------------------")
a = mynp.arange(1,10).reshape(3,3)
b = mynp.arange(20,26).reshape(2,3)
print(f" vstack array is : {mynp.vstack((a,b))}") # size of axis 1 of both the arrays are same

