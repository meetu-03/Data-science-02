import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

sns.catplot(
    data=titanic, x="class", y="survived",
    kind="bar", color="cornflowerblue", errorbar=("ci", 95)
)

plt.title("Titanic Survival Rate by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# Output: Bar chart showing survival rate by class with confidence intervals.
