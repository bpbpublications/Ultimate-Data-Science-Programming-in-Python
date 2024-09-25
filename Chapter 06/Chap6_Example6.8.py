import matplotlib.pyplot as myplt
my_cricketers = ['Sachin','Virat','Ricky','Sangakarra','Jacques'] # x-axis values
my_centuries = [100,76,71,63,62] #height of bars, y-axis values
mycolorlist=['r','b','g','pink','k']
myplt.bar(my_cricketers,my_centuries, color=mycolorlist) # right alignment
myplt.xlabel('Cricketer Name',color='b',fontsize=15)
myplt.ylabel('Number of Centuries',color='g',fontsize=15)
myplt.title('Cricketer wise number of centuries',color='r',fontsize=15)
myplt.xticks(my_cricketers, rotation=30)
myplt.tight_layout()
#print(help(myplt.annotate))
for loop in range(len(my_centuries)):
    myplt.annotate(f'{my_centuries[loop]}C',(my_cricketers[loop],my_centuries[loop]+5),
                   ha='center',color='brown',backgroundcolor='yellow')
myplt.show()