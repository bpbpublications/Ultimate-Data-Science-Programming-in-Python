import polars as mypl
# Create a Series from a list of integers
myseries = mypl.Series("mynumbers", [11, 12, 13, 14, 15])
# Access values and perform operations on the Series
print(myseries)
print(myseries.sum())