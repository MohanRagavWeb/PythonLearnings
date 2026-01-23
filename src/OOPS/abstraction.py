from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Payment via Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment via UPI")

payments = [CreditCard(), UPI()]

for p in payments:
    p.pay()
