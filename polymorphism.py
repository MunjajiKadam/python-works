
from abc import ABC, abstractmethod


# =====================================================
# 1. ABSTRACTION + INHERITANCE
# =====================================================

# Abstract parent class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# =====================================================
# 2. METHOD OVERRIDING + RUNTIME POLYMORPHISM
# =====================================================

# CreditCard inherits PaymentMethod
class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")


# UPI inherits PaymentMethod
class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")


# PayPal inherits PaymentMethod
class PayPal(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs.{amount} using PayPal")


# =====================================================
# 3. POLYMORPHISM USING A COMMON FUNCTION
# =====================================================

# Same function works with different payment objects
def process_payment(payment, amount):

    payment.pay(amount)


# Creating objects
card = CreditCard()
upi = UPI()
paypal = PayPal()

# Same function, different behavior
process_payment(card, 500)
process_payment(upi, 1000)
process_payment(paypal, 1500)


# =====================================================
# 4. DUCK TYPING
# =====================================================

# This class does NOT inherit PaymentMethod
# But it has the required pay() method

class DigitalWallet:

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Digital Wallet")


wallet = DigitalWallet()

# Works even without inheriting PaymentMethod
process_payment(wallet, 2000)


# =====================================================
# 5. METHOD OVERLOADING (PYTHON-STYLE)
# =====================================================

class Calculator:

    # Python does not support traditional method
    # overloading, but default arguments provide
    # similar behavior.

    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print("Addition:", calc.add(10, 20))
print("Addition:", calc.add(10, 20, 30))
print("Addition:", calc.add(10))


# =====================================================
# 6. OPERATOR OVERLOADING
# =====================================================

class Money:

    def __init__(self, amount):
        self.amount = amount

    # Overloading the + operator
    def __add__(self, other):

        return Money(self.amount + other.amount)


money1 = Money(500)
money2 = Money(1000)

# Python internally calls money1.__add__(money2)
total = money1 + money2

print("Total Money:", total.amount)


# =====================================================
# 7. BUILT-IN FUNCTION POLYMORPHISM
# =====================================================

# The same len() function works with different objects

print("String length:", len("Python"))

print("List length:", len([10, 20, 30]))

print("Dictionary length:", len({"name": "MK", "age": 21}))


# =====================================================
# 8. FUNCTION POLYMORPHISM
# =====================================================

def display(value):

    print("Value:", value)


# Same function accepts different data types
display(100)
display("Python")
display([10, 20, 30])
display({"name": "MK"})


# =====================================================
# 9. FINAL PAYMENT PROCESSING
# =====================================================

print("\n--- Payment Processing System ---")

payments = [
    CreditCard(),
    UPI(),
    PayPal(),
    DigitalWallet()
]

# Same loop and same method call for different objects
for payment in payments:

    process_payment(payment, 2500)
