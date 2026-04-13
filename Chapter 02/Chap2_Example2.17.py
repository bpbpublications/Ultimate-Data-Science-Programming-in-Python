import numpy as mynp
# 2-D diagonal elements are extracted
myndarray = mynp.arange(1,17).reshape(4,4)
print(f"2-D Original array is : \n {myndarray}")
print(f"Elements which are present at 0-diagonal : {mynp.diag(myndarray,k=0)}")
print(f"Elements which are present at 1-diagonal : {mynp.diag(myndarray,k=1)}")
print(f"Elements which are present at 2-diagonal : {mynp.diag(myndarray,k=2)}")
print(f"Elements which are present at -1-diagonal : {mynp.diag(myndarray,k=-1)}")
print(f"Elements which are present at -2-diagonal : {mynp.diag(myndarray,k=-2)}")
print(f"Elements which are present at 3-diagonal : {mynp.diag(myndarray,k=3)}")
print(f"Elements which are present at -3-diagonal : {mynp.diag(myndarray,k=-3)}")
print('-'*50)

# 1-D construct a 2-D array using the provided elements and a diagonal array;
# the remaining elements are all filled with zeros.
myndarray1 = mynp.array([100,200,300,400])
print(mynp.diag(myndarray1,k=0))
print('-'*50)
myndarray2 = mynp.array([100,200,300,400])
print(mynp.diag(myndarray2,k=1))
print('-'*50)
myndarray3 = mynp.array([100,200,300,400])
print(mynp.diag(myndarray3,k=-1))