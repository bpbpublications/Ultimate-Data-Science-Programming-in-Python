import numpy as mynp

#print(help(mynp.hsplit))
myarr1= mynp.arange(1,9).reshape(2,4)
print("Eg1: splitting based on sections ................")
print(f"hsplit:2 {mynp.hsplit(myarr1,2)}")

print("Eg2: splitting based on indices ................")
print(f"hsplit: {mynp.hsplit(myarr1,[2,3])}")

