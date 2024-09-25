import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('iris')
#print(help(mysns.distplot))
mysns.distplot(my_dataset['petal_length'],hist=False)
myplt.title('Univariate kde Plot using distplot() function')
myplt.show()