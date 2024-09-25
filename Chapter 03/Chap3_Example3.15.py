import numpy as mynp

# print(help(mynp.dsplit))
myarr1= mynp.arange(24).reshape(2,3,4)
print("Eg1: splitting based on sections ................")
print(f"dsplit: {mynp.dsplit(myarr1,2)}")

print("Eg2: splitting based on indices ................")
print(f"dsplit: {mynp.dsplit(myarr1,[1,3])}")