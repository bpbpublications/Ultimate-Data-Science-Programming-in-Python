import pandas as mypd
# Read the CSV file and select both 'Employee Name' and 'Salary' columns
mydf = mypd.read_csv('employees_salary2.csv', usecols=['Employee Name', 'Salary'])
print(mydf)
# Replace 'NA' values with '12345' in the 'Salary' column
mydf['Salary'] = mydf['Salary'].fillna(12345)
# Convert the DataFrame into a Series object with 'Employee Name' as the index
myseries = mydf.set_index('Employee Name')['Salary']
# Display the resulting Series object
print(myseries)
print(type(myseries))
