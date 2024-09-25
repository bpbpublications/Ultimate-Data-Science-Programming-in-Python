import matplotlib.pyplot as myplt
import numpy as mynp
# print(help(myplt.pie))
my_lang_popularity= mynp.array([40,32,18,15,12]) # some random value
# addition of labels to the wedges
mylang_labels = ['Python','Java','C#.Net','C','VB.Net']
# * autopct function: For labelling widgets with numeric percentage and specifying its value 
# using formatted string: autopct = '%.2f': considering 2 digits after decimal point
# with addition of % symbol using wild character for formatted string so using autopct = '%.2f%%'

myautopct = '%.2f%%'
# * explode: For highlighting a particular category we will be using explode argument.
myexplode = [0.2,0.0,0.0,0.0,0.0]

# * shadow = shadow effect can be added to the pie chart using shadow effect by setting value to True.
myshadow = True

# * colors = colors can be specifed for the wedges using list or array with color name or hex code.
# if colors number is < wedges number , then the colors will be reused.
my_list_color=['r','b','g','pink','#8B00FF']

# * startangle: wedge will start from 0 from x-axis and will move in counter clockwise direction
# a number will be specified from which wedge will start. Here, we are specifying value with 90
mystartangle=90

# * wedgeprops= pie chart wedges can be customised using wedgeprops and
# keys in the form of key-value pairs can be edgecolor, linestyle or linewidth
mywedgeprop_para={'edgecolor':'k','linestyle':'--'} # try increase the linewidth say 2 and check 

# pie chart creation
myplt.pie(my_lang_popularity, labels=mylang_labels,autopct = myautopct, explode=myexplode,
          shadow=myshadow, colors=my_list_color, startangle=mystartangle, wedgeprops = mywedgeprop_para)

# addition of legend
myplt.legend(title='Languages Popularity Pie chart')
myplt.tight_layout()
myplt.show()