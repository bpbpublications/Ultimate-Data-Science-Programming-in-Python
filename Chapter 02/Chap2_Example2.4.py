import numpy as mynp
from datetime import datetime
myarr1 = mynp.array([4,5,6])
myarr2 = mynp.array([1,2,3])

#conventional python code
def dot_product(myarr1,myarr2):
    myresult = 0
    for x,y in zip(myarr1,myarr2):
        myresult +=  x*y
    return myresult
mybefore = datetime.now()
for loop in range(1000000):
    dot_product(myarr1,myarr2)
myafter = datetime.now()
print('Total Time taken by conventional python:',myafter-mybefore)

#numpy library code
mybefore = datetime.now()
for loop in range(1000000):
    mynp.dot(myarr1,myarr2) # numpy
myafter = datetime.now()
print('Total Time taken by Numpy Library:',myafter-mybefore)