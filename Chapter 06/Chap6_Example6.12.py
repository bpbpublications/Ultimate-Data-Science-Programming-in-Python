import matplotlib.pyplot as myplt
import numpy as mynp
myallround_cricketers=['Jacques Kallis','SIr Garifield Sobers','Imran Khan','Ian Botham','Kapil Dev'
                       ,'Sir Richard Hadlee','Sanath Jayasuriya','Andrew Flintoff','Shaun Pollock','Sakib Al Hasan']
my_runs=[25528,8032,7516,7313,9031,4875,21032,7315,7386,11955]
my_wickets=[577,236,544,528,687,589,440,400,829,576]
myxpos=mynp.arange(len(myallround_cricketers))
mywidth=0.3
myplt.bar(myxpos,my_runs,color='r', label='Runs', width=mywidth)
myplt.bar(myxpos + mywidth, my_wickets, color='g', label='Wickets', width=mywidth)
myplt.xticks(myxpos+(mywidth/2),myallround_cricketers, rotation=90)
myplt.legend(['Runs','Wickets'])

for i in range(len(myallround_cricketers)):
    myplt.text(myxpos[i], my_runs[i] + 10 , my_runs[i], ha='center', color='black', weight=1000)
    myplt.text(myxpos[i]+mywidth, my_wickets[i] + 5 , my_wickets[i], ha='center', color='black', weight=1000)

myplt.tight_layout()
myplt.show()