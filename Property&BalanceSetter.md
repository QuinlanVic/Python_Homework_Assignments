# @property Decorator and Balance.setter in Python OOP
## SDDA - 29 February 2024
### By: Quinlan Caiger

### `@property` Definition
- `@property`
  - `@property` is a built-in decorator for the `property()` function in Python.
  - A decorator function adds new functionality to an existing function, which is passed to it as an argument, without modifying the existing function at all.
  - The only addition to the existing function is adding "@decorator" syntax above its declaration which results in the decorator function only being run when the existing function is called.
  - The @property decorator is used to provide "special" functionality to certain attributes/methods to make them act as "getters", "setters", or "deleters" when we define properties in a class.
  - By using @property, you can "reuse" the name of a property to avoid creating new names for the "getters", "setters", and "deleters".
  - These advantages make properties a helpful tool allowing you to write more concise and readable code.

### @property Simple Example
<code>
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
</code>

### @property Real-World Example
Let us say we a "Car" class with a constrctor as follows.
<code>
class Car:
	def __init__(self, price):
		self.price = price
</code>
What if we wanted this price value to be "protected" (only available to classes and subclasses) and we require to access and modify it outside of the class.
If you want to add "getters" and "setters" -> each line of code that accesses or modifies the value of the attribute will have to be modified to call the getter or setter, respectively or the code will break. 
With `@property`, you will not need to modify any of those lines because you will be able to add "getters" and "setters" *behind the scenes* without affecting the syntax that you used to access or modify the attribute when it was public.
<code>
\# getter
@property
def price(self): # getter name is the same as the property we wish to access
	return self._price
 
\# name of property is used for setter and deleter
@price.setter
def price(self, new_price):
	if new_price > 0 and isinstance(new_price, float):
		self._price = new_price
	else:
		print("Please enter a valid price")

@price.deleter
def price(self):
	del self._price
</code>

How it may be used for example:
<code>
car = Car(100000.0) # Create instance of Car class
car.price           # Access value
car.price = 75000   # Update value
</code>
ouput = 100000.0

### balance.setter Definition
- balance.setter
  - balance.setter is 

### balance.setter Example


#### References
1. https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,define%20properties%20in%20a%20class.
