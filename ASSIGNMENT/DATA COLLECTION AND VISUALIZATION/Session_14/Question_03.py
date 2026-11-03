import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV must contain average_cost_for_two and user_rating
df = pd.read_csv("zomato_restaurants.csv")

sns.scatterplot(data=df, x="average_cost_for_two", y="user_rating")
plt.title("Restaurant Cost vs User Rating")
plt.xlabel("Average Cost for Two")
plt.ylabel("User Rating")
plt.show()

# Output: Scatterplot showing restaurant cost against user rating.
