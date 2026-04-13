import polars as mypl
from datetime import datetime
mydf = mypl.DataFrame(
    {
        "myint": [11, 12, 13, 14, 15],
        "mydate": [
            datetime(2023, 11, 11),
            datetime(2023, 11, 12),
            datetime(2023, 11, 13),
            datetime(2023, 11, 14),
            datetime(2023, 11, 15),
        ],
        "myfloat": [4.0, 5.0, 6.0, 7.0, 8.0],
        "mycity": ['Hyderabad', 'Delhi', 'Durg', 'Bhilai', 'Raipur']
    }
)
print(mydf)
# head: will return the first 5 rows of a dataframe as default and can specify the number of rows we want by inserting some number other than default value of 5
print(mydf.head(2))
# tail: will return the last 5 rows of a dataframe as default and can specify the number of rows we want by inserting some number other than default value of 5
print(mydf.tail(2))
# sample: will return 'n' number of random rows from the dataframe
print(mydf.sample(2))
# describe: will return quick summary statistics of the dataframe
print(mydf.describe())