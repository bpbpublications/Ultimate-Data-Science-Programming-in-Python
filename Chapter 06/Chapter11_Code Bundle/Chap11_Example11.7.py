import polars as mypl
mydf = mypl.DataFrame({"values":[11,None,0,False,None,12]})
print('Case1: Displaying the dataframe object')
print(mydf)
print('-'*50)
print('Case2:First piece of metadata')
mydf_null_count = mydf.null_count() # display of number of rows with null values in the columns
print(mydf_null_count)
print('-'*50)
print('Case3:validity bitmap used by is_null method indicating whether each data value is null or not')
print(mydf.select(
    mypl.col("values").is_null()
))
print('-'*50)
print('Case4:Filling the missing data with a specified literal value using mypl.lit] using fill_null method')
print(mydf.select(
    mypl.col("values").fill_null(mypl.lit(3))
))
print('-'*50)
print('Case5:Filling the missing data with a strategy by setting it as backward here using fill_null method')
print(mydf.select(
    mypl.col("values").fill_null(strategy='backward')
))
print('-'*50)
print('Case6:Filling the missing data with an expression using fill_null method')
print(mydf.select(
    mypl.col("values").fill_null(mypl.mean("values")) # (11+0+0(False)+12/4)
))
print('-'*50)
print('Case7:Filling the missing data with an interpolation using interpolate function')
print(mydf.select(
    mypl.col("values").interpolate())
)