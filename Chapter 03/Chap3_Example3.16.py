import numpy as mynp

# print(help(mynp.array_split))
myarr1 = mynp.arange(10)
myarraysplit = mynp.array_split(myarr1,3)
# 10 %3 = 1 subarray having size as 10//3 + 1 = 4
# and rest 2 subarray of each size 10//3 = 3
# Concept: # a % n sub-arrays of size a//n + 1 where a: length and n sections
# and the rest of size a//n
print(f"Array split 1-D array result is: {myarraysplit}")

myarr2 = mynp.arange(10).reshape(5,2)
myarraysplit2 = mynp.array_split(myarr2,4)
# Concept: # 5 % 4 (1) sub-arrays of size 5//4 + 1 = 2
# and the rest (3) subarrays of size 5//4 = 1 . So (2,1,1,1)
print(f"Array split 2-D array result is: {myarraysplit2}")