import matplotlib.pyplot as myplt
import numpy as mynp
myplt.figure(num=1,figsize=(8,4),facecolor='green')
myndarray = mynp.arange(1,6)
myplt.plot(myndarray,myndarray,'o-r')
myplt.show()
