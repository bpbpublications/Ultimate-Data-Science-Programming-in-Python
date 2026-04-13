import numpy as mynp

# Example of view
mynp1=mynp.array([1,2,3,4,5])
mynp2=mynp1.view()
print(f"The original array is: {mynp1}")
print(f"The view array is: {mynp2}")
print('-'*50)
mynp1[2]=100
print(f"After changing 2nd index value of mynp1, mynp1 array value is changed as: {mynp1}")
print(f"After changing 2nd index value of mynp1, mynp2 array value is changed as: {mynp2}")
print('-'*50)
mynp2[-1]=300
print(f"After changing last index value of mynp2, mynp1 array value is changed as: {mynp1}")
print(f"After changing last index value of mynp2, mynp2 array value is changed as: {mynp2}")

# Example of copy
print('*'*100)
mynp3=mynp.array([11,12,13,14,15])
mynp4=mynp3.copy()
print(f"The original array is: {mynp3}")
print(f"The copy array is: {mynp4}")
print('-'*50)
mynp3[2]=110
print(f"After changing 2nd index value of mynp3, mynp3 array value is changed as: {mynp3}")
print(f"After changing 2nd index value of mynp3, mynp4 array value is retained as: {mynp4}")
print('-'*50)
mynp4[-1]=310
print(f"After changing last index value of mynp4, mynp3 array value is retained as: {mynp3}")
print(f"After changing last index value of mynp4, mynp4 array value is changed as: {mynp4}")
