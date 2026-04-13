import pandas as mypd
# creating a Pandas Series
mypd_series = mypd.Series([loop for loop in range(10)])

def my_even_number_selection(myseries):
    return [True if loop%2==0 else False for loop in range(myseries.size)]

print("Approach-1--------------------------")
print(mypd_series[my_even_number_selection]) 

print("Approach-2--------------------------")
print(mypd_series.loc[lambda myseries: [True if loop%2==0 else False for loop in range(myseries.size)]]) 

print("Approach-3--------------------------")
print(mypd_series.iloc[lambda myseries: [True if loop%2==0 else False for loop in range(myseries.size)]]) 

print("Approach-4--------------------------")
print(mypd_series.get(lambda myseries: [True if loop%2==0 else False for loop in range(myseries.size)])) 
