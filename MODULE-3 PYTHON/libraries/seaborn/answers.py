"""Short Seaborn answers and examples."""
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())
print("Rows and columns:", tips.shape)
print("Average bill:", tips["total_bill"].mean())
print("Average tip:", tips["tip"].mean())
print("Missing values:\n", tips.isnull().sum())
sns.set_theme(style="whitegrid")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Bill Amount and Tip")
plt.tight_layout()
plt.show()

sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Bills by Day")
plt.tight_layout()
plt.show()

sns.heatmap(tips.select_dtypes("number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
