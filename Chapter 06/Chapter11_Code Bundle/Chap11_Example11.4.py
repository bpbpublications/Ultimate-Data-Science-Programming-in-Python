import polars as mypl
mydf = mypl.DataFrame(
    {
        "myint_col":[10,0,12,-11,14],
        "mybigint_col":[10010000,5,30030000,40040000,11],
        "myfloat_col":[12.0,15.0,18.0,21.0,24.0],
        "myfloat_decimal":[12.11,15.22,18.33,21.44,24.55],
        "myfloat_string":["12.11","15.22","18.33","21.44","24.55"],
        "mydate_string": [
            "2023-11-01",
            "2023-11-02",
            "2023-11-03",
            "2023-11-04",
            "2023-11-05",
        ]
    }
)
print(mydf)
print('-'*50)
print('Case1: Casting operations between integer and float')
print(mydf.select(
    mypl.col("myint_col").cast(mypl.Float32).alias("myint_as_floats"),
    mypl.col("myfloat_decimal").cast(mypl.Int32).alias("myfloat_decimal_as_integers"),
))
print('-'*50)
print('Case2: Checking whether it can be casted to a smaller data type or not')
try:
    print(mydf.select(mypl.col("mybigint_col").cast(mypl.Int16)))
except Exception as mye:
    print(mye)
print('-'*50)
print('Case3: Checking whether it can be casted to a smaller data type or not by making strict parameter to false')
print(mydf.select(mypl.col("mybigint_col").cast(mypl.Int16, strict=False))) # The overflowing values will be assigned to null
print('-'*50)
print('Case4: Casting numerical data types to string and vice-versa')
print(mydf.select(
    mypl.col("myfloat_string").cast(mypl.Float64),
    mypl.col("myfloat_col").cast(mypl.Utf8)
))
print('-'*50)
print('Case5: Casting integer values to boolean')
print(mydf.select(
    mypl.col("myint_col").cast(mypl.Boolean)
))
print('-'*50)
print('Case6: Convert string values to date')
print(mydf.select(
    mypl.col("mydate_string").str.to_datetime("%Y-%m-%d")
))