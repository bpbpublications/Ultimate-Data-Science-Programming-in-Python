import polars as mypl
mydf = mypl.read_csv("iris.csv")
print('Case1: Usage of try except block if trying to use the same column multiple times in the expression')
try:
    print(mydf.select(mypl.col('sepal.length')+2 , mypl.col('sepal.length')-2 ))
except Exception as mye:
    print("Exception...")
    print(mye)
print('-'*50)
print('Case2: Removing length word from sepal.length and petal.length columns only and exclude other columns and converting it into upper case using map_alias')
# The  map_alias  method is used in the provided code to modify the column names of the DataFrame  mydf  during the  select  operation. 
print(mydf.select(mypl.col('*').exclude('variety','sepal.width','petal.width').map_alias(lambda c: c.rstrip("length").replace(".","").upper())))
print('Case3: Support of if else-condition in polars using when, then and otherwise syntax')
'''
The when clause contains the predicate, 
and if it evaluates to true, the then expression is applied; 
otherwise, the otherwise expression is applied.
ALos, .lit function is used to create a literal value which will be used as 
the results of the conditional expression within the  when  and  otherwise  clauses. 
'''
mydf_conditional = mydf.select(
    mypl.col("sepal.length"),
    mypl.when(mypl.col("sepal.length") > 4.7)
    .then(mypl.lit(True))
    .otherwise(mypl.lit(False))
    .alias("Condition_Check_Sepal_Length"),
)
print(mydf_conditional.head())