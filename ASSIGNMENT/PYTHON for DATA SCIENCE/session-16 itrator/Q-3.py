#Use enumerate() to print out the index and name of each item in a shopping cart list (e.g., ['Pizza', 'Burger', 'Fries', 'Coke']) like Flipkart displays item numbers in your cart.

cart = ["Pizza", "Burger", "Fries", "Coke"]

for index, item in enumerate(cart, start=1):
    print(index, item)