import seaborn as mysns
import matplotlib.pyplot as myplt
mycolor_palette = mysns.color_palette(n_colors=6)
print(mycolor_palette)
# This line will plot by default 6 colors.
mysns.palplot(mycolor_palette)
myplt.show()