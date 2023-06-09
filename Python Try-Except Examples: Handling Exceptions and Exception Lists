# Try and Except in Python
# Exception is an error event that occurs when executing program statements.
# It disrupts the normal flow of program execution.
# Exception is a runtime error that, when it occurs, prevents further execution of the program.
# Exception Handling: try, except, else, and finally
# try: Used to test a piece of code and check if it raises an error or not.
# except: Used to handle an error by providing a specific code block to execute when an error occurs.
# else: Optional block of code that executes when the try block is error-free.
# finally: Code that is executed regardless of whether an exception occurred or not.

# Syntax:
try:
    # Code to be tested for errors
    # ...
except ExceptionType:
    # Code to handle the specific exception
    # ...
else:
    # Code to be executed when the try block is error-free
    # ...
finally:
    # Code to be executed regardless of exceptions
    # ...

# Example:
try:
    num1 = 10
    num2 = 0
    result = num1 / num2  # Raises a ZeroDivisionError
    print(result)        # This line won't be executed
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division performed successfully.")  # This line won't be executed
finally:
    print("Exception handling is complete.")

# StopIteration

# Explanation: StopIteration is an exception raised to signal the end of an iterator.
# Syntax: raise StopIteration()
# Example:
class MyIterator:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration()

my_iter = MyIterator()
for item in my_iter:
    print(item)


# Exception List Examples:

# 1. SystemExit
# Explanation: SystemExit is an exception raised to request the termination of the program.
# Syntax: raise SystemExit()
# Example:
try:
    raise SystemExit("Exiting program")
except SystemExit as e:
    print(e)


# 2.  StandardError (Python 2)

# Explanation: StandardError is the base class for all built-in exceptions except StopIteration and SystemExit (Python 2 only).
# Syntax: N/A
# Example: N/A

# 3. ArithmeticError

# Explanation: ArithmeticError is the base class for all errors that occur during arithmetic calculations.
# Syntax: raise ArithmeticError("Error message")
# Example:
try:
    result = 10 / 0
except ArithmeticError as e:
    print("Error:", e)

# 4. OverflowError
# Explanation: OverflowError is an exception raised when the result of an arithmetic operation is too large to be expressed within the allowed range.
# Syntax: raise OverflowError("Error message")
# Example:
try:
    result = 2 ** 1000
except OverflowError as e:
    print("Error:", e)

# 5. FloatingPointError (Python 2)
# Explanation: FloatingPointError is an exception raised when a floating-point calculation fails (Python 2 only).
# Syntax: raise FloatingPointError("Error message")
# Example:
try:
    result = 0.1 + 0.2
except FloatingPointError as e:
    print("Error:", e)

# 6. ZeroDivisionError

# Explanation: ZeroDivisionError is an exception raised when division or modulo operation is performed with zero as the divisor.
# Syntax: raise ZeroDivisionError("Error message")
# Example:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# 7. AssertionError
# Explanation: AssertionError is an exception raised when an assert statement fails.
# Syntax: assert condition, "Error message"
# Example:
try:
    x = 5
    assert x < 0, "x should be a negative number"
except AssertionError as e:
    print("Error:", e)

# 8. AttributeError
# Explanation: AttributeError is an exception raised when an attribute reference or assignment fails.
# Syntax: raise AttributeError("Error message")
# Example:
try:
    x = 5
    x.append(10)
except AttributeError as e:
    print("Error:", e)

# 9. EOFError
# Explanation: EOFError is an exception raised when the input() function hits an end-of-file condition (no input received).
# Syntax: N/A
# Example:
try:
    user_input = input("Enter a value: ")
except EOFError:
    print("End of input reached.")

# 10. ImportError
# Explanation: ImportError is an exception raised when a module or name cannot be imported.
# Syntax: raise ImportError("Error message")
# Example:
try:
    import non_existent_module
except ImportError as e:
    print("Error:", e)
    
# 11. KeyboardInterrupt
# Explanation: KeyboardInterrupt is an exception raised when the user interrupts the execution of a program, usually by pressing Ctrl+C.
# Syntax: N/A
# Example:
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by user.")


# 12. LookupError
# Explanation: LookupError is the base class for all exceptions raised when a key or index is not found in a mapping or sequence.
# Syntax: raise LookupError("Error message")
# Example:
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except LookupError as e:
    print("Error:", e)


# 13. IndexError
# Explanation: IndexError is an exception raised when a sequence subscript is out of range.
# Syntax: raise IndexError("Error message")
# Example:
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Error:", e)


# 14. KeyError
# Explanation: KeyError is an exception raised when a mapping (dictionary) key is not found.
# Syntax: raise KeyError("Error message")
# Example:
try:
    my_dict = {"name": "John", "age": 25}
    print(my_dict["address"])
except KeyError as e:
    print("Error:", e)


# 15. NameError

# Explanation: NameError is an exception raised when a local or global name is not found.
# Syntax: raise NameError("Error message")
# Example:
try:
    print(non_existent_variable)
except NameError as e:
    print("Error:", e)

# 16. UnboundLocalError
# Explanation: UnboundLocalError is an exception raised when a local variable is referenced before it has been assigned a value.
# Syntax: raise UnboundLocalError("Error message")
# Example:
def my_function():
    print(x)  # x is not assigned a value before referencing it
    x = 5
try:
    my_function()
except UnboundLocalError as e:
    print("Error:", e)

# 17. EnvironmentError (Python 2)
# Explanation: EnvironmentError is the base class for all exceptions raised when a system/environment-related error occurs (Python 2 only).
# Syntax: raise EnvironmentError("Error message")
# Example:
try:
    open("non_existent_file.txt")
except EnvironmentError as e:
    print("Error:", e)

# 18. IOError (Python 2)
# Explanation: IOError is an exception raised when an I/O (input/output) operation fails (Python 2 only).
# Syntax: raise IOError("Error message")
# Example:
try:
    file = open("non_existent_file.txt")
except IOError as e:
    print("Error:", e)

# 19. SyntaxError
# Explanation: SyntaxError is an exception raised when there is a syntax error in the code.
# Syntax: N/A
# Example:
try:
    eval("print('Hello, World!'")
except SyntaxError as e:
    print("Error:", e)

# 20. IndentationError
# Explanation: IndentationError is an exception raised when there is an indentation-related error in the code.
# Syntax: N/A
# Example:
try:
    def my_function():
    print("Hello, World!")
except IndentationError as e:
    print("Error:", e)


# 21. SystemError
# Explanation: SystemError is an exception raised when an internal error in the Python interpreter is detected.
# Syntax: raise SystemError("Error message")
# Example:
try:
    raise

# 22. SystemExit
# Explanation: SystemExit is an exception raised when the sys.exit() function is called to exit the program.
# Syntax: raise SystemExit("Error message")
# Example:
try:
    raise SystemExit("Program exit")
except SystemExit as e:
    print("Error:", e)

# 23. TypeError
# Explanation: TypeError is an exception raised when an operation or function is applied to an object of inappropriate type.
# Syntax: raise TypeError("Error message")
# Example:
try:
    x = 5 + "Hello"
except TypeError as e:
    print("Error:", e)


# 24. ValueError
# Explanation: ValueError is an exception raised when a function receives an argument of the correct type but an inappropriate value.
# Syntax: raise ValueError("Error message")
# Example:
try:
    x = int("Hello")
except ValueError as e:
    print("Error:", e)


# 25. RuntimeError
# Explanation: RuntimeError is a generic exception raised when an error occurs that doesn't belong to any other specific category.
# Syntax: raise RuntimeError("Error message")
# Example:
try:
    raise RuntimeError("Something went wrong")
except RuntimeError as e:
    print("Error:", e)

# 26. NotImplementedError
# Explanation: NotImplementedError is an exception raised when an abstract method or function is not implemented in a subclass.
# Syntax: raise NotImplementedError("Error message")
# Example:
class BaseClass:
    def abstract_method(self):
        raise NotImplementedError("Method not implemented")

try:
    obj = BaseClass()
    obj.abstract_method()
except NotImplementedError as e:
    print("Error:", e)

# Example 1:
while True:
    try:
        age = int(input("Enter your age: "))  # Prompt the user to enter their age
        break  # Break out of the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        height = float(input("Enter your height in meters: "))  # Prompt the user to enter their height
        break  # Break out of the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid floating-point number.")

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")  # Raise a ValueError if age is negative
    if height < 0:
        raise ValueError("Height cannot be negative.")  # Raise a ValueError if height is negative
    if height > 3:
        raise ValueError("Height cannot be greater than 3 meters.")  # Raise a ValueError if height is greater than 3
except ValueError as e:
    print("Error:", e)  # Print the error message if a ValueError is raised

try:
    result = age + "10"  # Attempt to concatenate an integer and a string
except TypeError as e:
    print("Error:", e)  # Print the error message if a TypeError is raised
    
    
# Example 2:
my_list = [1, 2, 3]

try:
    # Attempting to access an element at an index that is out of range
    print(my_list[5])  # Raises IndexError
except IndexError:
    print("Index is out of range")  # Prints an error message if IndexError occurs

my_dict = {"name": "John", "age": 25}

try:
    # Attempting to access a non-existent key in the dictionary
    print(my_dict["address"])  # Raises KeyError
except KeyError:
    print("Key does not exist in the dictionary")  # Prints an error message if KeyError occurs

