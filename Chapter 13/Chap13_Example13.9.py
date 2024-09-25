import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('iris')
#print(help(mysns.scatterplot))
# set the style as whitegrid
mysns.set(style="whitegrid")  # Set the style of the plot
# Usage of seaborn's scatterplot function
'''
 This line of code is creating a scatter plot using Seaborn, where the x-axis represents sepal length, 
 the y-axis represents sepal width, points are colored based on the species, and different marker styles 
 are used for different species. This allows for the visualization of the relationships between 
 sepal length and width while distinguishing the data points by species.
'''
mysns.scatterplot(x="sepal_length", y="sepal_width", data=my_dataset, hue="species", style="species")
# Set plot labels and title
myplt.title("Scatter Plot of Sepal Length vs Sepal Width")
myplt.xlabel("Sepal Length (cm)")
myplt.ylabel("Sepal Width (cm)")
# Display the plot
myplt.show()