#.Design a simple abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: Paytm and PhonePe, each implementing pay(amount) to print a different message. Instantiate both and call their pay methods with any amount.

from abc import ABC, abstractmethod


# Abstract base class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Subclass 1: Paytm
class Paytm(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} successfully using Paytm.")


# Subclass 2: PhonePe
class PhonePe(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} successfully using PhonePe.")


# Demonstration
if __name__ == "__main__":
    paytm_payment = Paytm()
    phonepe_payment = PhonePe()

    # Calling pay method on both instances
    paytm_payment.pay(500)
    phonepe_payment.pay(1200)