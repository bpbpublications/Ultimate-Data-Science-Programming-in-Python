import polars as mypl
print("Reading the iris.csv dataset and storing the contents in the variable mydf")
mydf = mypl.read_csv("iris.csv")
# Define a lazy computation plan
mylazy_plan = mydf.lazy().select([
    mypl.col("sepal.length"),
    mypl.col("petal.length"),
    mypl.col("variety")
]).filter(mypl.col("sepal.length") > 5.0).sort("petal.length")
# Execute the computation plan and get the result
myresult = mylazy_plan.collect(streaming=True)
# Display the result
print(myresult)