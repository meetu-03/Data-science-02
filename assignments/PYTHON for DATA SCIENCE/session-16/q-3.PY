#Task 3: Write a function show_final_price(item) that takes any Product or Electronics object and prints its name and the discounted price by calling get_discounted_price(). Demonstrate polymorphism by passing both a Product and an Electronics object to this function.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90


class Electronics(Product):

    def get_discounted_price(self):
        return self.price * 0.80


def show_final_price(item):
    print(f"Item: {item.name} | Final Price: {item.get_discounted_price()}")


# Demonstration of Polymorphism
prod = Product("Backpack", 1000)
elec = Electronics("Smartwatch", 5000)

show_final_price(prod)
show_final_price(elec)