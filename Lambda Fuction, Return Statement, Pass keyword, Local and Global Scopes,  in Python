# 1. Return Statement
# The Return Statement is used in a function to specify the value that should be sent back or "returned" to the caller of the function.
# When a return statement is encountered in a function, the function execution stops, and the value specified in the return statement is passed back as the result of the function
# This returned value can then be stored in a variable, used in expressions, or printed as output
# Syntax:
#             return [expression]
def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(5, 3)
print(result)  # Output: 8


# 2. Pass Keyword
# Pass Keyword is used as a placeholder or a filler statement when you want to have a syntactically correct block of code that does nothing
# It does not perform any action or have any functionality
# It simply acts as a null operation, allowing you to define empty code blocks without causing any errors
# Syntax:
def process_data(data):
    if data > 0:
        # Perform some operation
        pass
    else:
        # Handle the case when data is less than or equal to 0
        pass
# 3. Lambda Function
# An Anonymous Function, also known as a Lambda Function, is a function that is defined without a name
# It is commonly used when you need a simple function that you don't intend to reuse elsewhere in your code
# Syntax:
lambda arguments: expression
# Lambda Example 1:
# An anonymous function to calculate the square of a number
square = lambda x: x**2

result = square(5)
print(result)  # Output: 25
# Lambda Example 2:
name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")

show_full_name = lambda name1, name2: print(name1 + " " + name2)
show_full_name(name1, name2)

# 4. Local Scope
# Local scope refers to the visibility of variables limited to a specific block or function where they are defined
# Variables defined inside a function or block are considered local variables and can only be accessed within that specific function or block
# Local Variable Example:
def greet():
    name = "John"  # Local variable
    print("Hello, " + name)

greet()  # Output: Hello, John
print(name)  # Error: name is not defined (not accessible outside the function)

# 5. Global Scope
# Global scope refers to the visibility of variables that can be accessed from anywhere in the program
# Variables defined outside of any function or block are considered global variables and can be accessed throughout the program
# Global Scope Example:
name = "John"  # Global variable

def greet():
    print("Hello, " + name)

greet()  # Output: Hello, John
print(name)  # Output: John (accessible outside the function)








