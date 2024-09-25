import numpy as mynp

#print(help(mynp.concatenate))

print("Eg1 1-D array concatenation------------------------------")
myarr1= mynp.arange(4)
myarr2= mynp.arange(5)
print(f"Concatenation array 1-D is {mynp.concatenate((myarr1,myarr2))}")

print("Eg2 2-D array concatenation with/without axes parameter------------------------------")
myarr3 = mynp.arange(1,7).reshape(2,3)
myarr4 = mynp.array([[10,11,12],[13,14,15]])
print(f"Vertical concatenation: {mynp.concatenate((myarr3,myarr4), axis=0)}")
print('-'*50)
print(f"Horizontal concatenation: {mynp.concatenate((myarr3,myarr4), axis=1)}")
print('-'*50)
print(f"Flat and then concatenation: {mynp.concatenate((myarr3,myarr4), axis=None)}")

print("Eg3 out parameter and dtype usage------------------------------")
# After concatenation, using the 'out' parameter, we can store 
# the result in an array, but the result and out must be in the same shape.
myarr5 = mynp.arange(5)
myarr6 = mynp.arange(3)
myempty = mynp.empty(8, dtype=str)
print(f"out and dtype usage: {mynp.concatenate((myarr5,myarr6), out=myempty)}")
print(f"out and dtype usage: {mynp.concatenate((myarr5,myarr6), out=myempty, dtype=str)}") # error in the above line