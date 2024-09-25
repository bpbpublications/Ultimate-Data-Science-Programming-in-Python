import polars as mypl
import numpy as mynp
mydf = mypl.DataFrame({"mynum1": [2, 4, 6], "mynum2": [1, 3, 5]})
# Element-wise functions
print(mydf.select(
    mynp.exp(mypl.col("mynum1")).alias("_exp1"),
    mynp.exp(mypl.col("mynum2")).alias("_exp2")
))
print('-'*50)
print(mydf.select(
    mynp.sin(mypl.col("mynum1")).alias("_sin1"),
    mynp.sin(mypl.col("mynum2")).alias("_sin2")
))
print("-"*50)
# # Vectorized function
print(mydf.select(
    mynp.degrees(mypl.col("mynum1")).alias("_degrees1"),
    mynp.degrees(mypl.col("mynum2")).alias("_degrees2")
))
# We can even perform aggregate functions like sim, min, max, mean, median
