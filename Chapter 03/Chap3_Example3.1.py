import numpy as mynp

# print(help(mynp.reshape)) # --- will display help for reshape function

print("Eg-1 1-D array conversion to 2-D array with by default C style order ---------------------------")
myarr1 = mynp.arange(1,7)
myarr2 = myarr1.reshape(2,3)
print(f"myarr1 is : {myarr1}")
print(f"myarr2 is : {myarr2}")

print("Eg-2 modifying the 2nd index value of original array ---------------------------")
myarr1[1] = 12
print(f"myarr1 after modification in the original array is : {myarr1}")
print(f"myarr2 after modification in the reshaped array is : {myarr2}")

print("Eg-3 F Style order ---------------------------")
myarr3 = mynp.arange(1,7)
myarr4 = myarr3.reshape((2,3), order='F')
print(f"myarr3 is : {myarr3}")
print(f"myarr4 is : {myarr4}")
