# List is a data type in Python.
# Example:
my_list = [1, 2, 3, 4, 5]

# Lists are mutable data types.
# Example:
my_list[0] = 10

# Lists can contain multiple values of different data types.
# Example:
my_list = [1, "two", 3.0, True]

# Lists are ordered data structures that store a sequence of elements.
# Example:
my_list = [10, 20, 30, 40, 50]

# List elements are enclosed in square brackets, i.e., [].
# Example:
my_list = [1, 2, 3]

# We can create a nested list, which is a list inside another list.
# Example:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Lists can be concatenated using the "+" operator.
# Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

# Lists can be repeated multiple times using the "*" operator.
# Example:
my_list = [1, 2, 3] * 3

# We can use the membership operator "in" to check if an element is present in a list.
# Example:
if 3 in my_list:
    print("Number 3 is present in the list.")
else:
    print("Number 3 is not present in the list.")

# We can iterate over the items in a list.
# Example:
for item in my_list:
    print(item)

# Accessing elements in a list
# 1. Using index
my_list = [10, 20, 30, 40, 50]
# Accessing a single element using its index
element = my_list[2]  # Accessing the element at index 2 (30)
print("Accessing element using index:")
print("Element at index 2:", element)

# Accessing a range of elements using slicing
sub_list = my_list[1:4]  # Accessing elements from index 1 to 3 (20, 30, 40)
print("Accessing a range of elements using slicing:")
print("Sublist:", sub_list)
# Accessing elements from the end of the list using negative indexing
last_element = my_list[-1]  # Accessing the last element (-50)
print("Accessing the last element using negative indexing:")
print("Last element:", last_element)

# 2. Using a loop
my_list = [10, 20, 30, 40, 50]
print("Accessing elements using a loop:")
for element in my_list:
    print(element)
    
# List Methods in Python
# 1. append(item)
# Syntax: list.append(item)
# Adds an item to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print("append(item) example:")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 2. extend(iterable)
# Syntax: list.extend(iterable)
# Adds all the elements from an iterable (e.g., another list) to the end of the list.
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print("extend(iterable) example:")
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert(index, item)
# Syntax: list.insert(index, item)
# Inserts an item at a specified index in the list.
colors = ['red', 'blue', 'green']
colors.insert(1, 'yellow')
print("insert(index, item) example:")
print(colors)  # Output: ['red', 'yellow', 'blue', 'green']

# 4. remove(item)
# Syntax: list.remove(item)
# Removes the first occurrence of the specified item from the list.
pets = ['dog', 'cat', 'rabbit', 'cat']
pets.remove('cat')
print("remove(item) example:")
print(pets)  # Output: ['dog', 'rabbit', 'cat']

# 5. pop([index])
# Syntax: list.pop([index])
# Removes and returns the item at the specified index. If no index is provided, removes and returns the last item.
numbers = [1, 2, 3, 4, 5]
removed_item = numbers.pop(2)
print("pop([index]) example:")
print("Removed item:", removed_item)  # Output: 3
print("Updated list:", numbers)  # Output: [1, 2, 4, 5]

# 6. index(item)
# Syntax: list.index(item)
# Returns the index of the first occurrence of the specified item in the list.
fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print("index(item) example:")
print("Index of 'banana':", index)  # Output: 1

# 7. count(item)
# Syntax: list.count(item)
# Returns the number of occurrences of the specified item in the list.
numbers = [1, 2, 3, 2, 4, 2]
count = numbers.count(2)
print("count(item) example:")
print("Count of '2':", count)  # Output: 3

# 8. sort()
# Syntax: list.sort()
# Sorts the list in ascending order.
numbers = [5, 2, 7, 1, 4]
numbers.sort()
print("sort() example:")
print(numbers)  # Output: [1, 2, 4, 5, 7]
# Additional example and explanation
# Sorts the list in descending order using the reverse parameter.
# The reverse parameter is set to True to indicate descending order.
numbers = [5, 2, 7, 1, 4]
numbers.sort(reverse=True)
print("sort(reverse=True) example:")
print(numbers)  # Output: [7, 5, 4, 2, 1]

# 9. reverse()
# Syntax: list.reverse()
# Reverses the order of the elements in the list.
colors = ['red', 'green', 'blue']
colors.reverse()
print("reverse() example:")
print(colors)  # Output: ['blue', 'green', 'red']

# 10. copy()
# Syntax: list.copy()
# Creates a shallow copy of the list.
# The new list contains the same elements as the original list.
numbers = [1, 2, 3, 4, 5]
numbers_copy = numbers.copy()
print("copy() example:")
print(numbers_copy)  # Output: [1, 2, 3, 4, 5]

# 11. join()
# Syntax: separator.join(list)
# Concatenates all elements of the list into a single string using the specified separator.
fruits = ["apple", "banana", "orange"]
fruits_string = ", ".join(fruits)
print("join() example:")
print(fruits_string)  # Output: "apple, banana, orange"

# 12. clear()
# Syntax: list.clear()
# Removes all elements from the list, making it empty.
languages = ["Python", "Java", "C++"]
languages.clear()
print("clear() example:")
print(languages)  # Output: []

# 13. len()
# Syntax: len(list)
# Returns the number of elements in the list.
animals = ["cat", "dog", "elephant", "lion"]
num_animals = len(animals)
print("len() example:")
print(num_animals)  # Output: 4


"""
Write a Python program to collect names of 5 students
from the user, store them in a list, and display the list in uppercase
"""
# Initialize an empty list to store student names
student_list = []

# Prompt the user to enter 5 student names
for _ in range(5):
    name = input("Enter the name of the student: ")
    # Convert the name to uppercase
    name_upper = name.upper()
    # Append the uppercase name to the list
    student_list.append(name_upper)

# Print the list of student names in uppercase
print(student_list)

"""
Write a Python program that prompts the user to enter 10 numbers
stores them in a list, and then displays only the odd numbers from the list
"""
# Initialize an empty list to store the numbers
number_list = []

# Iterate 10 times to get 10 numbers from the user
for i in range(10):
    number = int(input("Enter a number: "))
    # Check if the number is odd
    if number % 2 != 0:
        # If the number is odd, append it to the number_list
        number_list.append(number)
# Print the list of odd numbers
print("Odd numbers:", number_list)

# Alternatively:
# Initialize an empty list to store the numbers
number_list = []
# Iterate 10 times to get 10 numbers from the user
for i in range(10):
    number = int(input("Enter a number: "))
    # Check if the number is odd using a for loop
    for num in range(number, number + 1):
        if num % 2 != 0:
            # If the number is odd, append it to the number_list
            number_list.append(number)
# Print the list of odd numbers
print("Odd numbers:", number_list)

# Alternatively:
# Initialize an empty list to store the numbers
number_list = []
# Counter to keep track of the number of inputs
count = 0
# Continue loop until we get 10 numbers
while count < 10:
    number = int(input("Enter a number: "))
    # Check if the number is odd using a while loop
    while number % 2 != 0:
        # If the number is odd, append it to the number_list
        number_list.append(number)
        count += 1
        break
# Print the list of odd numbers
print("Odd numbers:", number_list)

# Loop with Python
"""
Write a Python program to get 5 words from the user
store the words that start with 'b' in a list, and display the list
 """
lst = []
for i in range(5):
    word = input("Enter a word: ")
    # Use the lower() method to convert the word to lowercase before checking the starting character
    if word.lower().startswith("b"):
        lst.append(word)
    # Print the list after the loop is completed, not within the loop
print(lst)

# Alternatively:
# Initialize an empty list to store the words starting with 'b'
st = []
# Iterate 5 times to get 5 words from the user
for i in range(5):
    word = input("Enter a word: ")
    st.append(word)
# Iterate over the words in the list
for word in st:
    # Check if the word starts with 'b' (case-insensitive)
    if word.lower().startswith("b"):
        # Print the word if it meets the condition
        print(word)

"""
Write a Python program to get 10 numbers from the use
and display the numbers that are between 10 and 20
"""
# Initialize an empty list to store the numbers
numbers = []
# Iterate 10 times to get 10 numbers from the user
for i in range(10):
    num = int(input("Enter a number: "))
    # Check if the number is between 10 and 20
    if 10 < num < 20:
        # If the number meets the condition, append it to the list
        numbers.append(num)
# Print the list of numbers that satisfy the condition
print(numbers)


# Python List Comprehension
# Python List Comprehension means creating a new list from an existing list based on a given condition
# We can filter the old list to get the required elements and store them in a new list
# Syntax: [expression for item in old_list if condition]

# Example without List Comprehension:
old_list = [1, 2, 3, 4, 5]
new_list = []
# Iterate over the elements in the old list
for item in old_list:
    # Check if the item meets the condition (even numbers)
    if item % 2 == 0:
        # Add the item to the new list
        new_list.append(item)
# Print the new list
print(new_list)

# Example with List Comprehension:
old_list = [1, 2, 3, 4, 5]
# Use list comprehension to create a new list of even numbers
new_list = [item for item in old_list if item % 2 == 0]
# Print the new list
print(new_list)

# Example 1: Squaring Numbers
# Create a new list with squares of numbers from 1 to 10
# Using list comprehension
squares = [x ** 2 for x in range(1, 11)]
# Print the resulting list
print(squares)

# Example 2: Filtering Odd Numbers
# Create a new list with only the odd numbers from an existing list
# Existing list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using list comprehension to filter odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
# Print the resulting list
print(odd_numbers)

# Example 3: Extracting First Characters
# Create a new list with the first character of each word in an existing list
# Existing list of words
words = ["apple", "banana", "cherry", "date"]
# Using list comprehension to extract first characters
first_chars = [word[0] for word in words]
# Print the resulting list
print(first_chars)

# Example 4: Combining Two Lists
# Create a new list by combining elements from two existing lists
# Existing lists
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
# Using list comprehension to combine the lists
combined_list = [str(num) + letter for num in numbers for letter in letters]
# Print the resulting list
print(combined_list)

# Write a Python program to get 5 numbers from the user
# store them in a list, and display their squares using a for loop
# Prompt the user to enter 5 numbers
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Calculate and display the square of each number using a for loop
print("Squares of the numbers:")
for num in numbers:
    square = num ** 2
    print(square)









