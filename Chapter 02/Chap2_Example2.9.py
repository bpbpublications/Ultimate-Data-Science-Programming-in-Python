import numpy as mynp
# type int
myndarray = mynp.array([100,200,310.5],dtype=int)
print(myndarray)

# type float
myndarray = mynp.array([100,200,310.5],dtype=float)
print(myndarray)

# type bool: For number and non-empty string --> True and for 0 and empty string--> False
myndarray = mynp.array([100,200,310.5, 0, "","Hello"],dtype=bool)
print(myndarray)

# type complex
myndarray = mynp.array([100,200,310.5],dtype=complex)
print(myndarray)

# type str
myndarray = mynp.array([100,200,310.5],dtype=str)
print(myndarray)