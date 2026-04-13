import polars as mypl
print("Creating a list of individual scores made by 5 batsman in 6 innings")
mydf = mypl.DataFrame(
    {
        "batsman": ["Batsman " + str(x) for x in range(5)],
        "runs": [
            "12 45 78 100 156 38",
            "18 116 101 12 70 40",
            "0 35 16 6 12 10",
            "57 15 7 8 10 24",
            "14 16 22 24 45 103",
        ],
    }
)
print(mydf)
print('-'*50)
print('Case1: Creating a list column')
print(mydf.with_columns(mypl.col("runs").str.split(" ")))
print('-'*50)
print('Case2: Performing operations on list columns')
print(mydf.with_columns(mypl.col("runs").str.split(" ")).with_columns(
    mypl.col("runs").list.head(2).alias("MyTop2"),
    mypl.col("runs").list.slice(-2, 2).alias("Mybottom_2"),)) # tail(2) can also be used
print('-'*50)
print('Case4: Computing the Rank of each batsman based on total number of runs')
mydf = mydf.with_columns(
    mypl.col("runs")
    .str.split(" ")
    .list.eval(mypl.element().cast(mypl.Int8, strict=False))
    .list.sum()
    .alias("Total"),
)
# Compute the rank of each batsman based on total number of runs
print(mydf.with_columns(mypl.col("Total").rank(method="dense").alias("Rank")))
print("Case5: Array data type contains same number of elements per row")
print(mypl.DataFrame(
    [
        mypl.Series("MyArr1", [[11, 31], [12, 15]]),
        mypl.Series("MyArr2", [[11, 17, 31], [81, 11, 10]]),
    ],
    schema={
        "MyArr1": mypl.Array(inner=mypl.Int8, width=2),
        "MyArr2": mypl.Array(inner=mypl.Int8, width=3),
    },
))
