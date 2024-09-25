import numpy as mynp

# print(help(mynp.resize))

print("Eg1 Increasing the size using functional style------------------------------")
myarr1=mynp.arange(1,5)
myarr2=mynp.resize(myarr1,(2,3))
print(f"myarr1 is: {myarr1}")
print(f"myarr2 is: {myarr2}")

print("Eg2 Increasing the size using object oriented style ------------------------------")
myarr3=mynp.arange(1,5)
myarr3.resize((2,3))
print(f"myarr3 is: {myarr3}")
