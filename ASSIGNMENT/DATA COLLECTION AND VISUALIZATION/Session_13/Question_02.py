import seaborn as sns
import matplotlib.pyplot as plt

# Load flights dataset
flights = sns.load_dataset("flights")

# Make a table with months as rows and years as columns
flight_table = flights.pivot(index="month", columns="year", values="passengers")

sns.heatmap(flight_table, annot=True, fmt="d", cmap="coolwarm")
plt.title("Passengers by Month and Year")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()

# Output: Heatmap showing passenger counts by month and year.
