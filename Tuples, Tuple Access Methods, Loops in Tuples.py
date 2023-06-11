# Tuple is a Data Type used in Python
my_tuple = ()  # Empty tuple

# Tuple is an immutable data type
#  Once a tuple is created, its elements cannot be modified or changed.
# However, we can perform operations on tuples such as accessing elements or creating new tuples

# Tuple is an ordered data structure having sequence in elements
# The order of elements in a tuple is preserved, meaning the items are indexed and accessible by their position

# Tuples contain multiple items having different data types
my_tuple = (1, "hello", 3.14, True)  # Tuple with different data types

# Tuple is an ordered data structure having sequence in elements
my_tuple = (1, 2, 3)  # Tuple with ordered elements

# Tuple items are stored in parentheses i.e. ()
my_tuple = (1, 2, 3)  # Tuple with elements enclosed in parentheses

# We can create a tuple inside another tuple i.e. nested tuple
nested_tuple = (1, (2, 3), ("hello", "world"))  # Tuple with nested tuple

# We can concatenate tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2  # Concatenating two tuples

# We can repeat a tuple many times using the "*" symbol
repeated_tuple = (1, 2) * 3  # Repeating the tuple three times

# We can use the membership operator to check any element in a tuple
my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True
print(4 in my_tuple)  # Output: False

# We can iterate over tuple items one by one
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)  # Printing each item in the tuple
    
# Tuple access methods
# 1. Accessing Tuple Elements using Index (Positive and Negative)
# Example: Create a tuple
fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
# Accessing elements using positive index
first_fruit = fruits[0]  # Access the first element
last_fruit = fruits[4]   # Access the last element

# Accessing elements using negative index
second_last_fruit = fruits[-2]  # Access the second last element
third_fruit = fruits[-3]        # Access the third element

# 2. Accessing Tuple Elements using a For Loop
# Example: Iterate over the tuple elements
for fruit in fruits:
    print(fruit)
# Example 1 
# write a python program that allows the user to get 10 student names
# store them in a tuple, and print the names in uppercase
# Get 10 student names from the user
names = []  # Create an empty list to store the names
for i in range(10):
    name = input("Enter student name: ")
    names.append(name)  # Add the name to the list
# Convert the list of names to a tuple
student_names = tuple(names)
# Print the names in uppercase
for name in student_names:
    print(name.upper())

# Loop with Python Tupple
# Problem 1: Python Program To Get 5 Words From User and Display Only Those Ending with "n"

# Initialize an empty list to store the words
word_list = []

# Get 5 words from the user
for _ in range(5):
    word = input("Enter a word: ")
    word_list.append(word)
# Convert the list to a tuple
words_tuple = tuple(word_list)
# Iterate over each word in the tuple
for word in words_tuple:
    # Check if the word ends with "n"
    if word.endswith("n"):
        # Display the word
        print(word)
        
# Problem 2: Python Program To Get 10 Numbers From User and Display Numbers Divisible by 2 and 3
# Initialize an empty list to store the numbers
number_list = []
# Get 10 numbers from the user
for i in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)
# Iterate over each number in the list
for number in number_list:
    # Check if the number is divisible by both 2 and 3
    if number % 2 == 0 and number % 3 == 0:
        # Display the number
        print(number)
        
# Creating a Tuple ysing List Comprehension
# Example: Creating a Tuple using List Comprehension
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List comprehension to create a tuple of even numbers
even_numbers = tuple(num for num in numbers if num % 2 == 0)
# Display the tuple of even numbers
print(even_numbers)

# Tuple Methods
# Create a list
my_list = [10, 20, 30, 40, 50, 20, 30, 20]

# Count(): Returns the number of occurrences of a value in the list
count = my_list.count(20)
print("Count of 20:", count)

# Index(): Returns the index of the first occurrence of a value in the list
index = my_list.index(30)
print("Index of 30:", index)

# Overview: Prints the list
print("List:", my_list)

# Max(): Returns the maximum value in the list
maximum = max(my_list)
print("Maximum value:", maximum)

# Min(): Returns the minimum value in the list
minimum = min(my_list)
print("Minimum value:", minimum)

# Tuple(): Converts the list to a tuple
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)

# Len(): Returns the length of the list
length = len(my_list)
print("Length of list:", length)

# Del: Deletes an element or a slice from the list
del my_list[2]  # Delete element at index 2
print("List after deleting element at index 2:", my_list)

del my_list[1:4]  # Delete elements in the range from index 1 to 3
print("List after deleting elements in the range [1:4]:", my_list)


# Example 1: Write a Python Program that gets 10 numbers from the user, stores in a Tuple
# find their sum and multiplication
# Create an empty list to store numbers
numbers = []
# Get 10 numbers from the user and append them to the list
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Convert the list to a tuple
numbers_tuple = tuple(numbers)
# Calculate the sum of all numbers in the tuple
addition = sum(numbers_tuple)
# Calculate the multiplication of all numbers in the tuple
multiplication = 1
for num in numbers_tuple:
    multiplication *= num
# Display the result
print("Sum of all numbers:", addition)
print("Multiplication of all numbers:", multiplication)





