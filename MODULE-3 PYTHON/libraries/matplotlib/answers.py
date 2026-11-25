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
