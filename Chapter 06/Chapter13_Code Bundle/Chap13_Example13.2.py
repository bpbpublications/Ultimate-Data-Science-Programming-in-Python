import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('tips')
#print(help(mysns.kdeplot))
mysns.kdeplot(data=my_dataset, x="total_bill")
myplt.title('kde Plot')
myplt.show()