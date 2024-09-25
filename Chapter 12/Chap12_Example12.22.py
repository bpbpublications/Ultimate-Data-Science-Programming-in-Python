import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('healthexp')
myfiltered_df = my_dataset[my_dataset['Country'] == 'USA']
print(myfiltered_df.head())
mysns.boxplot(data=myfiltered_df,x='Spending_USD',orient="v")
myplt.title('Expenditure Spend on Health')
myplt.show()