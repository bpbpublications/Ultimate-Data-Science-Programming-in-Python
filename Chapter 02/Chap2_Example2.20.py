#  np.random module examples
import numpy as mynp
import sys
# single random integer value generation in the range between 20 to 29
print(mynp.random.randint(20,30))
print('-'*50)
# 1-D nd-array creation of size 5 with random values from 10 to 19
print(mynp.random.randint(10,20, size=5))
print('-'*50)
# 2-D array with high as None and random values from 0 to 49 with shape as (3,4)
print(mynp.random.randint(0,50, size=(3,4)))
print('-'*50)
# memory utilization is improved using dtype

a = mynp.random.randint(1,21,size=(30,40))
print(f"ndarray int32 size: {sys.getsizeof(a)}")
a = mynp.random.randint(1,21,size=(30,40),dtype='int8')
print(f"ndarray int8 size : {sys.getsizeof(a)}")
