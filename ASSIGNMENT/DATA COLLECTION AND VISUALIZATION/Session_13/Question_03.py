import seaborn as sns
import matplotlib.pyplot as plt

# Load fmri dataset
fmri = sns.load_dataset("fmri")

sns.relplot(data=fmri, x="timepoint", y="signal", hue="event", kind="line")
plt.suptitle("Signal Changes Over Time", y=1.02)
plt.show()

# Output: Line plot showing signal changes for different events.
