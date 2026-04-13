import polars as mypl
print("Reading the iris.csv dataset and storing the contents in the variable mydf")
mydf = mypl.read_csv("iris.csv")
print('-'*50)
print(mydf.groupby('variety').agg(mypl.count())) 
'''
1. The code starts by calling the 'groupby' function on the dataframe 'mydf' and passing the column name 'variety' as an argument. 
2. This groups the dataframe based on the unique values in the 'variety' column. 
3. Then, the 'agg' function is called on the grouped dataframe, and 'mypl.count()' is passed as an argument. 
4. 'mypl.count()' is a function that counts the number of non-null values in each column of the grouped dataframe. 
5. The 'agg' function applies this counting operation to each group and returns the result. 
6. The resulting dataframe will have the count of non-null values for each column, grouped by the 'variety' column.
'''
print('Computing count and % of Instances')
print(mydf.groupby('variety').agg(mypl.count()).sort('count').with_columns([
    (mypl.col('count')/mypl.col('count').sum()).alias('mypercentage')
])) 
