import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('exercise')
#print(help(mysns.violinplot))
mysns.violinplot(my_dataset['pulse'])
myplt.title('Violin Plot')
myplt.show()