import numpy as mynp
# evenly spaced values of no. of samples as 50 between 0 and 1 which includes both 0 and 1
print(mynp.linspace(0,1))
print('-'*50)
# 3 evenly spaced values between 0 and 1 and also including both 0 and 1
print(mynp.linspace(0,1,3))
print('-'*50)
# 3 evenly spaced values between 0 and 1 and also including 0 but excluding 1
print(mynp.linspace(0,1,3, endpoint=False))
print('-'*50)
# 3 evenly spaced values between 0 and 1 and also including 0 but excluding 1 and returning spacing
print(mynp.linspace(0,1,3, endpoint=False, retstep=True))
print('-'*50)
# 10 values between 1 to 50 including both 1 and 50 with equally spacing int type values
print(mynp.linspace(1,50,5, dtype=int, retstep=True))