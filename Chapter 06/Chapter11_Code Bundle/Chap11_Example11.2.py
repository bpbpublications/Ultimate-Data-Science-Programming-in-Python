import polars as mypl
import polars.selectors as mysel
mydf = mypl.read_csv("iris.csv")
print("Case1: selection of all columns using '*' and all() method")
# M-1
print(mydf.select(mypl.col('*')).head())
# M-2
#print(mydf.select(mypl.all()).head()) # Just uncomment, run and view the output
print('-'*50)
print("Case2: Some columns can be excluded using exclude  method")
print(mydf.select(mypl.col('*').exclude('sepal.length','petal.length')).head())
print('-'*50)
print("Case3: selection of column using polar data type")
print(mydf.select(mypl.col(mypl.Utf8).n_unique())) # will return the number of unique values in the column
print('-'*50)
print('Case4: selecting the float columns only')
print(mydf.select(mysel.float()))
print('-'*50)
print('Case5: selecting the non-float columns only')
print(mydf.select(~mysel.float()))