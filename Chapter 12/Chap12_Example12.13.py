import seaborn as mysns
import matplotlib.pyplot as myplt
# print(help(mysns.diverging_palette))
mysns.palplot(mysns.diverging_palette(h_neg=250, h_pos=300,n=7, s=60,l=50, sep=5,center='light'))
myplt.show()