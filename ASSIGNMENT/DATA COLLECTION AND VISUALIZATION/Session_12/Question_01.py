import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate delivery times for 50 Zomato orders
np.random.seed(42)
delivery_times = np.random.randint(15, 60, 50)

sns.histplot(delivery_times, bins=10, color="blue")
plt.title("Zomato Delivery Time Distribution")
plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Number of Orders")
plt.show()

# Output: Histogram showing delivery times for 50 orders.
