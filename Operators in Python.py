# This code demonstrates various types of operators in Python

# Arithmetic Operators: +, -, *, /, %
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus

# Relational Operators: ==, !=, >, >=, <, <=
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to
print(num1 > num2)   # Greater than
print(num1 < num2)   # Less than

# Compound Assignment Operators
x = 10
x += 2  # Addition assignment operator
print(x)  # Output: 12
x -= 2  # Subtraction assignment operator
print(x)  # Output: 10
x *= 2  # Multiplication assignment operator
print(x)  # Output: 20
x /= 2  # Division assignment operator
print(x)  # Output: 10.0
x %= 2  # Modulus assignment operator
print(x)  # Output: 0.0

# Logical Operators: and, or, not
a = 2
b = 4
c = 6
d = 8
print(c > b and d > b)   # Output: True
print(c > b or d > b)    # Output: True
print(not(a > b))        # Output: True

# User Authentication
username = "user1"
password = "QWerty"
name = input("Enter your username: ")
pwd = input("Enter your password: ")

if username == name and password == pwd:
    print("Your username and password match")
else:
    print("Incorrect username or password")

# User Authentication (Alternative)
username = "User1"
pwd = "QWerty"
name = input("Enter your username: ")
password = input("Enter your password: ")

if username == name or pwd == password:
    print("Your username or password is correct, or both of them are correct")
else:
    print("Sorry, your username and password are incorrect")

# Membership Operators: in, not in
lst = [2, 3, 5, 7]
print(2 in lst)  # Output: True
tpl = (2, 3, 5, 7)
print(10 in tpl)  # Output: False

lst = ["blue", "pink", "green", "grey", "black", "white"]
colour_name = input("Enter a color name: ")

if colour_name in lst:
    print(colour_name + " color is present.")
    print(lst)
else:
    print(colour_name + " color is not present.")

# Identity Operators: is, is not
a = 10
b = 20
c = 10
print(a is b)          # Output: False
print(a is c)          # Output: True
print(a is not b)      # Output: True
print(a is not c)      # Output: False

# Bitwise Operators: &, |, ~, ^
# Bitwise operators perform operations on binary representations of integers
# Usage of bitwise operators is not demonstrated in the provided code

