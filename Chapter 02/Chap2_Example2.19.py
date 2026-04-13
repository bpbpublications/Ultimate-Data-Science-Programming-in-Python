# Performance comparison of zeros() and empty() function of numpy
import numpy as mynp
from datetime import datetime
mybegin = datetime.now()
myndarray = mynp.zeros((10000,200,300))
myafter = datetime.now()
print('Time taken by zeros function of numpy is:',myafter-mybegin)

print('-'*50)
myndarray= None
mybegin = datetime.now()
myndarray = mynp.empty((10000,200,300))
myafter = datetime.now()
print('Time taken by empty function of numpy is:',myafter-mybegin)