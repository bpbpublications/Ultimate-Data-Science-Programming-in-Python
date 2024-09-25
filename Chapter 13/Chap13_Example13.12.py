import seaborn as mysns
import matplotlib.pyplot as myplt
my_dataset = mysns.load_dataset('penguins')
myfacet_obj = mysns.FacetGrid(data=my_dataset, row="island", col='sex')
myfacet_obj.map(mysns.histplot, 'bill_length_mm')
myplt.show()

