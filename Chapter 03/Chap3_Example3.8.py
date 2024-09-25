import numpy as mynp

# print(help(mynp.stack))

print("Eg1 axis-0(default) stacking in 1-D array ------------------------------")
myarr1= mynp.array([1,2,3])
myarr2 = mynp.array([10,12,13])
mystack_array = mynp.stack((myarr1,myarr2))
print(f"Stack array result is: {mystack_array }")
print(f"Shape of stack array is: {mystack_array.shape}")

print("Eg2 stacked array with axis-1 ------------------------------")
myarr3= mynp.arange(1,7).reshape(2,3)
myarr4 = mynp.array([[10,12,13],[14,15,17]]) 
mystack_array_3D = mynp.stack((myarr3,myarr4), axis=1)
print(f"Stack array result is: {mystack_array_3D }")
print(f"Shape of stack array is: {mystack_array_3D.shape}")
# Take 1st row from 1st array and make it 1st row of the stacked array
# Take 2nd row from 2nd array and make it 2nd row of the stacked array
# Combine these 2 rows and repeat the remaining rows of the arrays
# axis-1 means row wise in each 2-D array

print("Eg3 stacked array with axis-2 ------------------------------")
# axis-2 means column wise in each 2-D array
mystack_array_3D = mynp.stack((myarr3,myarr4), axis=2)
print(f"Stack array result is: {mystack_array_3D }")
print(f"Shape of stack array is: {mystack_array_3D.shape}")