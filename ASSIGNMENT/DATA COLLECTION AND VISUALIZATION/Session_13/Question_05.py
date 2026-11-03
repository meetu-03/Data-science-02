import seaborn as sns
import matplotlib.pyplot as plt

# Load penguins dataset
penguins = sns.load_dataset("penguins")

sns.jointplot(
    data=penguins, x="bill_length_mm",
    y="flipper_length_mm", kind="reg", color="green"
)
plt.show()

# Output: Scatter plot with regression line and marginal distributions.
