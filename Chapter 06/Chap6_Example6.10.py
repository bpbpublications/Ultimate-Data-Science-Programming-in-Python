import matplotlib.pyplot as myplt
myallround_cricketers=['Jacques Kallis','SIr Garifield Sobers','Imran Khan','Ian Botham','Kapil Dev'
                       ,'Sir Richard Hadlee','Sanath Jayasuriya','Andrew Flintoff','Shaun Pollock','Sakib Al Hasan']
my_runs=[25528,8032,7516,7313,9031,4875,21032,7315,7386,11955]
my_wickets=[577,236,544,528,687,589,440,400,829,576]
myplt.bar(myallround_cricketers,my_runs,color='r', label='Runs')
myplt.bar(myallround_cricketers, my_wickets,bottom=my_runs, color='g', label='Wickets')
myplt.xticks(myallround_cricketers, rotation=90)
for i in range(len(myallround_cricketers)):
    myplt.text(myallround_cricketers[i],(my_runs[i]/2),str(my_runs[i]), ha='center',color='black',weight=1000)
    myplt.text(myallround_cricketers[i],(my_runs[i]+my_wickets[i]/2),str(my_wickets[i]), ha='center',color='black',weight=1000)
myplt.legend()
myplt.tight_layout()
myplt.show()
