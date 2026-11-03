# Task 3
# Question:
# Create a class called FoodOrder with attributes: restaurant_name, items (list), and total_price. Write an __init__() constructor to initialize these, then create an object representing your last Zomato or Swiggy order and print its details.

# Answer:


class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

my_order = FoodOrder("Burger King", ["Whopper", "Fries"], 350)
print(f"Restaurant: {my_order.restaurant_name}")
print(f"Items: {my_order.items}")
print(f"Total: ₹{my_order.total_price}")