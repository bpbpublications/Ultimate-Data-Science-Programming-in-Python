import numpy as mynp

#print(help(mynp.ndarray.flat))

print("Eg1 ------------------------------")
mynp1=mynp.arange(1,7).reshape(2,3)
print(mynp1.flat)

# iterating
for loop in mynp1.flat:
    print(loop)