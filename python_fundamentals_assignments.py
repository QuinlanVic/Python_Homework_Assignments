# Python Fundamentals Assignment
# SDDA - 05 March 2024
# By: Quinlan Caiger


# Q1. Data Sorting and Ranking
# Objective: Sort a complex data structure and add a ranking key based on a specific criterion.
# Setup Code
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.
# Expected Output: The sorted list with an additional "rank" key for each student.
print("Question 1")
sorted_list = []
# sort the list according to grade and add to new list
sorted_list = sorted(students, key=(lambda student: student["grade"]), reverse=True)
i = 1
# run through new list and assign ranks (it should be in order so add one each time)
for student in sorted_list:
    student["rank"] = i
    i += 1
print(sorted_list)


# Q2. Merging Data from Two Lists
# Objective: Merge data from two lists of dictionaries based on a common key.
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.
# Expected Output: A merged list of dictionaries containing both name and salary for each employee.
print("Question 2")
# run through employees and salaries
for employee in employees:
    for pay in salaries:
        # if they have the same id key
        if employee["id"] == pay["id"]:
            # add a new salary field to employee with the salary from the salaries list of dict
            employee["salary"] = pay["salary"]
            break
print(employees)


# Q3. Advanced Filtering with Multiple Conditions
# Objective: Apply multiple filtering criteria to a list of dictionaries.
# Setup Code
print("Question 3")
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.
# Expected Output: A filtered list of dictionaries meeting both criteria.
# filter list according to two conditions using "and" operator and convert it from filter object to list
specific_products = list(
    filter(
        lambda product: product["category"] == "Electronics" and product["price"] < 500,
        products,
    )
)
print(specific_products)


# Q4. Complex Data Transformation
# Objective: Transform a list of dictionaries into a new structure.
# Setup Code
print("Question 4")
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.
# Expected Output: A dictionary with product names as keys and total quantities as values.
products_total = {}
# insane nesting. go through orders list
for order in orders:
    # unpack each order's values
    for key, value in order.items():
        # go through the list of values for the items key in each order
        if key == "items":
            for item in value:
                # if we already have the product in the new list then increment its quantity
                if item["product"] in products_total.keys():
                    products_total[item["product"]] = (
                        products_total.get(item["product"]) + item["quantity"]
                    )
                else:
                    # otherwise we do not have the product and we need to make a new entry into the dict with its quantity
                    # productstotal = {**productstotal, item["product"]: item["quantity"]}
                    # more optimised
                    products_total[item["product"]] = item["quantity"]
print(products_total)


# Q5. Data Consolidation and Summarization
# Objective: Consolidate and summarize data from a list of dictionaries.
# Setup Code
print("Question 5")
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.
# Expected Output: A dictionary with categories as keys and total amounts spent as values.
transactions_by_category = {}
# run through transactions
# similar to above
for transaction in transactions:
    # if we have the category in the new dict, increment its amount
    if transaction["category"] in transactions_by_category.keys():
        transactions_by_category[transaction["category"]] = (
            transactions_by_category.get(transaction["category"])
            + transaction["amount"]
        )
    else:
        # otherwise add new category entry with its amount
        # transactions_by_category = {
        #     **transactions_by_category,
        #     transaction["category"]: transaction["amount"],
        # }
        # more optimised
        transactions_by_category[transaction["category"]] = transaction["amount"]
print(transactions_by_category)


# Q6. Grouping and Aggregating Data
# Objective: Group data by a specific key and perform aggregation.
# Setup Code
print("Question 6")
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.
# Expected Output: A dictionary with salespersons as keys and total sales amounts as values.
salesbysalesperson = {}
# very similar to previous 2 questions
for sale in sales:
    if sale["salesperson"] in salesbysalesperson.keys():
        salesbysalesperson[sale["salesperson"]] = (
            salesbysalesperson.get(sale["salesperson"]) + sale["amount"]
        )
    else:
        salesbysalesperson[sale["salesperson"]] = sale["amount"]
print(salesbysalesperson)


# These assignments are designed to challenge freshers with real-world data manipulation scenarios, enhancing their problem-solving skills and proficiency in Python.


# Q7. Lambda Functions for Spell Power
# Objective: Use a lambda function to sort a list of spells by their power level.
# Setup Code
print("Question 7")
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.
# Expected Output: [('Obliviate', 10), ('Expelliarmus', 7), ('Lumos', 5)]
# sort according to spell power using key and lambda function with reverse=True for descending order
spellssorted = sorted(spells, key=(lambda spell: spell[1]), reverse=True)
print(spellssorted)


# Q8. Map Transformation for Potion Ingredients
# Objective: Transform a list of potion ingredients to their required quantities using map.
# Setup Code
print("Question 8")
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.
# Expected Output: ['Wolfsbane: 3 grams', 'Eye of Newt: 3 grams', 'Dragon Scale: 3 grams']
# use map to change each ingredient in the list and concatenation to make the changes
addweight = list(map(lambda ingredient: ingredient + ": 3 grams", ingredients))
print(addweight)


# Q9. Magical Book Filter and Formatter
# Objective: Combine filter, map, and lambda functions to process a list of books and format their titles.
# Setup Code
print("Question 9")
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.
# Expected Output: ['MAGICAL DRAFTS AND POTIONS']
# filter out books with more than 120 pages
filteredbooks = list(filter(lambda book: book["pages"] > 120, books))
# extract only their titles using map
titlesonly = list(map(lambda filteredbook: filteredbook["title"], filteredbooks))
print(titlesonly)


# Q10. Wizard Duel Game Class
# Objective: Create a WizardDuel class where wizards can cast spells at each other until one wins.
# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.
# Expected Output: After a duel between Harry and Draco, Harry wins with 10 health points left.
print("Question 10")


# A lot of creative licence and I did a lot for this having a decent amount of fun
class WizardDuel:
    # constructor function
    def __init__(self, name, health_points):
        self.name = name
        self.health_points = health_points

    # function for one wizard to cast a spell on another and update hit points using reduce_health_points function
    def cast_spell(self, wizard2, spellname, hitpoints):
        # are they going to die after this spell was casted on them?
        if hitpoints >= wizard2.health_points:
            WizardDuel.reduce_health_points(wizard2, hitpoints)
            return f"{self.name} casted {spellname} on {wizard2.name} and hit them for {hitpoints} health points and they are now dead!"
        WizardDuel.reduce_health_points(wizard2, hitpoints)
        return f"{self.name} casted {spellname} on {wizard2.name} and hit them for {hitpoints} health points and they are now on {wizard2.health_points} health points!"

    # function to reduce health points
    def reduce_health_points(wizard, hitpoints):
        wizard.health_points -= hitpoints

    # function to determine who has more health points and won after a duel
    def determine_winner(wizard1, wizard2):
        if wizard1.health_points > wizard2.health_points:
            return f"After a duel between {wizard1.name} and {wizard2.name}, {wizard1.name} wins with {wizard1.health_points} health points left"
        elif wizard1.health_points == wizard2.health_points:
            return f"After a duel between {wizard1.name} and {wizard2.name}, it is a draw with each wizard having {wizard1.health_points} health points left"
        return f"After a duel between {wizard1.name} and {wizard2.name}, {wizard2.name} wins with {wizard2.health_points} health points left"


# creating instances and simulating an epic battle
harry = WizardDuel("Harry", 100)
draco = WizardDuel("Draco", 100)
print(harry.cast_spell(draco, "dragon's breath", 10))
print(draco.cast_spell(harry, "black pearl", 15))
print(harry.cast_spell(draco, "eagle claw", 15))
print(draco.cast_spell(harry, "snake poison", 15))
print(harry.cast_spell(draco, "silver tongue", 10))
print(draco.cast_spell(harry, "eternal darkness", 20))
print(harry.cast_spell(draco, "infinite void", 25))
print(WizardDuel.determine_winner(harry, draco))
print(draco.cast_spell(harry, "dealthly hallows", 40))
print(harry.cast_spell(draco, "Avada Kedavra", 45))
print(WizardDuel.determine_winner(harry, draco))


# Q11. Custom Error Handling in Potion Making
# Objective: Create a custom exception to handle errors in potion making, such as using the wrong ingredient.
# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.
# Expected Output: Caught PotionError: 'Eye of Newt' is not a valid ingredient for the Love Potion.
print("Question 11")


# A lot of creative licence and I did even more with this task
class PotionError(Exception):
    """Raised when there is an error during potion making"""

    # constructor for creating an error
    def __init__(self, ingredient, potion):
        self.ingredient = ingredient
        self.potion = potion
        self.message = "Caught PotionError: "
        # here we create an instance of the exception class using base method, giving it self.message
        super().__init__(self.message)

    # Override print() for base class of Exception
    # "__str__" = String dunder method
    # if you do not override then only "self.message" will print by default
    def __str__(self):
        return f"{self.message} '{self.ingredient}' is not a valid ingredient for the {self.potion}."


# list of dictionaries with potions and the ingredients to make them
potions = [
    {"Love Potion": ["unicorn tear", "eagle feather"]},
    {"Hate Potion": ["Eye of Newt", "Eye of Kashar"]},
    {"Death Potion": ["dragon's claw", "earth essence"]},
    {"Life Potion": ["pure silver", "oracle eye"]},
]


# function to create potions and throw errors if ingredients are not correct (a lot of unnecessary extra work but fun and good practice)
def potion_making(ingredients, potion_chosen):
    valid_ingre_for_potion = []
    # run through potions and their names and ingredients to check for type of potion
    for potion in potions:
        for potion_name, ingre in potion.items():
            if potion_name == potion_chosen:
                valid_ingre_for_potion = ingre
                break
    # try, except block to catch when an ingredient is invalid
    try:
        for ingredient in ingredients:
            if ingredient not in valid_ingre_for_potion:
                raise PotionError(ingredient, potion_chosen)
        print(f"{potion_chosen} successfully created using {ingredients}")
    except PotionError as e:
        print(e)


# making potions (one failing)
potion_making(["dragon's claw", "earth essence"], "Death Potion")
potion_making(["pure silver", "oracle eye"], "Life Potion")
potion_making(["unicorn tear", "Eye of Newt"], "Love Potion")


# Q12. Hogwarts Library Database Query
# Objective: Simulate a database query to find books by a specific author using list comprehensions.
# Setup Code
print("Question 12")
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
#  Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.
# Expected Output: [{'title': 'Magical Hieroglyphs and Logograms', 'author': 'Bathilda Bagshot'}]
# list comprehension to select books by authorname
books_by_author = [book for book in library if book["author"] == "Bathilda Bagshot"]
print(books_by_author)


# Q13. Hogwarts House Points Calculator
# Objective: Calculate the total points for each house using nested loops and a list of dictionaries.
# Setup Code
print("Question 13")
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.
# Expected Output: Gryffindor: 95, Slytherin: 90
house_total_points = {}
# go through points scored for houses
for house in house_points:
    # check if we have an entry for that house in our new dict
    if house["house"] not in house_total_points:
        # if not create a new entry
        house_total_points[house["house"]] = house["points"]
    else:
        # otherwise increment the points for that house
        house_total_points[house["house"]] += house["points"]
# special replace mthods to remove "{}" on ends of dict in print
print(f"{house_total_points}".replace("{", "").replace("}", ""))


# Q14. Class Inheritance for Magical Creatures
# Objective: Implement a class hierarchy for magical creatures where each subclass overrides a common method.
# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.
# Expected Output: Calling sound() on a Dragon instance prints 'Roar', on a Unicorn instance prints 'Neigh'.
print("Question 14")


class MagicalCreature:
    """MagicalCreature class to create new magical creatures"""

    # constructor method
    def __init__(self, name):
        self.name = name

    # sound function to describe the sound a magical creature makes
    def sound(self):
        return "Noise"


class Dragon(MagicalCreature):
    """Dragon subclass of MagicalCreature"""

    # can get rid of, don't need to override
    # def __init__(self, name):
    #     super().__init__(name)
    # function to override parent's
    def sound(self):
        return "Roar"


class Unicorn(MagicalCreature):
    """Unicorn subclass of MagicalCreature"""

    # can get rid of, don't need to override
    # def __init__(self, name):
    #     super().__init__(name)

    # function to override parent's
    def sound(self):
        return "Neigh"


# creating instances
giant = MagicalCreature("Giant")
darkscales = Dragon("DarkScales")
whitelily = Unicorn("WhiteLily")
# printing sounds of each creature
print(giant.sound())
print(darkscales.sound())
print(whitelily.sound())


# Q15. Custom Sorting with Lambda for Magical Artifacts
# Objective: Sort a list of magical artifacts by their age and power level using a custom lambda function.
# Setup Code
print("Question 15")
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.
# Expected Output: Sorted list by age, then by power.
# sort by two values, one before the other using key and a lambda function with a tuple of the two values to sort by
artifactsrankedagepower = sorted(
    artifacts,
    key=(lambda artifact: (artifact["age"], artifact["power"])),
    reverse=True,
)
print(artifactsrankedagepower)


# Q16. Wizard Profile Generator with f-strings
# Objective: Dynamically generate wizard profiles using f-strings and dictionary unpacking.
# Setup Code
print("Question 16")
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.
# Expected Output: 'Albus Dumbledore, the Headmaster of Gryffindor.'
# tricky formatting with single and double quotes in f string to create profile string
print(f"{wizard.get('name')}, the {wizard.get('title')} of {wizard.get('house')}.")


# Q17. Magical Creature Adoption Matching
# Objective: Match potential magical creature adopters with creatures based on preferences using filter and map.
# Setup Code
print("Question 17")
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.
# Expected Output: [('Harry', 'Fawkes'), ('Hermione', 'Dobby')]

# extract the preferences so that you can filter creatures easily
preferences = [adopter[1] for adopter in adopters]
# get list of creatures that match
creatures_match = list(filter(lambda pair: pair[1] in preferences, creatures))
# print(creatures_match)


# I can do it with loops and then modified it so that it could work in a map function
# take in adopter and their preference as well as creatures that match their preference
def pairthem(adopter_tup, creatures_match_list):
    # unpack the adopter and their preference into separate variables
    adopter, preference = adopter_tup
    # run through list of creatures that match unpacking their name and type of creature they are
    for name, creature in creatures_match_list:
        # if the adopter's preference and the type of creature match
        if preference == creature:
            # pair the adopter's and creature's name and return it
            return (adopter, name)


# change each value in adopters to add the creature they have adopted using map
adopters_creatures = list(
    map(lambda adopter_tuple: pairthem(adopter_tuple, creatures_match), adopters)
)
print(adopters_creatures)


# Q18. Advanced Potion Making with Nested Loops
# Objective: Simulate potion making where each combination of ingredients produces a unique result using nested loops.
# Setup Code
print("Question 18")
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.
# Expected Output: Combining Moonstone and Silver Dust produces a Visibility Potion., etc., for all unique pairs.
# list of unique potions made with ingredients above
potions_made = ["Visibility Potion", "Rage Potion", "Bliss Potion"]


# potion making function given a list of ingredients prints out the potions that can be made from their unique combinations
def potion_making(ingredients_list):
    i = 0
    k = 0
    # run through ingredients and create potions with element 1 + 2, then element 1 + 3 and then finally element 2 + 3
    # do this by nested loops with 3 sets of values i, j, k
    # i tracks the first element to make the potion; j tracks the second and k tracks what potion they will make
    for i in range(len(ingredients_list)):
        for j in range(i + 1, len(ingredients_list)):
            print(
                f"Combining {ingredients_list[i]} and {ingredients_list[j]} produces a {potions_made[k]}."
            )
            k += 1


potion_making(ingredients)


# Q19. Nested Data Manipulation
# Objective: Navigate and manipulate a nested data structure.
# Setup Code
print("Question 19")
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.
# Expected Output: The original list with the modified tags list for applicable items.
# run through data
for element in data:
    # check if that element of data has 'tag1'
    if "tag1" in element["tags"]:
        # if it does add 'tag4' to its list of tags
        element["tags"].append("tag4")
print(data)


# Q20. Implementing a Custom Sort Function
# Objective: Implement a custom sort function for a list of dictionaries based on multiple criteria.
# Setup Code
print("Question 20")
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
]


# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").
# Expected Output: The sorted list of tasks.


# function to convert the string 'priorities' into ints for the sorted function to sort by
def priority_as_int(priority):
    # print(priority)
    if priority == "High":
        return 3
    if priority == "Medium":
        return 2
    return 1


# sort by two values, one before the other using key and a lambda function with a tuple of the two values to sort by
tasks_ranked_completed_priority = sorted(
    tasks,
    # "-" to give you reverse = True (descending order)
    key=(lambda task: (task["completed"], -priority_as_int(task["priority"]))),
)
print(tasks_ranked_completed_priority)
