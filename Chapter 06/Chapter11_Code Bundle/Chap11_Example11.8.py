import polars as mypl
mydf = mypl.DataFrame(
    {
        "list1": [4,5,6],
        "list2": [10, 100, 1000],
    }
)
print('Case1: Manual multiplication')
'''
-  acc=mypl.lit(1) : This sets the initial value of the accumulator ( acc ) to 1. The accumulator is used to keep track of the intermediate result during the fold operation. 
   -  function=lambda acc, y: acc * y : This defines the function to be applied during the fold operation. In this case, it is a lambda function that multiplies the accumulator ( acc ) with each element ( y ) in the expression. 
   -  exprs=mypl.all() : This specifies that the fold operation should be applied to all columns in the DataFrame. 
  The result of the fold operation is then selected using  mydf.select() . 
'''
print(mydf.select(
    mypl.fold(acc=mypl.lit(1), function=lambda acc, y: acc * y, exprs=mypl.all())
    .alias("mymul")
    ))
print('-'*50)
print('Case2:Filtering all rows where each column value is > 5')
print(mydf.filter(
    mypl.fold(
        acc=mypl.lit(True),
        function=lambda acc, x: acc & x,
        exprs=mypl.all() > 5,
    )
))
print('-'*50)
print('Case3:Performing concatenation element wise')
print(mydf.select(mypl.concat_str(["list1", "list2"])))
print('-'*50)
print('Case3:Performing addition element wise')
print(mydf.select(mypl.sum(["list1", "list2"])))