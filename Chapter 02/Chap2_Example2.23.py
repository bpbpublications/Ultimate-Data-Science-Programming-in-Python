import numpy as mynp
# We will be accessing elements of 3-D numpy array
mynd1 = mynp.array([
    [[11,12,13],[14,15,16],[17,18,19]],
    [[1,2,3],[4,5,6],[7,8,9]]
    ])
# 1. using indexing: single element access, zero based indexing supporting both +ve and -ve
print(f"Array shape is:  ==> {mynd1.shape}")
print("To access the element 19 from the 3-D array")
print(f"mynd1[0][2][2] ==> {mynd1[0][2][2]}")
print(f"mynd1[-2][-1][-1] ==> {mynd1[-2][-1][-1]}")
print('-'*50) 

# 2. using slicing: elements group which are in order
# for 3-D array: arrayname[[begin:end :step],[[begin:end :step]],[[begin:end :step]]]
print("Accessing elements: 0th and 2nd row of 0th and 2nd column value of each 2-D array")
print(f"mynd1[:,::2,::2] ==> {mynd1[:,::2,::2]}")
print('-'*50) 

# 3. using advanced indexing: elements group which are not ordered (arbitrary elements)
# In order to access 3-D array arbitrary elements use
# myndarray[[2-D array indices],[row indices],[column indices]]
print("To access element 15 and 5 from 3-D array")
print(mynd1[[0,1],[1,1],[1,1]])

print('-'*50) 
# 4. using condition based selection: selecting array elements based on condition
mynp2=mynp.arange(1,13).reshape(3,4)
print(mynp2[mynp2%2 !=0]) # displaying odd numbers from an array as condition will return the boolean value
# and array[condition] will return the result
