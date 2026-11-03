import pandas as pd

# Keep ipl_matches.csv in this folder
df = pd.read_csv("ipl_matches.csv")

print("Mean:", df["total_runs"].mean())
print("Median:", df["total_runs"].median())
print("Minimum:", df["total_runs"].min())
print("Maximum:", df["total_runs"].max())
print("Standard Deviation:", df["total_runs"].std())

# Output: Summary statistics for the total_runs column.
