import numpy as mynp
# print(help(mynp.where))
# using where function
myarr1= mynp.array([10,11,12,15,19,8,39,16,57,8])
mysearch = mynp.where(myarr1%2==0)
print(myarr1[mysearch])

# condition based selection
myboolean_indexing = myarr1%2==0
print(myarr1[myboolean_indexing])
