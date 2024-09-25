import matplotlib.pyplot as myplt

myallround_cricketers = ['Jacques Kallis', 'SIr Garifield Sobers', 'Imran Khan', 'Ian Botham', 'Kapil Dev',
                        'Sir Richard Hadlee', 'Sanath Jayasuriya', 'Andrew Flintoff', 'Shaun Pollock', 'Sakib Al Hasan']

my_runs = [25528, 8032, 7516, 7313, 9031, 4875, 21032, 7315, 7386, 11955]
my_wickets = [577, 236, 544, 528, 687, 589, 440, 400, 829, 576]

fig, ax = myplt.subplots()

# Plot the runs
ax.barh(myallround_cricketers, my_runs, color='r', label='Runs')

# Plot the wickets on top of runs
ax.barh(myallround_cricketers, my_wickets, left=my_runs, color='g', label='Wickets')

ax.set_xlabel('Performance')
ax.set_title('Performance of All-Round Cricketers')
ax.set_xticks(range(0, 30001, 5000))
ax.invert_yaxis()  # Invert the y-axis to display the top performer at the top
ax.legend()

for i in range(len(myallround_cricketers)):
    ax.text(my_runs[i] + my_wickets[i] + 100, i, str(my_wickets[i]), ha='center', va='center', color='black', weight='bold')
    ax.text(my_runs[i] / 2, i, str(my_runs[i]), ha='center', va='center', color='black', weight='bold')

myplt.tight_layout()
myplt.show()


