# 1. Funtions in Python
# A Function is a block of reusable code that performs a specific task
# It allows you to break down a program into smaller, more manageable pieces, which can be called and executed whenever needed
# Functions are defined using the def keyword, followed by the function name and parentheses
# Syntax:
#            def function_name(parameter1, parameter2, ...):
     # Function body
     # Code to be executed when the function is called
     # Optionally, return a value using the return statement

# Example 1:
def square(num):
    return num ** 2

result = square(5)
print(result)  # Output: 25

# Example 2:
def square(num):
    return num ** 2

result = square(5)
print(result)  # Output: 25

# Example 3:
def greatest_num():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    if num1 > num2 and num1 > num3:
        print(str(num1) + " is the greatest.")
    elif num2 > num1 and num2 > num3:
        print(str(num2) + " is the greatest.")
    elif num3 > num1 and num3 > num2:
        print(str(num3) + " is the greatest.")
    else:
        print("Check your input values and try again.")

greatest_num()

# Example 4:
def multiplication_table(num):
    i = 10
    while i >= 0:
        print(str(num) + " * " + str(i) + " = " + str(num * i))
        i -= 1

num = int(input("Enter a number to get its multiplication table: "))
multiplication_table(num)

# Example 5
def multiplication_table(num):
    i = 10
    while i >= 0:
        print(str(num) + " * " + str(i) + " = " + str(num * i))
        i -= 1

num = int(input("Enter a number to get its multiplication table: "))
multiplication_table(num)

# Example 6:
def multiplication_table(num):
    for i in range(10, -1, -1):
        print(str(num) + " * " + str(i) + " = " + str(num * i))

num = int(input("Enter a number to get its multiplication table: "))
multiplication_table(num)

# Example 7:
def circle_and_square_area_calculator():
    selection = input("Enter the figure you want to calculate the area for: ")
    if selection.lower() == "circle":
        radius = int(input("Enter the radius of the Circle: "))
        area1 = radius ** 2 * (22 / 7)
        print("The area of a Circle with radius " + str(radius) + " is: " + str(area1))
    elif selection.lower() == "square":
        length = int(input("Enter the length of the Square: "))
        area2 = length ** 2
        print("The area of a Square with length " + str(length) + " is: " + str(area2))
    else:
        print("Check your figure type selection and try again")

circle_and_square_area_calculator()

# Example 8:
user_name = input("Enter your username: ")
length = len(user_name)

if user_name.isalnum() and 8 <= length <= 20:
    print(user_name)
else:
    if not user_name.isalnum():
        print("Your username should only contain alphanumeric characters.")
    else:
        print("The length of your username should be between 8 and 20 characters.")


# 2. Parameters and Arguements:
# Syntax:
# Parameters in a function definition
 def greet(name):  # 'name' is a parameter
     print("Hello, " + name + "!")

# Arguments in a function call
# greet("Alice")  # 'Alice' is an argument

# Keyword ArguementS:
# Keyword arguments explicitly mention the parameter names and their corresponding values
def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet(name="Alice", age=25)  # Using keyword arguments

# Default Arguements:
# Default arguments are used to provide a default value to a parameter in a function definition

def greet(name, age=30):  # 'age' has a default value of 30
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Bob")  # 'age' is not provided, so it defaults to 30

# Required Arguments:
# Required arguments are parameters that must be provided with values during a function call
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # 'name' is a required argument










