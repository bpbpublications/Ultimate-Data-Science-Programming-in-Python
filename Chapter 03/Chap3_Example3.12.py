import numpy as mynp

#print(help(mynp.split))
print("Eg1 split for 1-D array based on sections------------------------------")
myarr1 = mynp.arange(1,7)
myarr2 = mynp.split(myarr1,3)
print(f"Array type is: {type(myarr2)}")
print(f"Subarrays are : {myarr2}")

print("Eg2 2-D array split based on sections------------------------------")
myarr3 = mynp.arange(1,19).reshape(6,3)
print(f"Array split ino 2 sections: {mynp.split(myarr3,2, axis=0)}")
print(f"Array split ino 6 sections: {mynp.split(myarr3,6, axis=0)}")

print("Eg3 Splitting 1-D array based on indices")
myarr4=mynp.arange(1,11)
myresult = mynp.split(myarr4,[3,6])
print(f"myresult for 1-D after splitting is: {myresult}") # splitting on indexes: 0,1,2 and 3,4,5 and 6,7,8,9

print("Eg4 Splitting 2-D array based on indices")
myarr5=mynp.arange(1,19).reshape(3,6)
myresult = mynp.split(myarr5,[3,5], axis=1)
print(f"myresult for 2-D after splitting is: {myresult}")