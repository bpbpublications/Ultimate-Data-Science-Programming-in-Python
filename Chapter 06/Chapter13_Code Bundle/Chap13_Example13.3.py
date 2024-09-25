import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('iris')
mysns.kdeplot(data=my_dataset.loc[my_dataset.species=="versicolor"], 
              x="sepal_length", y="petal_length", cmap='Greens',
              cbar=True, n_levels=20)
myplt.title('Bivariate kde Plot')
myplt.show()
