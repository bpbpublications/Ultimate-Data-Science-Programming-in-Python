import numpy as mynp
# print(help(mynp.insert))
myarr1= mynp.array([10,11,12,15,19,8,39,16,57,8])
myarr2 = mynp.insert(myarr1,[1,4],[87,89])
print(myarr2) # inserting 87 before index 1 and 89 before index 4
myarr3 = mynp.insert(myarr1,2,33.56) # float ---> int as the original array contains int values
print(myarr3)
myarr4 = mynp.insert(myarr1,2,True) # addition of value 1 before index position 2
print(myarr4)

# If axis not defined for 2-D array, then 2D will be flattened to 1-D 
# and then insertion will happen
myarr5 = mynp.arange(4).reshape(2,2)
myarr6 = mynp.insert(myarr5,2,10)
print(myarr6)

# when axis = 0 or -2 is defined then insertion of rows after broadcasting will happpen
myarr7 = mynp.insert(myarr5,1,10, axis=0)
print(myarr7)
print('-'*50)
# when axis = 1 or -1 is defined then insertion of columns after broadcasting will happpen
myarr8 = mynp.insert(myarr5,1,10, axis=-1)
print(myarr8)