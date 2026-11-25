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
