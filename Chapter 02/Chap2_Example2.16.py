import numpy as mynp

# 2-D array with default value k = 0
print(mynp.eye(3,4))
print('-'*50)
# 2-D array with k = 1
print(mynp.eye(4, k=1))
print('-'*50)
# 2-D array with k = 2
print(mynp.eye(4, k=2))
print('-'*50)
# 2-D array with k = -1
print(mynp.eye(4, k=-1))
print('-'*50)
# 2-D array with k = -2
print(mynp.eye(4, k=-2))