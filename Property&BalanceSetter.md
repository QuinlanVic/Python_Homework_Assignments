# Property and Balance.setter in Python OOP
## SDDA - 29 February 2024
### By: Quinlan Caiger

### @property Definition
- @property
  - @property is a Decorator in Python
  - A decorator function adds new functionality to an existing function, which is passed to it as an argument, without modifying the existing function at all.
  -   The only addition to the existing function is adding 
  - By using @property, you can "reuse" the name of a property to avoid creating new names for the getters, setters, and deleters

### @property Example
<code>
# decorator function that accepts a function as an argument ("f")
def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function
@decorator
def initial_function():
    print("Initial Functionality")
initial_function()
</code>

### balance.setter Definition
- balance.setter
  - balance.setter is 

### balance.setter Example


#### References
1. https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,define%20properties%20in%20a%20class.
