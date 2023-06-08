# Sets in Python
# Set is a collection of unordered, unchangeable, and unindexable items
# Set elements are stored in curly braces, i.e., {}
# Every element in a set is separated by a comma
# Sets can be created using the set() method or by enclosing elements in curly braces {}
# Sets store unique elements, i.e., no duplicate elements
# The "+" and "*" operators cannot be used with sets

# Creating a set using the set() method
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set using curly braces
another_set = {4, 5, 6, 7, 8}
print(another_set)  # Output: {4, 5, 6, 7, 8}

# Adding elements to a set using the add() method
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set using the remove() method
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

# Checking if an element is present in a set using the "in" keyword
if 3 in my_set:
    print("3 is present in the set")
else:
    print("3 is not present in the set")  # Output: 3 is present in the set

# Performing set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of two sets using the union() method or the "|" operator
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of two sets using the intersection() method or the "&" operator
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}

# Difference between two sets using the difference() method or the "-" operator
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Subset check using the issubset() method
subset_check = set1.issubset(set2)
print(subset_check)  # Output: False

# Superset check using the issuperset() method
superset_check = set1.issuperset(set2)
print(superset_check)  # Output: False

# Creating a set
my_set = {2, 5, 8, 2, 56, 8, 2, 8, 90, 5, 8, 3, 3}
# Displaying the initial set
print("Initial Set:", my_set)
# Prompting the user to enter a new item
new_item = int(input("Enter a new item: "))
# Adding the new item to the set using the add() method
my_set.add(new_item)
# Displaying the updated set
print("Updated Set:", my_set)
# Counting the occurrences of each element in the set
occurrences = {}
for item in my_set:
    # If the element is already in the occurrences dictionary, increment its count
    # Otherwise, add the element to the dictionary with a count of 1
    occurrences[item] = occurrences.get(item, 0) + 1
# Displaying the occurrences of each element in the set
print("Element Occurrences:")
for item, count in occurrences.items():
    print(f"{item}: {count}")
    
# Creating a set
my_set = {2, 5, 8, 2, 56, 8, 2, 8, 90, 5, 8, 3, 3}
# Displaying the initial set
print("Initial Set:", my_set)
# Prompting the user to enter a new item
new_item = int(input("Enter a new item: "))
# Adding the new item to the set using the add() method
my_set.add(new_item)
# Displaying the updated set
print("Updated Set:", my_set)
# Clearing the set using the clear() method
my_set.clear()
# Displaying the empty set
print("Cleared Set:", my_set)
# Example: Creating a set from a list
numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
unique_numbers = set(numbers)
print("Unique Numbers Set:", unique_numbers)
# Example: Set operations - union, intersection, difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print("Union Set:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection Set:", intersection_set)
difference_set = set1.difference(set2)
print("Difference Set (set1 - set2):", difference_set)

# Create an empty set
my_set = set()
# Ask the user for the number of items they want to add to the set
times = int(input("Enter the number of items you want to add to the set: "))
# Loop to add items to the set
for i in range(times):
    item = input("Enter the name of the item you want to add: ")
    my_set.add(item)
# Print the set
print(my_set)
# Loop to print each item in uppercase
for item in my_set:
    print(item.upper())
    
my_set = set()
num_count = int(input("Enter the number of elements you want to add to the set: "))
for _ in range(num_count):
    num = int(input("Enter a number: "))
    my_set.add(num)
print(my_set)
addition = 0
for number in my_set:
    addition += number
print("Sum of the set elements:", addition)
multiplication = 1
for number in my_set:
    multiplication *= number
print("Product of the set elements:", multiplication)

# Difference in Sets
# The difference operation returns a new set containing elements that are present in the first set but not in the second set.
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Difference: Elements present in set1 but not in set2
difference = set1 - set2
print("Difference:", difference)
# Output: Difference: {1, 2, 3}
# Symmetric Difference in Sets
# The symmetric difference operation returns a new set containing elements that are present in either of the sets, but not in both.
# Symmetric Difference: Elements present in either set1 or set2, but not in both
symmetric_difference = set1 ^ set2
print("Symmetric Difference:", symmetric_difference)
# Output: Symmetric Difference: {1, 2, 3, 6, 7, 8}

# Set Comprehension
# Set comprehension allows creating sets in a concise and expressive manner.
# Syntax:
# {expression for item in iterable if condition}
# Example 1: Creating a set of squares of numbers from 1 to 5
squares = {x ** 2 for x in range(1, 6)}
# Output: {1, 4, 9, 16, 25}
# Example 2: Creating a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
# Output: {2, 4, 6, 8, 10}
# Example 3: Creating a set of unique characters from a string
message = "hello world"
unique_chars = {char for char in message if char.isalpha()}
# Output: {'e', 'l', 'h', 'r', 'o', 'd', 'w'}
# Example 4: Creating a set of lengths of words in a sentence
sentence = "This is a sample sentence"
word_lengths = {len(word) for word in sentence.split()}
# Output: {1, 2, 4, 7, 8}
# - Set comprehension can be used to filter elements using conditions.
# - The resulting set contains unique elements only.
# - If the expression evaluates to a duplicate value, it will be ignored.
# Set comprehension is a powerful technique for creating sets based on existing iterables and applying filtering conditions. 
# It provides a concise and efficient way to generate sets with specific characteristics.

# Set Comprehension Example
# Create a set of odd numbers from 1 to 100 using set comprehension.
# Syntax:
# {expression for item in iterable if condition}
# Here, we use set comprehension to generate a set of odd numbers.
# We iterate over the range from 1 to 100 and only include the numbers that are not divisible by 2 (i.e., odd numbers).
# Step 1: Define the set using set comprehension.
set1 = {i for i in range(1, 101) if i % 2 != 0}
# Output: {1, 3, 5, 7, 9, ..., 99}
# Step 2: Print the resulting set.
print(set1)

# Generate a Set of Student Names

# Create a set of student names.
student_set = {
    'John',
    'Emma',
    'Liam',
    'Olivia',
    'Noah',
    'Sophia',
    'Harper',
    'Alexander',
    'Mason',
    'Eleanor',
    'Peter',
    'Amber'
}

# Create a new set containing only student names ending with 'r'.
students_names_ends_with_r = {name for name in student_set if name.endswith('r')}
# Output the original set of student names.
print("Original Set of Student Names:")
print(student_set)
# Output the set of student names ending with 'r'.
print("Student Names Ending with 'r':")
print(students_names_ends_with_r)
# Output the uppercase version of each student name ending with 'r'.
print("Uppercase Student Names Ending with 'r':")
for name in students_names_ends_with_r:
    print(name.upper())

# Set Methods in Python Sets

# Create a set of student names
student_set = {
    'John',
    'Emma',
    'Liam',
    'Olivia',
    'Noah',
    'Sophia',
    'Harper',
    'Alexander',
    'Mason',
    'Eleanor',
    'Peter',
    'Amber'
}

# 1. add() - Adds an element to the set
student_set.add('Lucas')

# 2. clear() - Removes all elements from the set
student_set.clear()

# 3. copy() - Returns a shallow copy of the set
student_set_copy = student_set.copy()

# 4. discard() - Removes an element from the set if it exists, otherwise does nothing
student_set.discard('Peter')

# 5. isdisjoint() - Returns True if two sets have no common elements, otherwise False
other_set = {'Alice', 'Bob', 'Charlie'}
is_disjoint = student_set.isdisjoint(other_set)

# 6. issuperset() - Returns True if a set is a superset of another set, otherwise False
is_superset = student_set.issuperset(other_set)

# 7. issubset() - Returns True if a set is a subset of another set, otherwise False
is_subset = student_set.issubset(other_set)

# 8. pop() - Removes and returns an arbitrary element from the set
popped_element = student_set.pop()

# 9. remove() - Removes an element from the set, raises KeyError if the element is not found
student_set.remove('Olivia')

# 10. update() - Updates the set with the union of itself and others
other_set = {'David', 'Emily'}
student_set.update(other_set)

# Print the modified set and other results
print(student_set)
print(student_set_copy)
print(is_disjoint)
print(is_superset)
print(is_subset)
print(popped_element)

# Set Methods in Python Sets

# Create a set
my_set = {1, 2, 3}

# 1. Add an element to the set using add() method
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# 2. Remove an element from the set using remove() method
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# 3. Check if an element is present in the set using the in keyword
print(3 in my_set)  # Output: True

# 4. Get the length of the set using len() method
print(len(my_set))  # Output: 3

# 5. Create another set for set operations
set2 = {3, 4, 5}

# 6. Perform union of two sets using the union() method or the '|' operator
union_set = my_set.union(set2)
print(union_set)  # Output: {1, 3, 4, 5}

# 7. Perform intersection of two sets using the intersection() method or the '&' operator
intersection_set = my_set.intersection(set2)
print(intersection_set)  # Output: {3, 4}

# 8. Perform difference between two sets using the difference() method or the '-' operator
difference_set = my_set.difference(set2)
print(difference_set)  # Output: {1}

# 9. Perform symmetric difference between two sets using the symmetric_difference() method or the '^' operator
symmetric_difference_set = my_set.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 5}

# 10. Check if a set is a subset of another set using the issubset() method
subset = {1, 3}
print(subset.issubset(my_set))  # Output: True

# 11. Check if a set is a superset of another set using the issuperset() method
superset = {1, 3, 4, 5}
print(superset.issuperset(my_set))  # Output: True

# 12. Remove and return an arbitrary element from the set using pop() method
popped_item = my_set.pop()
print(popped_item)
print(my_set)

# 13. Remove an element from the set using discard() method
my_set.discard(4)
print(my_set)

# 14. Check if two sets are disjoint (i.e., have no common elements) using the isdisjoint() method
set3 = {6, 7}
print(my_set.isdisjoint(set3))  # Output: True

# 15. Create a shallow copy of the set using the copy() method
my_set_copy = my_set.copy()
print(my_set_copy)

# 16. Clear all elements from the set using clear() method
my_set.clear()
print(my_set)  # Output: set()

# 17. Remove an element from the set using remove() method
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# 18. Update the set with elements from another iterable using update() method
my_set.update({4, 5, 6})
print(my_set)  # Output: {1, 3, 4, 5, 6}

# Example 1:
# Create two empty sets
set1 = set()
set2 = set()
# Prompt the user to enter the number of elements for set1
times = int(input("Enter the number of elements you want to add to set1: "))
# Add elements to set1
for i in range(times):
    item = input("Enter an item you wish to add to set1: ")
    set1.add(item)
print("set1:", set1)
# Prompt the user to enter the number of elements for set2
times = int(input("Enter the number of elements you want to add to set2: "))
# Add elements to set2
for i in range(times):
    item = input("Enter an item you wish to add to set2: ")
    set2.add(item)
print("set2:", set2)
# Find the intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("The Intersection of set1 and set2 is: ")
for item in intersection_set:
    print(item)

# Example 2:
# Create two empty sets
set1 = set()
set2 = set()
# Prompt the user to enter the number of items for set1
times = int(input("Enter the number of items you wish to add to set1: "))
# Add items to set1
for i in range(times):
    item = input("Enter an item you wish to add to set1: ")
    set1.add(item)
print("set1:", set1)
# Prompt the user to enter the number of items for set2
times = int(input("Enter the number of items you wish to add to set2: "))
# Add items to set2
for i in range(times):
    item = input("Enter an item you wish to add to set2: ")
    set2.add(item)
print("set2:", set2)
# Check if set2 is a subset of set1
if set2.issubset(set1):
    print("set2 is a subset of set1")
else:
    print("set1 is a subset of set2")

# Example 3:
# Create a set of special main course dishes for the Queen's menu
queen_menu = {
    "Roast Beef with Yorkshire Pudding",
    "Braised Lamb Shank with Mint Sauce",
    "Grilled Salmon with Lemon Butter",
    "Beef Wellington",
    "Chicken Tikka Masala",
    "Shepherd's Pie",
    "Prawn Linguine with Garlic and Chilli",
    "Venison Medallions with Red Wine Sauce",
    "Lobster Thermidor",
    "Rack of Lamb with Rosemary and Garlic"
}
# Print the original Queen's menu
print("Queen's Menu:")
print(queen_menu)
# Prompt the user to enter an item they wish to remove from the menu
item = input("Enter the item you wish to remove from the menu: ")
# Create a new menu set without the specified item, converting the items to uppercase
new_menu = {i.upper() for i in queen_menu if i != item}
# Print the new menu
print("New Menu:")
print(new_menu)
