import seaborn as sns
import matplotlib.pyplot as plt

# Load Seaborn tips dataset
tips = sns.load_dataset("tips")

sns.boxplot(data=tips, x="day", y="total_bill", color="skyblue")
plt.title("Total Bill Amount by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# Output: Boxplot showing total bill distribution for each day.
