import seaborn as mysns
import matplotlib.pyplot as myplt
import pandas as mypd

mycovid_dataset = mypd.read_csv('mycovid_data.csv')
print(mycovid_dataset)
# Selecting only the desired columns
selected_columns = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'Country']
selected_data = mycovid_dataset[selected_columns]

# Creating a pivot table for the heatmap
heatmap_data = selected_data.pivot_table(index='Country')

# Plotting the heatmap
mysns.heatmap(data=heatmap_data, cmap='YlOrRd', annot=True, fmt="0.2f", linewidth=0.4)

myplt.title('Covid Data HeatMap Analysis')
myplt.xlabel('Metrics')
myplt.ylabel('Country')
myplt.show()