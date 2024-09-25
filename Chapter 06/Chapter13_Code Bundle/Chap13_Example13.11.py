import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('penguins')
# print(help(mysns.FacetGrid))
myfacet_obj = mysns.FacetGrid(data=my_dataset, col="island")
myfacet_obj.map(mysns.histplot, 'bill_length_mm')
myplt.show()