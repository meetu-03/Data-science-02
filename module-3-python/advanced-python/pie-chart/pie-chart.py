# Task: Visualize Food Wastage in a Canteen Management System

# Create a Python program using Pandas and Matplotlib to analyze and visualize food wastage in a canteen management system.

# Requirements

# Create a dataset containing:

# Food item name

# Quantity prepared (in kg)

# Quantity consumed (in kg)

# Quantity wasted (in kg)

# Create a Pandas DataFrame from the dataset.

# Calculate the total food wastage for each food item.

# Use a pie chart to visualize the percentage of total food wastage contributed by each food item.

# Display:

# Food item names as labels

# Wasted quantity as the pie-chart values

# Percentage of wastage on each slice

# A suitable chart title such as "Canteen Food Wastage Analysis"

# Display the DataFrame before displaying the chart.

# Expected Output

# The program should display a table containing the canteen food-wastage data and a pie chart showing the proportion of total wastage for each food item.

# Example Food Items

# Rice

# Dal

# Vegetables

# Chapati

# Curry

# Salad

# The objective is to help canteen management identify which food items contribute most to overall food wastage.




import pandas as pd    
import matplotlib.pyplot as pplot


data={
    "food_item" : ["rice","chapati","curry","salad"],
    "food_prepared" :[25,26,27,28,],
    "food_consumed" :[20,21,22,23],
    "food_wasted" : [8,9,10,11]
}



df=pd.DataFrame(data)
print(df)
pplot.pie(
    df["food_wasted"],
    labels=df["food_item"],
    autopct="%1.1f%%",
)
pplot.title("Canteen Food Wastage Analysis")
pplot.show()


