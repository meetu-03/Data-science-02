
# ## Task 5: Temperature Analysis

# Create a Pandas DataFrame containing the daily temperatures recorded for 15 days.

# - Calculate the maximum temperature.
# - Calculate the minimum temperature.
# - Calculate the average temperature.
# - Identify the days where the temperature was above the average.
# - Create a **line plot using Matplotlib** showing the temperature variation over the 15 days.

import pandas as pd
import matplotlib.pyplot as plt

data={
    "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "temperature": [15.1, 15.3, 15.5, 15.7, 15.9, 16.0, 16.2, 16.4, 16.6, 16.8, 17.0, 17.2, 17.4, 17.6, 17.8]



}

df=pd.DataFrame(data)

print(df)
print("--------------------------------------------")
print("maximum temprature :",df["temperature"].max())
print("--------------------------------------------")
print("minimum temperature :",df["temperature"].min())
print("--------------------------------------------")
print("average temperature :",df["temperature"].mean())
print("--------------------------------------------")
highest_temp_above_avg=df[df["temperature"]>df["temperature"].mean()]
print("highest temperature above average:")
print(highest_temp_above_avg)

plt.plot(df["day"], df["temperature"])
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Temperature Variation Over Days")
plt.show()