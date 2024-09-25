import seaborn as mysns
import matplotlib.pyplot as myplt
# By default n_colors=6 in husl_palette()
# A palette is generated with colors evenly distributed in the HUSL (Hue, Saturation, Lightness) hue space.
# values for parameters h, l and s should be ranged between 0 and 1.
mysns.palplot(mysns.husl_palette(s=0.5, l=0.5))
myplt.show()