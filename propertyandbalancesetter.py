# @property and @balance.setter decorators code
# SDDA - 29 February 2024
# By: Quinlan Caiger
# @property
"""Decorator example using function to illustrate meaning"""


# decorator function that accepts a function as an argument ("f")
def decorator(f):
    def new_function():
        # runs extra functionality function "new_function" before the initial function "f"
        print("Extra Functionality")
        # accepted function "f" is called in nested function
        f()

    return new_function


@decorator
def initial_function():
    print("Initial Functionality")


initial_function()


class Car:
    """Decorator function usage in a class Real-World example to further illustrate meaning and fully elaborate on its usefulness"""

    def __init__(self, price):
        self.price = price

    @property
    def price(self):  # getter name is the same as the property we wish to access
        return self._price

    # name of property is used for setter and deleter
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


car = Car(100000.0)  # Create instance of Car class
car.price  # Access value
car.price = 75000.0  # Update value
print(car.price)  # 75000.0


# @balance.setter
class Bank:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self._balance = balance  # protected variable

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError(f"{value} is not a valid input for balance")
        self._balance = value

    def deposit(self, depositamount):
        if depositamount < 0:
            raise ValueError(f"Invalid deposit amount of R{depositamount:,}")
        self._balance += depositamount
        return f"Success. {self.display_balance()}"

    def withdraw(self, withdrawal):
        if withdrawal < 0:
            raise ValueError(
                f"Insufficient funds (R{self._balance:,}) to make this withdrawal (R{withdrawal:,})"
            )
        if withdrawal > self.balance:
            raise ValueError(
                f"Insufficient funds (R{self._balance:,}) to make this withdrawal (R{withdrawal:,})"
            )
        self._balance -= withdrawal
        return f"Success. {self.display_balance()}"

    # instance method | self -> instance/object
    def display_balance(self):
        return f"Your balance is: R{self._balance:,}"


gemma = Bank(123, "Gemma Porrill", 15_000)
print(gemma.balance)  # 15000
gemma.deposit(1100)
print(gemma.balance)  # 16100
# gemma.withdraw(20000) # ValueError: Insufficient funds (R16,100) to make this withdrawal (R20,000)
# gemma.deposit(-100)   # ValueError: Invalid deposit amount of R-100
