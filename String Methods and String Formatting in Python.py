#  A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ")
# Immutable: Strings in Python are immutable, which means they cannot be modified once created
# Built in methods of operation perform on string:

# 1. len() : Returns the length of a string
# Syntax: len(string)
my_string = "Hello"
print(len(my_string))  # Output: 5

# 2. lower() : Converts all characters in a string to lowercase
# Syntax: string.lower()
my_string = "Hello"
print(my_string.lower())  # Output: "hello"

# 3. upper() : Converts all characters in a string to uppercase
# Syntax: string.upper()
my_string = "Hello"
print(my_string.upper())  # Output: "HELLO"

# 4. strip(): Removes leading and trailing whitespace from a string
# Syntax: string.strip()
my_string = "  Hello  "
print(my_string.strip())  # Output: "Hello"

# 5. replace(): Replaces occurrences of a substring with another substring
# Syntax: string.replace(old, new)
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: "Hello, Python!"

# 6. split(): Splits a string into a list of substrings based on a delimiter
# Syntax: string.split(delimiter)
my_string = "Hello, World!"
my_list = my_string.split(", ")
print(my_list)  # Output: ["Hello", "World!"]

# 7. join(): Joins a list of strings into a single string, using a specified delimiter
# Syntax: delimiter.join(list)
my_list = ["Hello", "World!"]
my_string = ", ".join(my_list)
print(my_string)  # Output: "Hello, World!"

# 8. startswith(): Checks if a string starts with a specified prefix
# Syntax: string.startswith(prefix)
my_string = "Hello, World!"
print(my_string.startswith("Hello"))  # Output: True
my_string = "Hello, World!"
print(my_string.startswith("Hello"))  # Output: True

# 9. endswith(): Checks if a string ends with a specified suffix
# Syntax: string.endswith(suffix)
my_string = "Hello, World!"
print(my_string.endswith("World!"))  # Output: True

# 10. capitalize() : Returns a copy of the string with its first character capitalized and the rest of the characters in lowercase
# Syntax: string.capitalize()
string = "hello world"
capitalized_string = string.capitalize()
print(capitalized_string)  # Output: "Hello world"

# 11. islower() :  Checks if all the characters in the string are lowercase
# Syntax: string.islower()
string = "hello"
print(string.islower())  # Output: True

# 12.  isupper() : Checks if all the characters in the string are uppercase
# Syntax: string.isupper()
text = "HELLO"
print(text.isupper())  # Output: True

# 13. title() : used to convert the first character of each word in a string to uppercase and all other characters to lowercase
# Syntax: string.title()
text = "hello world! welcome to python"
new_text = text.title()
print(new_text)  # Output: Hello World! Welcome To Python

# 14. isspace() :  used to check if a string contains only whitespace characters
# Syntax: string.isspace()
text = "   "
result = text.isspace()
print(result)  # Output: True

# 15. isdecimal() : used to check if a string consists of only decimal characters
# SyntaX: string.isdecimal()
number1 = "12345"
number2 = "12.34"
number3 = 12345
print(number1.isdecimal())  # Output: True
print(number2.isdecimal())  # Output: False
print(number3.isdecimal())  # Output: False

# 16. isdigit() : used to check if a string consists of only digit characters
# Syntax: string.isdigit()
number1 = "12345"
number2 = "12.34"
print(number1.isdigit())  # Output: True
print(number2.isdigit())  # Output: False

# 17.  isnumeric() : used to check if a string consists of only numeric characters
# Syntax: string.isnumeric()
num1 = "12345"
num2 = "12.34"
num3 = "½"
print(num1.isnumeric())  # Output: True
print(num2.isnumeric())  # Output: False
print(num3.isnumeric())  # Output: True

# STRING ACCESS METHODS

# 18: Variable Methods
# Syntax: variable_name[index]
my_string = "Hello, World!"
print(my_string[0])  # Output: 'H'
print(my_string[7])  # Output: 'W'

my_string = "Hello, World!"
print(my_string[-1])  # Output: '!'
print(my_string[-6])  # Output: 'W'

# 19. Slice Method
# Syntax: variable_name[start_index:end_index]
my_string = "Hello, World!"
print(my_string[7:12])  # Output: 'World'

# 20. Loop Method
# Syntax: for variable in string:
    # Code block
my_string = "Hello"
for char in my_string:
    print(char)  # Output: 'H', 'e', 'l', 'l', 'o'
    
# 21. isalpha()  : checks whether all characters in a string are alphabetic, meaning they are letters from the alphabet
# Syntax: string.isalpha()
text = "Hello"
print(text.isalpha())  # True

# 22. isalnum() :  checks whether all characters in a string are alphanumeric, meaning they are either letters from the alphabet or digits
# Syntax: string.isalnum()
text = "Hello123"
print(text.isalnum())  # True

# String Formatting Methods in Python
# 1. Formatting with % Operator (Old)
# Explanation: This is the oldest method of string formatting in Python, using the % operator.
# The %s placeholder is used for strings, %d for integers, %f for floats, and %b for binary format.
# Syntax: print("%s %s" % (string_variable, integer_variable))
# Example:
name = "John"
age = 25
print("My name is %s and my age is %d." % (name, age))

# 2. Formatting with format() method (New)
# Explanation: The format() method is introduced in Python 3 as a more versatile way to format strings.
# Curly braces {} are used as placeholders, and the variables are passed as arguments to the format() method.
# Syntax: print("{} {} {}".format(variable1, variable2, variable3))
# Example:
name = "Alice"
age = 30
city = "New York"
print("My name is {} and I am {} years old. I live in {}.".format(name, age, city))

# 3. Formatting with f-strings
# Explanation: f-strings are introduced in Python 3.6+ and provide a concise and convenient way to format strings.
# The variables are enclosed in curly braces {} preceded by the 'f' prefix.
# Syntax: print(f"Hi, I am {variable} and my age is {expression}")
# Example:
name = "Bob"
age = 35
print(f"Hi, I am {name} and my age is {age}")
# 4. Formatting with String Template Class
# Explanation: The String Template class provides another way to format strings using placeholders.
# Placeholders are represented by dollar signs $ and variables are passed using the substitute() method.
# Syntax:
from string import Template
template = Template("$variable1 $variable2")
result = template.substitute(variable1="Hello", variable2="World")
print(result)
# Example:
from string import Template
name = "Sarah"
age = 28
template = Template("My name is $name and my age is $age.")
result = template.substitute(name=name, age=age)
print(result)
