import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV must contain rating and category columns
df = pd.read_csv("flipkart_reviews.csv")

sns.countplot(data=df, x="rating", color="orange")
plt.title("Flipkart Reviews by Rating")
plt.xlabel("Rating (1 to 5)")
plt.ylabel("Number of Reviews")
plt.show()

# Output: Bar plot showing review counts for ratings 1 to 5.
