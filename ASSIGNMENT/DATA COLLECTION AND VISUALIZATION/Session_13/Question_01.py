import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

sns.pairplot(tips)
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

# Output: Pairwise plots for numeric columns in the tips dataset.
