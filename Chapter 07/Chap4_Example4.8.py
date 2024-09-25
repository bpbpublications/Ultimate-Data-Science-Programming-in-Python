import pandas as mypd
myseries=mypd.Series([loop for loop in range(20)])
# head method
print(myseries.head())
print(myseries.head(n=2))
# tail method
print(myseries.tail())
print(myseries.tail(n=-18)) # equivalent to print(myseries.tail(n=2)) , it will return last 2 rows