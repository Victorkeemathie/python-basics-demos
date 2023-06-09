# 1. Title: Introduction to Arrays in Python

# Explanation:
# An array in Python is a collection of items with the same data type that are stored in contiguous memory locations.
# Arrays can be one-dimensional (vector) or multi-dimensional (table-like). The array elements are the individual items
# stored in the array, and each element has a unique index for accessing it. The size of an array refers to the total
# number of elements it can hold. The name of the array is the variable name used to declare it. Array elements are the
# items or data stored within the array. The index is a unique number assigned to each array element, allowing us to
# access specific elements by their index value. The memory location refers to the specific and unique memory address
# where each element is stored in the computer's memory device.

# Example 1: Creating an array using NumPy and accessing elements
# Importing the required library
import numpy as np
# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Printing the type of the array
print(type(arr))
# Printing the array
print(arr)
# Accessing elements of the array
print(arr[1])       # Output: 2
print(arr[-3])      # Output: 7
# Example 2: Using a loop to iterate through array elements
# Iterating through the array and printing each element
for element in arr:
    print(element)

# Example 3: Deleting an element from the array using NumPy
# Deleting the first element of the array
arr = np.delete(arr, 0)
# Printing the updated array
print(arr)

# Example 4: Creating an array and finding the product of its elements
# Creating an empty array
arr = np.array([])
# Taking input from the user to fill the array
for _ in range(5):
    num = int(input("Enter an element for the array: "))
    arr = np.append(arr, num)
# Printing the array
print(arr)

# Calculating the product of array elements
product = 1
for element in arr:
    product *= element
# Printing the product
print("Product of array elements:", product)

# Example 5: Converting an array to a list and calculating the sum
# Creating an array
user_array = np.array([2, 3, 4, 5, 6, 7, 8, 9])
# Converting array to a list
user_list = user_array.tolist()
# Printing the type and contents of the list
print(type(user_list))
print(user_list)
# Printing the type and contents of the array
print(type(user_array))
print(user_array)
# Calculating the sum of the list
sum_total = sum(user_list)
print("Sum of the list:", sum_total)

# Example 6: Creating an array and performing calculations on its elements
# Creating an empty array
user_array = np.array([])
# Taking input from the user to fill the array
for _ in range(10):
    num = int(input("Enter a number: "))
    user_array = np.append(user_array, num)
# Printing the array
print(user_array)
# Performing calculations on array elements
for number in user_array:
    num_squared = number**2
    num_result = num_squared + 5
    print(num_result)
    
# Note: To install the NumPy library, use the following command in the command prompt or terminal:
# pip install numpy

# Note: The examples above cover basic array operations, but NumPy provides many more advanced features for
# array manipulation and mathematical computations.
