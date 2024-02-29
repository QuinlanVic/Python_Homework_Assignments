# `@property` and `@balance.setter` decorators in Python OOP
## SDDA - 29 February 2024
### By: Quinlan Caiger

### `@property` Definition
- `@property` is a built-in decorator for the `property()` function in Python.
- A decorator function adds new functionality to an existing function, which is passed to it as an argument, without modifying the existing function at all.
- The only addition to the existing function is adding the "@decorator" syntax above its declaration which results in the decorator function only being run when the existing function is called.
- The `@property` decorator is used to provide "special" functionality to certain attributes/methods to make them act as "getters", "setters", or "deleters" when we define properties in a class.
- By using `@property`, you can "reuse" the name of a property to avoid creating new names for the "getters", "setters", and "deleters".
	- These advantages make properties a helpful tool allowing you to write more concise and readable code.

### `@property` Simple Example
```
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
```

**Output:** <br>
Extra Functionality<br>
Initial Functionality

### `@property` Real-World Example
Let us say we have a "Car" class with a constrctor as follows.
```
"""Decorator function usage in a class Real-World example to further illustrate meaning and fully elaborate on its usefulness"""
class Car:
	def __init__(self, price):
		self.price = price
```
If we want the price attribute to be "protected" (only available to classes and subclasses) but need to access and modify it outside of the class we would need to use "getter" and "setter" functions.
If there is existing code in the program that accesses or modifies the value of the attribute it will have to be modified to call "getter" or "setter" functions, respectively, or the code will break. 
With `@property`, you will not need to modify any of those lines because you will be able to add "getters" and "setters" *behind the scenes* without affecting the syntax that you used to access or modify the attribute when it was public.
```
# getter
@property
def price(self): # getter name is the same as the property we wish to access
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
```

How it may be used for example:
```
car = Car(100000.0) # Create instance of Car class
car.price           # Access value
car.price = 75000   # Update value
```
**Ouput: 100000.0**
Through the examples it is clear that the `@property` decorator is a useful tool for implementing new functionalities to existing functions and improving readability and code size.


### `@balance.setter` Definition
- `@balance.setter` is a decorator that is often used to provide functionality to a Bank class example's balance attribute in order for it to act as a "setter" function.
- For example, we may have a defined a Bank class with the code below and added an `@balance.setter` decorator to print errors when a negative balance is attempted to be set, a negative deposit or withdrawal is attempted or a withdrawal greater than the balance in the account is attempted.

### `@balance.setter` Example
```
class Bank:
    def __init__(self, accno, name, balance):  
        self.accno = accno
        self.name = name
        self._balance = balance # protected variable
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError(f"{value} is not a valid input for balance")
        self._balance = value

    # instance method | self -> instance/object
    def display_balance(self):
        return f"Your balance is: R{self.__balance:,}"
	
    def withdraw(self, withdrawal):
        if withdrawal < 0:
            raise VaueError(f"Insufficient funds (R{self.__balance:,}) to make this withdrawal (R{withdrawal:,})")
	if withdrawal > self.balance:
	    raise ValueError(f"Insufficient funds (R{self.__balance:,}) to make this withdrawal (R{withdrawal:,})")
    	self.__balance -= withdrawal
    	return f"Success. {self.display_balance()}"
	    
    def deposit(self, depositamount):
        if depositamount < 0:
            raise ValueError(f"Invalid deposit amount of R{depositamount:,}")
	self.__balance += depositamount
	return f"Success. {self.display_balance()}"
```
Below is an example of how to class and its attributes may be used with the `@balance.setter` decorator in play:
```
gemma = Bank(123, "Gemma Porrill", 15_000)
print(gemma.balance) # 15_000
gemma.deposit(1100) 
print(gemma.balance)     # 16_100
gemma.withdraw(20000)    # ValueError: 
gemma.deposit(-100)      # ValueError: -100 is not a valid input for amount
gemma.deposit("100")     # ValueError: 100 is not a valid input for amount
```

#### References
1. https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,define%20properties%20in%20a%20class.
