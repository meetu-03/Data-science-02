
# Create a Pandas DataFrame containing at least 8 products and their sales quantities.

# - Calculate the total quantity sold.
# - Identify the top 3 best-selling products.
# - Create a **pie chart using Matplotlib** showing the sales distribution among the products.

# ---

import pandas as pd
import matplotlib.pyplot as plt


data={
    "employee": ["faize", "raj", "meet","sahil","rajan"],
    "sales": [100, 200, 150, 300, 250]
}


df=pd.DataFrame(data)

print(df)
print("--------------------------------------")
print("total quantity sold:",df["sales"].sum())
print("--------------------------------------")
print("top 3 ",df.nlargest(3, "sales"))
print("-------------------------------------")


plt.pie(df["sales"], labels=df["employee"],
        autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution Among Employees")
plt.show()