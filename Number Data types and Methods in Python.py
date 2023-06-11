# Examples of Number Data Types in Python include:
# Integer, Floating-point, Complex, Decimal, Fraction
# They are immutable data types.
# These data types can be used to represent and manipulate different kinds of numbers.

# Integer (int):
# Syntax: x = 10
# Integers are whole numbers without any decimal point.
# They can be positive or negative.
# Examples:
x = 10
y = -5
z = 0

# Floating-Point (float):
# Syntax: x = 3.14
# Floating-point numbers are numbers with a decimal point.
# They can represent both whole and fractional numbers.
# Examples:
x = 3.14
y = -0.5
z = 1.0

# Complex (complex):
# Syntax: x = 3 + 5j
# Complex numbers are numbers in the form a + bj, where a is the real part and b is the imaginary part.
# Examples:
x = 3 + 5j
y = -2j
z = 4 + 0j

# Decimal (decimal):
# Syntax: from decimal import Decimal
# Decimal numbers are used for precise decimal arithmetic.
# They are often used in financial calculations.
# Examples:
from decimal import Decimal

x = Decimal('3.14')
y = Decimal('0.5')
z = Decimal('-2.25')

# Fraction (fractions):
# Syntax: from fractions import Fraction
# Fraction numbers represent rational numbers as fractions (numerator/denominator).
# Examples:
from fractions import Fraction

x = Fraction(1, 2)  # Represents 1/2
y = Fraction(3, 4)  # Represents 3/4
z = Fraction(5, 2)  # Represents 5/2

# These number data types provide different functionalities and are suitable for different use cases.
# You can perform various operations and calculations using these data types.
# It's important to choose the appropriate data type based on the requirements of your program.

# Data type conversion in Python

# Integer to other data types:
x = 3478
int_to_float = float(x)  # Convert integer to float
int_to_complex = complex(x)  # Convert integer to complex

# Float to other data types:
y = 3.14
float_to_int = int(y)  # Convert float to integer
float_to_complex = complex(y)  # Convert float to complex

# Complex to other data types:
z = 2 + 3j
complex_to_int = int(z.real)  # Convert complex to integer (taking the real part)
complex_to_float = float(z.real)  # Convert complex to float (taking the real part)

# String to other data types:
s = "42"
string_to_int = int(s)  # Convert string to integer
string_to_float = float(s)  # Convert string to float

# Note: Conversion from complex to int or float is not possible directly, 
#       as complex numbers have both real and imaginary parts.

# Number Methods in Python
# 1. pow(x, y)
# Returns x raised to the power of y.
result = pow(2, 3)
print(result)  # Output: 8

# 2. exp(x)
# Returns the exponential value of x (e^x).
result = exp(2)
print(result)  # Output: 7.3890560989306495

# 3. max(iterable)
# Returns the maximum value from an iterable.
numbers = [5, 8, 2, 1, 9]
max_num = max(numbers)
print(max_num)  # Output: 9

# 4. min(iterable)
# Returns the minimum value from an iterable.
numbers = [5, 8, 2, 1, 9]
min_num = min(numbers)
print(min_num)  # Output: 1

# 5. round(x, n)
# Rounds the number x to n decimal places.
result = round(3.14159, 2)
print(result)  # Output: 3.14

# 6. sqrt(x)
# Returns the square root of x.
result = sqrt(16)
print(result)  # Output: 4.0

# 7. choice(seq)
# Returns a random element from a non-empty sequence.
import random
colors = ['red', 'blue', 'green']
chosen_color = random.choice(colors)
print(chosen_color)  # Output: Randomly selected color from the list

# 8. randrange(start, stop[, step])
# Returns a randomly selected element from the range(start, stop, step).
import random
num = random.randrange(1, 10, 2)
print(num)  # Output: Random odd number between 1 and 10 (exclusive)

# 9. random()
# Returns a random floating-point number between 0 and 1.
import random
num = random.random()
print(num)  # Output: Random number between 0 and 1

# 10. shuffle(lst)
# Shuffles the elements in a list in-place.
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: Shuffled list

# 11. abs(x)
# Returns the absolute value of x.
result = abs(-5)
print(result)  # Output: 5

# 12. ceil(x)
# Returns the smallest integer greater than or equal to x.
import math
result = math.ceil(3.2)
print(result)  # Output: 4

# 13. cmp(x, y)
# Compares two values and returns -1 if x < y, 0 if x == y, or 1 if x > y.
# This function is deprecated in Python 3.
result = cmp(5, 3)
print(result)  # Output: 1

# 14. fabs(x)
# Returns the absolute value of x as a float.
import math
result = math.fabs(-3.5)
print(result)  # Output: 3.5

# 15. floor(x)
# Returns the largest integer less than or equal to x.
import math
result = math.floor(5.8)
print(result)  # Output: 5

# 16. log(x)
# Returns the natural logarithm of x.
import math
result = math.log(10)
print(result)  # Output: 2.302585092994046

# 17. log10(x)
# Returns the base-10 logarithm of x.
import math
result = math.log10(100)
print(result)  # Output: 2.0


# 18. modf(x)
# Returns the fractional and integer parts of x as a tuple.
import math
result = math.modf(4.5)
print(result)  # Output: (0.5, 4.0) - Fractional part: 0.5, Integer part: 4.0
# Note: The functions cmp(x, y) and fabs(x) are no longer available in Python 3. Use alternative methods for comparison and absolute value.

# 19. uniform(x, y)
# Returns a random floating-point number between x and y.
import random
result = random.uniform(1, 5)
print(result)

 # Example 1:
"""
Write a Python program that takes a number from the user, finds the square root of that number,
and then finds the square root of the resulting answer.
Finally, add the two square roots together and display the result to the user.
"""
import math
# Prompt the user to enter a number
num = int(input("Enter a number: "))
# Find the square root of the entered number
sqrt_num = math.sqrt(num)
# Find the square root of the previous answer
sqrt_sqrt_num = math.sqrt(sqrt_num)
# Add the two square roots
result = sqrt_num + sqrt_sqrt_num
# Display the result to the user
print(result)

# Example 2:
"""
Write a Python program that takes two numbers from the user, calculates their cubed values
and then finds the sum of the two cubed values
"""
# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Calculate the power of each number with 3
power1 = pow(num1, 3)
power2 = pow(num2, 3)
# Find the sum of the two power results
sum_of_powers = power1 + power2
# Display the final sum to the user
print(sum_of_powers)

# Example 3:
"""
Write a Python program to obtain 5 numbers
from the user and find the minimum number among them
"""
# Create an empty list to store the numbers
numbers = []
# Prompt the user to enter five numbers one by one
for i in range(5):
    num = int(input("Enter a number: "))  # Read a number from the user
    numbers.append(num)  # Add the number to the list
print(numbers)  # Print the list of numbers
# Find the minimum number in the list
min_num = min(numbers)
print("The minimum number is:", min_num)

# Example 4:
"""
Write a Python program to take a floating-point number
as input from the user and round it to the specified decimal place
"""
# Prompt the user to enter a floating-point number
num = float(input("Enter a floating-point number: "))
# Prompt the user to enter the desired rounding-off digit
round_digit = int(input("Enter the desired rounding-off digit: "))
# Round the number to the specified digit
rounded_num = round(num, round_digit)
# Print the rounded number
print("Rounded number:", rounded_num)
