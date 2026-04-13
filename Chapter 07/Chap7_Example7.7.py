import pandas as mypd
import numpy as mynp
myndarray = mynp.array([11,12,13,14])
myseries = mypd.Series(myndarray, copy=False)
myseries[1] = 32
print("When copy=False, no separate copy is created. myseries data is ")
print(myseries)
print(f"When copy=False, myndarray data is {myndarray}")

myndarray2 = mynp.array([11,12,13,14])
myseries2 = mypd.Series(myndarray2, copy=True)
myseries2[1] = 32
print("When copy=True, Separate copy is created. myseries data is ")
print(myseries2)
print(f"When copy=True, myndarray data is {myndarray2}")
