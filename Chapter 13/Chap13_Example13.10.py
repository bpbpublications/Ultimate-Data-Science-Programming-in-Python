import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('iris')
#print(help(mysns.jointplot))
mysns.jointplot(x="sepal_length", y="sepal_width", data=my_dataset, hue="species")
# Set plot labels and title
myplt.title("Joint Plot of Sepal Length vs Sepal Width")
myplt.xlabel("Sepal Length (cm)")
myplt.ylabel("Sepal Width (cm)")
# Display the plot
myplt.show()