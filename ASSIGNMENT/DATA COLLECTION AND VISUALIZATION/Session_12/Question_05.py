import seaborn as sns
import matplotlib.pyplot as plt

# Daily step counts for one week
steps = [5000, 6500, 7000, 8000, 9000, 10000, 8500]

sns.set_theme(style="whitegrid")
sns.kdeplot(x=steps, fill=True, color="purple")

plt.title("Daily Steps Distribution")
plt.xlabel("Number of Steps")
plt.ylabel("Density")
plt.show()

# Output: KDE plot showing the distribution of daily steps.
