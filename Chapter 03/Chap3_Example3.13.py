import numpy as mynp

#print(help(mynp.vsplit))
myarr1= mynp.arange(1,17).reshape(4,4)
print("Eg1: splitting based on sections ................")
print(f"vsplit:2 {mynp.vsplit(myarr1,2)}")
print(f"vsplit:4 {mynp.vsplit(myarr1,4)}")

print("Eg2: splitting based on indices ................")
print(f"vsplit:2 {mynp.vsplit(myarr1,[2,3])}")

