# @property Decorator and Balance.setter in Python OOP
## SDDA - 29 February 2024
### By: Quinlan Caiger

### `@property` Definition
- `@property`
  - `@property` is a built-in decorator for the `property()` function in Python.
  - A decorator function adds new functionality to an existing function, which is passed to it as an argument, without modifying the existing function at all.
  - The only addition to the existing function is adding the "@decorator" syntax above its declaration which causes the decorator function to only be run when the existing function is called.
  - the @property decorator is used to provide "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.
  - By using @property, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters
  - These advantages make properties a really awesome tool to help you write more concise and readable code

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
Consider us having a "Car" class with a constrctor as follows.
<code>
class Car:
	def __init__(self, price):
		self.price = price
</code>
What if we wanted this price value to be protected and we require the new value to be validated before assigning it.

### balance.setter Definition
- balance.setter
  - balance.setter is 

### balance.setter Example


#### References
1. https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,define%20properties%20in%20a%20class.
