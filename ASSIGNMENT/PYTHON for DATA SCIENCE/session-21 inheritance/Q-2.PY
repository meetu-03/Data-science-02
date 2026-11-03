#Task 2: Now create a subclass called Electronics that inherits from Product and overrides the get_discounted_price() method to apply a 20% discount instead of 10%.


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90


class Electronics(Product):

    def get_discounted_price(self):
        return self.price * 0.80


# Example usage:
e = Electronics("Headphones", 2000)
print(f"Electronics: {e.name}, Discounted Price: {e.get_discounted_price()}")