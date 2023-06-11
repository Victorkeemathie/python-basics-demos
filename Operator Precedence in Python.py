# In math, we follow the rule of BODMAS to learn the order of operators.
# In Python, we use the rule of PEMDAS to check operator precedence.
# PEMDAS stands for Parentheses, Exponents, Multiplication, Division, Addition, Subtraction.

# Example: Evaluating an equation
# We'll calculate the value of x using the given formula: x = (a - d) + (d ** f) / (b + c) + (e * f)

# Prompting the user for input
a = int(input("Enter the value of the first number: "))
b = int(input("Enter the value of the second number: "))
c = int(input("Enter the value of the third number: "))
d = int(input("Enter the value of the fourth number: "))
e = int(input("Enter the value of the fifth number: "))
f = int(input("Enter the value of the sixth number: "))

# Evaluating the equation
x = (a - d) + (d ** f) / (b + c) + (e * f)

# Displaying the result
print(f"The result of x is: {x}")
