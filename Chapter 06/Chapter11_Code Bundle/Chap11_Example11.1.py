import polars as mypl
print("Reading the iris.csv dataset and storing the contents in the variable mydf")
mydf = mypl.read_csv("iris.csv")
# numerical 
mydf_numerical = mydf.select(
    mypl.col("sepal.length"),
    mypl.col("petal.length"),
    (mypl.col("sepal.length") + 5).alias("sepal.length + 5"),
    (mypl.col("sepal.length") - 5).alias("sepal.length - 5"),
    (mypl.col("sepal.length") * mypl.col("petal.length")).alias("sepal.length * petal.length"),
    (mypl.col("sepal.length") / mypl.col("petal.length")).alias("sepal.length / petal.length"),
)
print(mydf_numerical.head())
print('-'*50)
# logical
mydf_logical = mydf.select(
    mypl.col("sepal.width"),
    mypl.col("petal.width"),
    (mypl.col("sepal.width") >3.2).alias("sepal.width_Greater"),
    (mypl.col("petal.width") == 0.2).alias("petal.width_check"),
)
print(mydf_logical.head())