"""Short NumPy answers and examples."""
import numpy as np

array = np.array([1, 2, 3, 4])
matrix = np.arange(1, 10).reshape(3, 3)
print("Array:", array)
print("Shape:", matrix.shape)
print("Mean:", array.mean())
print("Sum:", array.sum())
print("Maximum:", array.max())
print("Minimum:", array.min())
print("Array plus five:", array + 5)
print("Squared values:", array ** 2)
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Matrix transpose:\n", matrix.T)
random_values = np.random.default_rng(1).integers(1, 10, size=5)
print("Random values:", random_values)
print("Even values:", array[array % 2 == 0])
print("Zeros:", np.zeros((2, 3)))
print("Ones:", np.ones(4))
print("Reshaped array:", array.reshape(2, 2))
*** Add File: D:/data science all theory notes/MODULE-3 PYTHON/libraries/pandas/answers.py
"""Short Pandas answers and examples."""
import pandas as pd

data = {"Name": ["Asha", "Ravi", "Neha"], "Marks": [85, 72, 91]}
df = pd.DataFrame(data)
print(df)
print("Columns:", list(df.columns))
print("Rows and columns:", df.shape)
print("First row:\n", df.head(1))
print("Average marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
df["Result"] = df["Marks"].apply(lambda mark: "Pass" if mark >= 40 else "Fail")
print("With result:\n", df)
print("Passed students:\n", df[df["Result"] == "Pass"])
df = df.sort_values("Marks", ascending=False)
print("Sorted data:\n", df)
df["Bonus"] = 5
print("Updated marks:\n", df["Marks"] + df["Bonus"])
print("Missing values:\n", df.isnull().sum())
print("Summary:\n", df.describe(numeric_only=True))
df.to_csv("students.csv", index=False)
*** Add File: D:/data science all theory notes/MODULE-3 PYTHON/libraries/matplotlib/answers.py
"""Short Matplotlib answers and examples."""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [12, 18, 15, 22]
plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker="o", color="navy", label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

categories = ["A", "B", "C"]
values = [25, 40, 30]
plt.bar(categories, values, color=["tomato", "gold", "seagreen"])
plt.title("Category Values")
plt.xlabel("Category")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
*** Add File: D:/data science all theory notes/MODULE-3 PYTHON/libraries/seaborn/answers.py
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
