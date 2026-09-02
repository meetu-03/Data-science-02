#Task 4: Build a simple Ticket class for a movie booking app with a method get_final_price(). Then, create a subclass PremiumTicket that overrides get_final_price() to add a 50 rupee convenience fee. Show both in action by creating objects and printing their final prices. Hint: Use super() in PremiumTicket to reuse the parent method and add the extra fee.


class Ticket:

    def __init__(self, price):
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):

    def get_final_price(self):
        base_price = super().get_final_price()
        return base_price + 50  # Adding ₹50 convenience fee


# Demonstration
standard_ticket = Ticket(200)
premium_ticket = PremiumTicket(200)

print("Standard Ticket Final Price:", standard_ticket.get_final_price())
print("Premium Ticket Final Price:", premium_ticket.get_final_price())