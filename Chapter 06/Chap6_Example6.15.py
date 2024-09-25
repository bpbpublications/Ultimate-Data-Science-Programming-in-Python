import matplotlib.pyplot as myplt
import numpy as mynp
import matplotlib.patches as mpatches

#print(help(myplt.scatter))

# Xaxis and Yaxis data
my_xaxis_data = mynp.arange(1,6)
my_yaxis_data = [20,10,60,30,80]

# for each markers displaying different color
# if huge number of colors required, cmap maps colors to numbers
mycolors=['r','b','g','k','y']

# for change of size of each marker
mysize=[100,200,300,400,500]

# Addition of labels using annotate function
mylabels=['L1','L2','L3','L4','L5']
for loop, label in enumerate(mylabels):
    myplt.annotate(label,(my_xaxis_data[loop]+0.2,my_yaxis_data[loop]))

# scatter function
myscatter = myplt.scatter(my_xaxis_data,my_yaxis_data, c=mycolors, s=mysize)

# creating a list of  Patch  objects representing each marker 
# and use it as an argument in the  legend()  function. 
mylegend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(mycolors, mylabels)]

# Displaying the legend
myplt.legend(handles=mylegend_patches)
myplt.show()