
# ## Task 2: Monthly Sales Analysis

# Create a Pandas DataFrame containing monthly sales data for 12 months.

# - Calculate the total annual sales.
# - Find the month with the highest sales.
# - Find the month with the lowest sales.
# - Create a **line plot using Matplotlib** to visualize the monthly sales trend.



import pandas as pd
import matplotlib.pyplot as ptl


data={
    "months":["january","febuary","march","aprile","may","june","july","august","september","octorber","november","december"],
    "sales":[11000,11500,12000,12500,13000,12300,14000,14500,11000,15500,9000,16500],

}

df=pd.DataFrame(data)
sales = df["sales"]

print(df)

print("---------------------------------------------")
print("Total annual sales:", sales.sum())
print("----------------------------------------------")
print("Month which has highest sales:", df["months"][sales.idxmax()])
print("----------------------------------------------")
print("Month which has lowest sales:", df["months"][sales.idxmin()])


ptl.plot(df["months"], df["sales"])
ptl.title("Monthly Sales Trend")
ptl.xlabel("Months")
ptl.ylabel("Sales") 

ptl.show()