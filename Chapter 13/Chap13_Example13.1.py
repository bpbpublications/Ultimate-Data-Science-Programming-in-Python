import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('tips')
#print(help(mysns.histplot))
mysns.histplot(data=my_dataset, x="total_bill", kde=False)
myplt.title('Histogram Plot')
myplt.show()