import numpy as mynp

# print(help(mynp.ndarray.flatten))

print("Eg1 Displaying flatten method example with default order='C'------------------------------")
myarr1=mynp.arange(1,7).reshape(2,3)
myarr2 = myarr1.flatten()
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")

print("Eg2 Changing the original array value will not be reflected in the flatten array------------------------------")
myarr1[0,0]=13
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")

print("Eg3 with order='F'------------------------------")
myarr3=myarr1.flatten('F')
print(f"Flatten array myarr3  is {myarr3}")