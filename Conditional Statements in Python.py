# IF Statement Syntax:
# if condition:
#     block of code to execute if the condition is True

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")

# IF ... ELSE Statement Syntax:
# if condition:
#     Code to execute if the condition is True
# else:
#     Code to execute if the condition is False

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# NESTED IF 
# Syntax:
# if condition1:
#     # code block to execute if condition1 is True
#     
#     if condition2:
#         # code block to execute if both condition1 and condition2 are True
#         
#         if condition3:
#             # code block to execute if condition1, condition2, and condition3 are True
#             pass
#         else:
#             # code block to execute if condition1, condition2 are True, and condition3 is False
#             pass
#     else:
#         # code block to execute if condition1 is True and condition2 is False
#         pass
# else:
#     # code block to execute if condition1 is False
#     pass

num = 30
if num % 2 == 0:
    if num % 3 == 0:
        print("The number is divisible by 2 and 3")
    else:
        print("The number is not divisible by 3")
else:
    print("The number is not divisible by 2")

name = input("Enter your name: ")
print(len(name))

if len(name) == 5 or len(name) < 10:
    if name.startswith('V'):
        print("Your name is: " + name)
    else:
        print("Your name does not start with V")
else:
    print("Your name does not meet the length requirement")

age = int(input("Enter your age: "))
marks = int(input("Enter the marks you scored: "))

if age == 18 or age > 18:
    if 90 < marks < 100:
        print("You passed")
    else:
        print("You did not meet the marks threshold")
else:
    print("You did not meet the age threshold")

# IF ... ELIF .. ELSE Statement
# Syntax:
# if condition1:
#     Code to execute if condition1 is True
# elif condition2:
#     Code to execute if condition1 is False and condition2 is True
# elif condition3:
#     Code to execute if condition1 and condition2 are False and condition3 is True
# else:
#     Code to execute if all conditions are False

marks = int(input("Enter your subject score: "))

if marks > 90:
    print("A")
elif marks > 80:
    print("B")
elif marks > 70:
    print("C")
elif marks > 60:
    print("D")
elif marks > 50:
    print("E")
else:
    print("Fail")
