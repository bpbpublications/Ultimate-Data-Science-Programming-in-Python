# list containing heterogenous elements
import numpy as mynp
myl1 = [100,200,310.5]
myndarray = mynp.array(myl1) # float upcasting
print(f'myndarray : {myndarray}')
print(f'Elements data type is: {myndarray.dtype}')