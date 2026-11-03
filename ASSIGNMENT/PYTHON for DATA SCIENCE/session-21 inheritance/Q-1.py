#Task 1: Create a Python class called Product with attributes name and price, and a method get_discounted_price() that returns the price after applying a 10% discount.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90


# Example usage:
p = Product("Book", 500)
print(f"Product: {p.name}, Discounted Price: {p.get_discounted_price()}")