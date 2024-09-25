import numpy as mynp

# print(help(mynp.hstack))

print("Eg1 hstack for 1-D array------------------------------")
myarr1 = mynp.array([1, 2, 3,])
myarr2 = mynp.array([11,12,13,14])
myarr3 = mynp.hstack((myarr1,myarr2))
print(f"Hstack array is {myarr3}")

print("Eg2 2-D array shape with (3,3) and (3,2)------------------------------")
a = mynp.arange(1,10).reshape(3,3)
b = mynp.arange(1,7).reshape(3,2)
print(f" hstack array is : {mynp.hstack((a,b))}")

print("Eg with error ------------------------------")
myarr4 = mynp.arange(1,5).reshape(2,2)
myarr5 = mynp.arange(1,7).reshape(3,2)
print(f" hstack array error for the above : {mynp.hstack((myarr4,myarr5))}")