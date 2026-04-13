# 2-D array creation from list
import numpy as mynp
myl1 = [[100,200,300],[400,500,600],[700,800,900]]
myndarray = mynp.array(myl1)
print(f'myndarray type is: ==> {type(myndarray)}')
print(f"myndarray==> {myndarray}")

# nd-array properties
print(f'Array dimensions is: {myndarray.ndim}')
print(f'Data type of elements of array is :  {myndarray.dtype}')
print(f'Array size is : {myndarray.size}')
print(f'Array shape is : {myndarray.shape}')