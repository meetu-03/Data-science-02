# Task 4
# Question:
# Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) that adds the item to the items list and updates total_price. Demonstrate by adding two items to your order and printing the updated total.

# Answer:

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price

my_order = FoodOrder("Burger King", ["Whopper"], 250)

# Add two new items
my_order.add_item("Fries", 100)
my_order.add_item("Coke", 80)

print(f"Updated Items: {my_order.items}")
print(f"Updated Total: ₹{my_order.total_price}")