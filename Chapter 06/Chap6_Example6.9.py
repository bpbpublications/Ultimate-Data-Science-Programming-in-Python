import matplotlib.pyplot as myplt
my_cricketers = ['Sachin', 'Virat', 'Ricky', 'Sangakarra', 'Jacques']
my_centuries = [100, 76, 71, 63, 62] 
mycolorlist = ['r', 'b', 'g', 'pink', 'k']
myplt.barh(my_cricketers, my_centuries, color=mycolorlist)  # horizontal bar chart
myplt.ylabel('Cricketer Name', color='b', fontsize=15)
myplt.xlabel('Number of Centuries', color='g', fontsize=15)
myplt.title('Cricketer-wise Number of Centuries', color='r', fontsize=15)
myplt.xticks(rotation=30)
myplt.tight_layout()
for loop in range(len(my_centuries)):
    myplt.annotate(f'{my_centuries[loop]}C', (my_centuries[loop], loop),
                 ha='center', color='brown', backgroundcolor='yellow')
myplt.show()
