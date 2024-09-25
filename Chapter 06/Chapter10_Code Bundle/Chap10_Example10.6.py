import polars as mypl
print("Reading the iris.csv dataset and storing the contents in the variable mydf")
mydf = mypl.read_csv("iris.csv")
# Perform multiple expressions using mydf.select
selected_data = mydf.select([
    mypl.col("sepal.length"),
    mypl.col("petal.length"),
    mypl.col("variety")
]).filter(mypl.col("sepal.length") > 5.0).sort("petal.length")
# Display the selected and filtered data
print(selected_data)