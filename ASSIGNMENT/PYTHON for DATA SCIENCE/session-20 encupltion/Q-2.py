#Build a Product class for a Flipkart-style app with a private attribute _price. Implement get_price() and set_price() methods to access and update the price. Demonstrate setting and getting the price for a product object.


class Product:

    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid price! Price must be greater than zero.")


# Demonstration
if __name__ == "__main__":
    # Create a product object
    laptop = Product("Gaming Laptop", 55000)

    # Get initial price using get_price()
    print("Initial Price:", laptop.get_price())

    # Update price using set_price()
    laptop.set_price(52999)

    # Get updated price
    print("Updated Price:", laptop.get_price())