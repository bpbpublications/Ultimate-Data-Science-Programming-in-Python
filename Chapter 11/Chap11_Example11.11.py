import pandas as mypd
import polars as mypl
import time
# Reading csv file in pandas
mypd_df = mypd.read_csv("iris.csv")
# Reading csv file in polars
mydf = mypl.read_csv("iris.csv")
print("Case1: Displaying first 3 rows using pandas")
print(mypd_df.head(3))
print("Case1: Displaying first 3 rows using polars")
print(mydf.head(3))
print('-'*50)
print("Case2: Displaying Dimensions using pandas")
print(mypd_df.shape)
print("Case2: Displaying Dimensions using polars")
print(mydf.shape)
print('-'*50)
print("Case3: Displaying datatype using pandas")
print(mypd_df.dtypes)
print("Case3: Displaying datatype using polars")
print(mydf.dtypes)
print('-'*50)
print("Case4: Columns selection using pandas")
print(mypd_df[["sepal.length","petal.length"]])
print("Case4: Columns selection using polars")
print(mydf[["sepal.length","petal.length"]])
print('-'*50)
print("Case5: Filtering Data using pandas")
print(mypd_df[mypd_df['variety'].isin(['Versicolor'])].head())
print("Case5: Filtering Data using polars")
print(mydf.filter(mypl.col('variety') == "Versicolor").head())
print('-'*50)
print("Case6: Sorting using pandas")
print(mypd_df.sort_values("variety", ascending=False))
print("Case6: Sorting using polars")
print(mydf.sort("variety", descending=True))
print('-'*50)
mydict1 = { 'staffno': [12, 13,14,15],
           'salary': [100000,200000,300000,400000]}
mydict2 = { 'staffno': [12, 13,17,18],
           'salary': [110000,220000,303030,404040]}
print("Case7: Join using pandas")
# Convert dictionaries to DataFrames
mypd_df1 = mypd.DataFrame(mydict1)
mypd_df2 = mypd.DataFrame(mydict2)
# Perform the merge
print(mypd_df1.merge(mypd_df2, on="staffno", how="inner"))
print("Case7: Join using polars")
# Convert dictionaries to DataFrames
mypl_df1 = mypl.DataFrame(mydict1)
mypl_df2 = mypl.DataFrame(mydict2)
# Perform the join
print(mypl_df1.join(mypl_df2, on="staffno", how="inner"))
print('-'*50)
print("Case8: Concatenate using pandas")
print(mypd.concat(
    [
        mypd_df1,
        mypd_df2,
    ],
    axis=0,
))
print("Case8: Concatenate using polars")
print(mypl.concat(
    [
        mypl_df1,
        mypl_df2,
    ],
    how="vertical",
))
print('-'*50)
print("Case9: Group using pandas")
print(mypd_df.groupby("variety")["sepal.length"].mean())
print("Case9: Group using polars")
print(mydf.groupby("variety").agg(mypl.mean("sepal.length")))
print('-'*50)
print("Case10: Rename column using pandas")
print(mypd_df.rename(columns={"sepal.length": "Mysepal.length"}).head())
print("Case10: Rename column using polars")
print(mydf.rename(mapping={"sepal.length": "Mysepal.length"}).head())
print('-'*50)
print("Case11: Delete column using pandas")
print(mypd_df.drop(columns=["petal.length"]).head())
print("Case11: Delete column using polars")
print(mydf.drop(columns=["petal.length"]).head())
print('-'*50)
# Reading csv file in pandas
start = time.time()
mypd_df = mypd.read_csv("election_results_2014.csv")
end = time.time()
print(f"Pandas took {end - start:.7f} seconds to read the file")
# Reading csv file in polars
start = time.time()
mydf = mypl.read_csv("election_results_2014.csv")
end = time.time()
print(f"Polars took {end - start:.7f} seconds to read the file")