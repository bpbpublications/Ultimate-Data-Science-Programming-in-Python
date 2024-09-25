import pandas as mypd
import numpy as mynp
mypd_series = mypd.Series(['Green','Yellow','Blue','Violet'])
#print(help(mypd_series.map))

# Using dict
mynewpd_series = mypd_series.map({'Green':'Pink','Blue':'Magenta'})
print(mynewpd_series) # there is no replacement for Yellow and Violet color hence converted to NaN

# Using lambda function
my_series_func = mypd_series.map(lambda x: f" I love {x} color ")
print(my_series_func)

# using na_action parameter
def myfunc(x):
    return f'I love {x} color '
mypd_series3 = mypd.Series(['Green','Yellow',mynp.NaN,'Violet'])
my_series_func2 = mypd_series3.map(myfunc, na_action='ignore') # for keeping as NaN, na_action parameter is used so as to avoid applying the function to missing values
print(my_series_func2)