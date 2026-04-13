import polars as mypl
dtypes = {
    "first_name": mypl.Categorical,
    "gender": mypl.Categorical,
    "type": mypl.Categorical,
    "district": mypl.Categorical
}
mydataset = mypl.read_csv("election_data.csv", dtypes=dtypes).with_columns(
    mypl.col("birthday").str.to_date(strict=False)
)
print(mydataset)
print('-'*50)
mydf = (
    mydataset.lazy()
    .groupby("last_name")
    .agg(
        mypl.count(),
        mypl.col("gender"),
        mypl.first("first_name"),
    )
    .sort("count", descending=True)
    .limit(5)
)
print(mydf.collect())