import numpy as mynp

#print(help(mynp.ndarray.ravel))

print("Eg1 using ravel method------------------------------")
myarr1 = mynp.arange(1,7).reshape(2,3)
myarr2 = myarr1.ravel()
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")

print("Eg2 Making changes to the ravel array------------------------------")
myarr2[0] = 11
print(f"myarr1 after making changes to ravel array is {myarr1}")
print(f"myarr2 after making changes to ravel array is {myarr2}")

print("Eg3 Using ravel function------------------------------")
myarr3 = mynp.arange(1,7).reshape(2,3)
myarr4 = mynp.ravel(myarr3, order='F')
print(f"myarr3 is {myarr3}")
print(f"myarr4 is {myarr4}")