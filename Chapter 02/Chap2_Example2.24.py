import numpy as mynp

# Approach1: iteration using python loop 
# we are iterating elements of 3-D array
myarr1 = mynp.array([[[100,200],[300,400]],[[500,600],[700,800]]])
for outer in myarr1: #iterating 2-D array with no scalar value
    for inner in outer: # iterating 1-D array with no scalar value
        for data in inner: # here data is a scalar value
            print(data)
print('-'*50)

# Approach2: iteration using nditer() function: class in numpy library with only one loop for iterating any n-D array
# using nditer we will get elements only but not indexes
myarr2=mynp.arange(1,7).reshape(2,3)
for loop in mynp.nditer(myarr2):
    print(loop)
print('-'*50)

# Approach3: iteration using ndenumerate() function
# This function will return indexes in addition to elements as multidimensional
# index iterator will be returned yielding pair of index-tuple with the corresponding array values
for mypos,myelement in mynp.ndenumerate(myarr2):
    print(f'{myelement} is present at position:{mypos}')
