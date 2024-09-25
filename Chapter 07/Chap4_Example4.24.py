import pandas as mypd
mypd_series = mypd.Series(['Green','Yellow','Blue','Violet'])
for index,value in mypd_series.items():
    print(f'{index} ---> {value}')

    