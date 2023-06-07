# Python Dictionaries
# A dictionary is a data structure used to store data in key-value pairs.
# Data in a dictionary is organized by associating each value with a unique key.
# Dictionaries are mutable, meaning their values can be modified.
# Dictionary items are unordered, meaning their order may not be preserved.
# Dictionaries do not allow duplicate keys.
# Dictionary items can be accessed using their keys.
# Items in dictionaries are enclosed in curly braces, {}.

# When to use a dictionary data structure?
# Dictionaries are used when we need to store and access data based on unique identifiers or keys.

# For example, dictionaries are ideal for storing information about objects that have multiple attributes or properties.
# Each attribute can be represented as a key, and its corresponding value contains the specific attribute's data.

# This allows for efficient and easy management of object details, as we can retrieve information by referencing its associated key.

# Example:
# Create a dictionary to store information about a product
product = {'id': 1, 'name': 'Example Product', 'price': 19.99}

# Accessing dictionary items
print('ID:', product['id'])
print('Name:', product['name'])
print('Price:', product['price'])

# Modifying dictionary items
product['price'] = 24.99

# Adding new items to the dictionary
product['category'] = 'Electronics'

# Deleting items from the dictionary
del product['id']

# Checking if a key exists in the dictionary
if 'name' in product:
    print("Name key exists")

# Iterating over dictionary items
for key, value in product.items():
    print(key + ':', value)

# Different Styles of Creating Dictionaries

# 1. Using Curly Braces {} and Colon :
# Create an empty dictionary
empty_dict = {}
# Create a dictionary with initial values
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}

# 2. Using dict() Constructor
# Create a dictionary using dict() constructor
car = dict(make='Toyota', model='Camry', year=2022)

# 3. Using Key-Value Pairs in List
# Create a dictionary using key-value pairs in a list
fruit_list = [('apple', 'red'), ('banana', 'yellow'), ('orange', 'orange')]
fruits = dict(fruit_list)

# 4. Using Zip() Function
# Create a dictionary using zip() function with two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = dict(zip(names, ages))

# Print the dictionaries created using different styles
print('Empty Dictionary:', empty_dict)
print('Student Dictionary:', student)
print('Car Dictionary:', car)
print('Fruits Dictionary:', fruits)
print('People Dictionary:', people)


# Example 1
# Create a dictionary to store university student details
student = {
    'name': 'John Doe',
    'age': 20,
    'student_id': '123456',
    'major': 'Computer Science',
    'year': 2,
    'gpa': 3.5
}
# Display the student details
print('Student Details:')
print('Name:', student['name'])
print('Age:', student['age'])
print('Student ID:', student['student_id'])
print('Major:', student['major'])
print('Year:', student['year'])
print('GPA:', student['gpa'])

# Exercise 2: Get 5 numbers from the user and create a dictionary with their squares as values.
# Initialize an empty dictionary to store the numbers and their squares
number_dict = {}
# Prompt the user to enter 5 numbers and calculate their squares
for i in range(5):
    number = int(input("Enter a number: "))
    square = number ** 2
    number_dict[number] = square
# Display the dictionary with the numbers and their squares
print(number_dict)

# Loop in Python Dictionaries

colors = {"1": "Green", "2": "Blue", "3": "Orange", "4": "Yellow", "5": "Pink"}
# Loop through items (key-value pairs)
for k, i in colors.items():
    print(k + " : " + i)

# Loop through keys
for k in colors.keys():
    print(k)

# Loop through values
for v in colors.values():
    print(v)

students_perfomance = {}
# Loop to get input from the user
for i in range(5):
    name = input("Enter the name of the Student: ")
    marks = int(input("Enter his score in the subject: "))
    students_perfomance[name] = marks
# Loop to display student names and scores
for n, m in students_perfomance.items():
    print(n + " : " + str(m))

# Dictionary Comprehension
# 1. Basic Syntax:
# newDict = {key: value for (key, value) in dictionary.items()}
# Explanation: This syntax pattern creates a new dictionary (newDict) by iterating over the items of an existing dictionary (dictionary).
# For each key-value pair, it assigns the key to the variable key and the value to the variable value.
# The resulting key-value pairs are used to construct the new dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three'}
doubled_numbers = {key: value * 2 for (key, value) in numbers.items()}
print(doubled_numbers)  # Output: {1: 'oneone', 2: 'twotwo', 3: 'threethree'}


# 2. Filtering with if Statement:
# newDict = {key: value for (key, value) in dictionary.items() if condition}
# Explanation: This syntax pattern allows you to include an if statement to filter
# the items in the original dictionary before creating the new dictionary.
# Only the key-value pairs that satisfy the condition will be included in the resulting dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
filtered_numbers = {key: value for (key, value) in numbers.items() if key % 2 == 0}
print(filtered_numbers)  # Output: {2: 'two', 4: 'four'}


# 3. Conditional Expression:
# newDict = {key: value_if_true if condition else value_if_false for (key, value) in dictionary.items()}
# Explanation: This syntax pattern allows you to use a conditional expression 
# (value_if_true if condition else value_if_false) to determine the value for each key in the new dictionary.
# The condition is evaluated, and if it's true, the value_if_true is assigned; otherwise, the value_if_false is assigned.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
replaced_numbers = {key: value.upper() if key % 2 == 0 else value.lower() for (key, value) in numbers.items()}
print(replaced_numbers)  # Output: {1: 'one', 2: 'TWO', 3: 'three', 4: 'FOUR'}


# 4. Nested if Statement:
# newDict = {key: value for (key, value) in dictionary.items() if outer_condition if inner_condition}
# Explanation: This syntax pattern allows you to use nested if statements to further filter the items in the original dictionary.
# Both the outer condition and the inner condition need to be satisfied for a key-value pair to be included in the resulting dictionary.
# Example:
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
filtered_numbers = {key: value for (key, value) in numbers.items() if key % 2 == 0 if len(value) > 3}
print(filtered_numbers)  # Output: {4: 'four'}


# Define the list of colors
colors = ["turquoise", "magenta", "lavender", "chartreuse", "marigold", "indigo"]
# Create an empty dictionary to store color lengths
my_colors = {}
# Iterate over each color in the list and assign its length to the dictionary
for color in colors:
    my_colors[color] = len(color)
# Print the resulting dictionary
print(my_colors)
# Alternatively, use dictionary comprehension with a conditional statement
my_colors = {color: len(color) for color in colors if len(color) > 8}
# Print the resulting dictionary
print(my_colors)

# Dictionary Methods
# 1. clear()
# Syntax: dictionary.clear()
# Explanation: The clear() method removes all key-value pairs from the dictionary, making it empty.
# Example 1: Clearing a dictionary
my_dict = {"apple": 5, "banana": 3, "orange": 2}
print(my_dict)  # Output: {"apple": 5, "banana": 3, "orange": 2}
my_dict.clear()
print(my_dict)  # Output: {}

# 2. copy()
# Syntax: new_dict = dictionary.copy()
# Explanation: The copy() method creates a shallow copy of the 
# dictionary and returns a new dictionary.
# Example 1: Copying a dictionary
my_dict = {"name": "John", "age": 25, "country": "USA"}
new_dict = my_dict.copy()
print(new_dict)  # Output: {"name": "John", "age": 25, "country": "USA"}

# 3. fromkeys()
# Syntax: new_dict = dict.fromkeys(keys, value)
# Explanation: The fromkeys() method creates a new dictionary with the 
# specified keys and optional value for all keys.
# Example 1: Creating a dictionary with default values
keys = ["apple", "banana", "orange"]
value = 0
my_dict = dict.fromkeys(keys, value)
print(my_dict)  # Output: {"apple": 0, "banana": 0, "orange": 0}

# 4. get()
# Syntax: value = dictionary.get(key, default)
# Explanation: The get() method returns the value for a given key in the dictionary. 
# If the key is not found, it returns the default value (or None if not specified).
# Example 1: Retrieving a value using the get() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
print(my_dict.get("apple"))  # Output: 5
print(my_dict.get("grape"))  # Output: None
print(my_dict.get("grape", 0))  # Output: 0 (default value)

# 5. items()
# Syntax: items = dictionary.items()
# Explanation: The items() method returns a view object that contains
# a list of key-value tuples of the dictionary.
# Example 1: Accessing key-value pairs using the items() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
for key, value in my_dict.items():
    print(key, "->", value)
# Output:
# apple -> 5
# banana -> 3
# orange -> 2

# 6. keys()
# Syntax: keys = dictionary.keys()
# Explanation: The keys() method returns a view object that
# contains a list of all keys in the dictionary.
# Example 1: Accessing keys using the keys() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(["apple", "banana", "orange"])

# 7. pop()
# Syntax: value = dictionary.pop(key, default)
# Explanation: The pop() method removes and returns the value associated
# with the given key. If the key is not found, it returns the default 
# value (or raises a KeyError if not specified).
# Example 1: Removing a key-value pair using the pop() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
value =

# 8. popitem()
# Syntax: key, value = dictionary.popitem()
# Explanation: The popitem() method removes and returns an arbitrary key-value
# pair from the dictionary. If the dictionary is empty, it raises a KeyError.
# Example 1: Removing an arbitrary key-value pair using the popitem() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
key, value = my_dict.popitem()
print(key, "->", value)  # Output: (Output can be different due to the arbitrary nature of popitem())

# 9. setdefault()
# Syntax: value = dictionary.setdefault(key, default)
# Explanation: The setdefault() method returns the value associated with the given key. 
# If the key is not found, it inserts the key with the specified default value and returns the default value.
# Example 1: Accessing a value using setdefault() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
value = my_dict.setdefault("grape", 0)
print(value)  # Output: 0 (default value)
print(my_dict)  # Output: {"apple": 5, "banana": 3, "orange": 2, "grape": 0}

# 10. update()
# Syntax: dictionary.update(other_dict)
# Explanation: The update() method updates the dictionary with the key-value pairs 
# from another dictionary or an iterable of key-value pairs.
# Example 1: Updating a dictionary with key-value pairs
my_dict = {"apple": 5, "banana": 3, "orange": 2}
other_dict = {"grape": 4, "mango": 2}
my_dict.update(other_dict)
print(my_dict)  # Output: {"apple": 5, "banana": 3, "orange": 2, "grape": 4, "mango": 2}

# 11. values()
# Syntax: values = dictionary.values()
# Explanation: The values() method returns a view object that contains
# a list of all values in the dictionary.
# Example 1: Accessing values using the values() method
my_dict = {"apple": 5, "banana": 3, "orange": 2}
values = my_dict.values()
print(values)  # Output: dict_values([5, 3, 2])

# Example 1
colors = {}  # Create an empty dictionary to store color names and codes
# Prompt the user to enter color names and codes
for i in range(5):
    color = input("Enter the name of the color: ")  # Get the color name from the user
    color = color.upper()  # Convert the color name to uppercase
    code = input("Enter the code of the color: ")  # Get the color code from the user
    colors[color] = code  # Add the color name and code to the dictionary
# Print the color names and codes from the original dictionary
for color, code in colors.items():
    print(color + " : " + code)
new = {x.lower(): y for (x, y) in colors.items()}  # Create a new dictionary with lowercase color names
# Print the color names and codes from the new dictionary
for color, code in new.items():
    print(color + " : " + code)
    
# Example 2:
students = {}  # Create an empty dictionary to store student names and admission numbers
# Prompt the user to enter student names and admission numbers
for i in range(5):
    name = input("Enter the student's name: ")  # Get the student name from the user
    name = name.upper()  # Convert the student name to uppercase
    admission_num = int(input("Enter the student's admission number: "))  # Get the student's admission number
    students[name] = admission_num  # Add the student name and admission number to the dictionary
# Print the student names and admission numbers from the original dictionary
for name, admission_num in students.items():
    print(name + " : " + str(admission_num))
students_with_even_admission_numbers = {x: y for (x, y) in students.items() if y % 2 == 0}
# Print the student names and admission numbers for students with even admission numbers
for name, admission_num in students_with_even_admission_numbers.items():
    print(name + " : " + str(admission_num))

Example 3:
# List of special dishes
special_dishes = ["Caviar", "Truffle Risotto", "Lobster Thermidor", "Foie Gras", "Kobe Beef Steak", "Saffron Paella", "Escargots de Bourgogne", "Baked Alaska"]
# List of corresponding dish prices
dish_prices = [200, 150, 180, 120, 300, 160, 90, 80]
# Create a dictionary to represent the menu
menu = {dish: price for dish, price in zip(special_dishes, dish_prices)}
# Print the menu
print(menu)
# Find the maximum price in the menu
max_price = max(menu.values())
print("The maximum price on the menu is:", max_price)

# Example 4:
# List of special dishes
special_dishes = ["Caviar", "Truffle Risotto", "Lobster Thermidor", "Foie Gras", "Kobe Beef Steak", "Saffron Paella", "Escargots de Bourgogne", "Baked Alaska"]
# Create a dictionary to represent the menu
menu = {dish: dish for dish in special_dishes}
# Print the menu
print(menu)
# Alternatively:
special_dishes = ["Caviar", "Truffle Risotto", "Lobster Thermidor", "Foie Gras", "Kobe Beef Steak", "Saffron Paella", "Escargots de Bourgogne", "Baked Alaska"]
# Create an empty dictionary to store the menu
menu = {}
# Iterate over each dish in the special_dishes list
for dish in special_dishes:
    # Assign the dish as both the key and value in the menu dictionary
    menu[dish] = dish
# Print the resulting menu dictionary
print(menu)

# Example 5:
# Dictionary of colors and their codes
colors = {
    "Red": "#FF0000",       # Color: Red, Code: #FF0000
    "Green": "#00FF00",     # Color: Green, Code: #00FF00
    "Blue": "#0000FF",      # Color: Blue, Code: #0000FF
    "Yellow": "#FFFF00",    # Color: Yellow, Code: #FFFF00
    "Cyan": "#00FFFF",      # Color: Cyan, Code: #00FFFF
    "Magenta": "#FF00FF",   # Color: Magenta, Code: #FF00FF
    "Orange": "#FFA500"     # Color: Orange, Code: #FFA500
}
# Print the dictionary of colors
print(colors)
# Prompt the user to enter a key to check its existence in the dictionary
user_key = input("Enter the key you want to check: ")
# Check if the user-entered key exists in the colors dictionary
if user_key in colors:
    print(user_key + " key exists.")
else:
    print(user_key + " key does not exist.")
