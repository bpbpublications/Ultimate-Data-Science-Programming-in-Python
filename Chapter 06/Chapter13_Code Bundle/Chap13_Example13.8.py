import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('iris')
#print(help(mysns.lineplot))
# Create a lineplot
mysns.lineplot(data=my_dataset, x="sepal_length", y="petal_length", hue="species") # F1
# Display the plot
myplt.show()