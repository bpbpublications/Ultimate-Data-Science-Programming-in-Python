import matplotlib.pyplot as myplt
#print(help(myplt.hist))

# Data
# Two lists are created: mymarks_ranges contains the ranges of marks, and 
# mynum_students contains the number of students falling within each range. 
mymarks_ranges = ["0-34", "35-49", "50-59", "60-79", "80-100"]
mynum_students = [35, 100, 45, 68, 27]

# Calculate the midpoints of each range for the x-axis labels
# The midpoints of each mark range are calculated and stored in the mymidpoints list. 
mymidpoints = [(0 + 34) / 2, (35 + 49) / 2, (50 + 59) / 2, (60 + 79) / 2, (80 + 100) / 2]

# Create a histogram
# The hist() function is called to create the histogram. It takes several arguments: 
# - mymidpoints: the values to be plotted on the x-axis. 
# - bins: the range of values for each bin/bar in the histogram. 
# - weights: the weights or frequencies of each value. 
# - edgecolor: the color of the edges of the bars in the histogram. 
# - color: the color of the bars in the histogram. 

myplt.hist(mymidpoints, bins=[0, 35, 50, 60, 80, 100], weights=mynum_students, edgecolor='black'
           , color='skyblue')

# Set axis labels and title
# The xlabel(), ylabel(), and title() functions are used to set the 
# labels and title of the plot. 

myplt.xlabel('Marks Range')
myplt.ylabel('Number of Students')
myplt.title('Distribution of Marks for 300 Students')

# Set x-axis labels
# The xticks() function is used to set the x-axis labels to the values in mymarks_ranges. 
myplt.xticks(mymidpoints, mymarks_ranges)

# Display the histogram
myplt.show()
