import seaborn as mysns
import matplotlib.pyplot as myplt
# By default n_colors=6 in hls_palette()
# A palette is generated with colors evenly distributed in the HLS (Hue, Lightness, Saturation) hue space.
# values for parameters h, l and s should be ranged between 0 and 1.
mysns.palplot(mysns.hls_palette(h=0.5, l=0.3, s=0.5))
myplt.show()