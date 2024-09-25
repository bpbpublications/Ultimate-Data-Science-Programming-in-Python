import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('titanic')
mysns.violinplot(data=my_dataset, x='age',y='sex',hue='alive', inner='points')
myplt.title('Violin Plot with comparison of different categories')
myplt.show()