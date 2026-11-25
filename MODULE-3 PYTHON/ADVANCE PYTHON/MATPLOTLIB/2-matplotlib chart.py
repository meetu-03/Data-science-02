
# crete a datat farme usning pandas to plotdata on chart
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales_INR": [45000, 52000, 49000, 61000, 58000, 72000],
    "Expenses_INR": [30000, 32000, 31000, 35000, 34000, 39000],
}

df=pd.DataFrame(data)
print(df)


# matplotlib provides pie,bar,line chart etc.

# BAR CHART


# plt.figure(figsize=(5,5))
# plt.bar(df["Month"], df["Sales_INR"])
# plt.xlabel("Month")
# plt.ylabel("Sales_INR")

# plt.show()



# PLOT CHART (LINE)

# plt.figure(figsize=(5,5))
# plt.plot(df["Month"], df["Sales_INR"],marker="o",colour="blue")
# plt.xlabel("Month")
# plt.ylabel("Sales_INR")
# plt.grid(True)

# plt.show()

# pie chrt


# plt.pie(df["Month"],df["Sales_INR"],labels=df["Month"],autopct="%1.1f%%",startangle=140)


        
# plt.show()


# DYNEMIC CHART PLOT OF DATA SET

import random

fig, ax = plt.subplots(figsize=(10, 6))


# create a fuction for update chart

def update(frame):
    # Clear the previous frame and show sales with a small random variation.
    ax.clear()
    sales = [value + random.randint(-5000, 5000) for value in df["Sales_INR"]]
    ax.plot(df["Month"], sales, marker="o", color="blue", label="Sales (INR)")
    ax.set_title("Monthly Sales (Dynamic)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales (INR)")
    ax.grid(True)
    ax.legend()


animation = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
plt.tight_layout()
plt.show()
