import pandas as mypd
import io
mydf = mypd.read_csv('student.csv', index_col = ['id'])
# mydf.info() # we already saw that the result will be displayed to the console
mybuffer = io.StringIO()
mydf.info(buf=mybuffer) # will not be displayed to the console
myvar = mybuffer.getvalue()
with open("df_information.txt",'w',encoding='utf-8') as myfile:
    myfile.write(myvar)
print("View df_information.txt for reading the details")