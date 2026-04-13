import numpy as mynp
# print(help(mynp.random.shuffle)) # This will display help of shuffle function

# shuffling of 1-D array
mynp1 = mynp.arange(6)
print(f'before shuffle mynp1 data is {mynp1}')
mynp.random.shuffle(mynp1)
print(f'after shuffle mynp1 data is {mynp1}')
print('-'*50)

# shuffling of 2-D array -- shuffling around axis0
mynp2 = mynp.random.randint(1,50,size=(4,3))
print(f'before shuffle mynp2 data is {mynp2}')
mynp.random.shuffle(mynp2)
print(f'after shuffle mynp2 data is {mynp2}')