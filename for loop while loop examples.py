# Program 1: Generating a list of odd numbers in descending order
odd_numbers = []
for num in range(49, 0, -2):
    odd_numbers.append(num)
   
# Calculating the sum of odd numbers
sum_odd_numbers = sum(odd_numbers)

# Printing the list of odd numbers and their sum
print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", sum_odd_numbers)

# Program 2: Printing odd numbers in descending order using a while loop
i = 100
while i >= 0:
    if i % 2 != 0:
        print(i)
    i -= 1

# Program 3: Generating a list of numbers from 10 to 50
lst = []
n = 10
while n <= 50:
    lst.append(n)
    n += 1

# Printing the list of numbers and calculating their sum
print("Numbers:", lst)
sum_all = sum(lst)
print("Sum of Numbers:", sum_all)

# Program 4: Printing a sequence of numbers based on user input
num1 = int(input("Enter the starting number of the sequence: "))
num2 = int(input("Enter the ending number of the sequence: "))

# Printing numbers from the starting number to the ending number
if num1 <= num2:
    i = num1
    while i <= num2:
        print(i)
        i += 1
else:
    print("The ending number of the sequence is less than the starting number.")

# Program 5: Printing the multiplication table of a number
num = int(input("Enter a number to get its multiplication table: "))

i = 1
while i <= 10:
    print(str(num) + " * " + str(i) + " = " + str(num * i))
    i += 1
