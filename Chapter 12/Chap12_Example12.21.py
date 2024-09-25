import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('healthexp')
#print(help(mysns.boxplot))
print(my_dataset.head())
mysns.boxplot(data=my_dataset,x='Spending_USD',orient='v')
myplt.title('Expenditure Spend on Health')
myplt.show()