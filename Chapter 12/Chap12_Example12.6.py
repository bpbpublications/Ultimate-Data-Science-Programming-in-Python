import seaborn as mysns
import matplotlib.pyplot as myplt
# print(help(mysns.color_palette))
mycolor_palette = mysns.color_palette()
print(mycolor_palette)
# This line calls the  color_palette  function from  seaborn  with the argument  desat=0  
# to create a color palette with no saturation. The  palplot function then displays the color
# palette.
mysns.palplot(mysns.color_palette(desat=0))
myplt.show()