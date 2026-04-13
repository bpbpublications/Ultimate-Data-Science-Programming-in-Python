import numpy as mynp

print("Broadcasting of 1-D array--------------")
# Broadcasting of 1-D array
myarr1=mynp.array([11,12,13])
myarr2= mynp.array([10])
print(f"myarr1 is {myarr1}")
print(f"myarr2 is {myarr2}")
print(f"myarr1+myarr2 is: {myarr1+myarr2}")
#                 myarr1 is      [11 12 13]
# on broadcasting myarr2 becomes [10 10 10]
#                 answer becomes [21 22 23]

print("Broadcasting of 2-D array--------------")
myarr3= mynp.arange(1,7).reshape(2,3)
myarr4= mynp.array([10,12,13])
print(f"myarr3 is {myarr3}")
print(f"myarr4 is {myarr4}")
print(f"myarr3+myarr4 is: {myarr3+myarr4}")
#                 myarr3 is      [1 2 3]
#                                [4 5 6]
# on broadcasting myarr4 becomes [10 12 13]
#                                [10 12 13]
#                 answer becomes [11 14 16]
#                                [14 17 19]
