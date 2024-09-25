import polars as mypl
import matplotlib.pyplot as myplt
print("Analyzing the iris.csv dataset")
mydf = mypl.read_csv("iris.csv")
print(mydf.shape) # 150 rows and 5 columns
print("display of first 5 rows")
print(mydf.head()) # we can display any number of rows if we pass any argument to head method
print('-'*50)
print("converting the result of head() into a pandas dataframe using to_pandas() function")
print(mydf.head().to_pandas())
print('-'*50)
print(" This code will return the datatypes of the columns of the dataframe")
print(mydf.dtypes)
print('-'*50)
print("--------------------------Selecting and Filtering Data----------------------------------")
print("1. indexing with [  ------------------")
print("display of first row and all the columns")
print(mydf[0,:])
print('-'*50)
print("Requirement to display first 2 rows of column name sepal.length and petal.length only")
print(mydf[:,['sepal.length','petal.length']].head(2))
print('-'*50)
print("Requirement to filter first 3 rows where petal.length is > 2.1 ")
print(mydf.filter(mypl.col('petal.length')>2.1).head(3))
print('-'*50)
print("2. Selecting data with idiomatic polars ---------------------------")
print("Random sample of 5 rows will be selected from a dataframe")
print(mydf.sample(5).to_pandas)
print('-'*50)
print("Selecting sepal.width , petal.width columns and variety columns and display of first 4 rows only")
# Using sql select type of operation for just selecting columns
print(mydf.select(['sepal.width','petal.width','variety']).head(4))
print('-'*50)
print("Add a new column name say Mux10_Petal.Length which is 10 * petal.length and display of only first 3 rows")
# Note if alias name is not written, then the change will happen in petal.length itself 
print(mydf.with_columns([
    (mypl.col('petal.length')*10).alias('Mux10_Petal.Length')
    ]).head(3)) 
print('-'*50)
print("Display of last 5 rows with Setosa variety only")
# The is_in() function is called on the 'variety' column. The is_in() function checks if the values 
# in the column are present in a given list. In this case, it checks if the 'variety' column values
# are in the list ['Setosa'].
print(mydf.filter
      (mypl.col('variety').is_in(['Setosa']))
      .tail())
# Computation performing on the select context
print('-'*50)
print('Calculating the number of unique values in sepal.length column')
print(mydf.select([
    mypl.col('sepal.length').n_unique()
]))
print('-'*50)
print('Performing statistics on the entire sepal.length column')
# This code will provide various statistical measures for the 'sepal.length' column of a dataframe called 'mydf'. 
# It calculates the minimum, mean, median, maximum, and standard deviation of the 'sepal.length' 
# column and renames each calculated value accordingly. 
print(mydf.select([
    mypl.col('sepal.length').min().alias('min_sepal_length'),
    mypl.col('sepal.length').mean().alias('mean_sepal_length'),
    mypl.col('sepal.length').median().alias('median_sepal_length'),
    mypl.col('sepal.length').max().alias('max_sepal_length'),
    mypl.col('sepal.length').std().alias('std_sepal_length')
]))
print('-'*50)
print('Computing statistics at a series level')
print(mydf.select([mypl.col('sepal.length')]).describe())
print('-'*50)
print('Performing data processing in polars and data visualization in pandas')
mysepal_length = mydf.select([
    mypl.col('sepal.length')
    ]) # data processing
# The given code takes a sample of 100 rows from the "mysepal_length" dataset, 
# converts it to a pandas dataframe, and then creates a histogram with 10 bins. 
mysepal_length.sample(100).to_pandas().hist(bins=10) # data visualization
myplt.show()