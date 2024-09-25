import seaborn as mysns
import matplotlib.pyplot as myplt
# Load the exercise dataset from seaborn
my_dataset = mysns.load_dataset('exercise')
# Create a violin plot
mysns.violinplot(my_dataset['pulse'])
# Calculate summary statistics
summary_stats = my_dataset['pulse'].describe()
q1 = summary_stats['25%']
q3 = summary_stats['75%']
myiqr = q3 - q1
minimum = summary_stats['min']
maximum = summary_stats['max']
median = summary_stats['50%']
print(summary_stats['mean'])
# Calculate range excluding outliers
mylower_bound = q1 - 1.5 * myiqr
myupper_bound = q3 + 1.5 * myiqr
range_without_outliers = myupper_bound - mylower_bound
print(f"q1 value is {q1}")
print(f"q3 value is {q3}")
print(f"iqr value is {myiqr}")
print(f"minimum value is {minimum}")
print(f"maximum value is {maximum}")
print(f"median value is {median}")
print(f"lower_bound value is {mylower_bound}")
print(f"upper_bound value is {myupper_bound}")
print(f"range_without_outliers value is {range_without_outliers}")
# Add text annotations for summary statistics
# print(help(myplt.text))
myplt.text(0.1, q1 - 3, f'Q1: {q1}', ha='center', va='bottom', color='red')
myplt.text(0.1, q3 + 3, f'Q3: {q3}', ha='center', va='top', color='red')
myplt.text(0.1, q1 + 0.1 * myiqr, f'IQR: {myiqr}', ha='center', va='bottom', color='red')
myplt.text(0.1, minimum - 5, f'Min: {minimum}', ha='center', va='bottom', color='red')
myplt.text(0.1, maximum + 5, f'Max: {maximum}', ha='center', va='top', color='red')
myplt.text(0.1, median + 2, f'Median: {median}', ha='center', va='bottom', color='red')
myplt.text(0.1, myupper_bound + 2, f'Range (no outliers): {range_without_outliers}', ha='center', va='bottom', color='red')
# Set plot title
myplt.title('Violin Plot with Summary Statistics')
# Add grid
myplt.grid(axis='y', linestyle='--', alpha=0.7)
# Show the plot
myplt.show()
