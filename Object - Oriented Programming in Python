# OOP in Python
# OOP (Object-Oriented Programming) is a programming paradigm that treats everything as objects.
# In OOP, objects have attributes (data) and methods (functions).
# There are four main components of OOP:
# 1. Abstraction: The process of hiding complex implementation details and providing a simplified interface.
# 2. Encapsulation: The bundling of data and methods within a class, hiding the internal details from the outside.
# 3. Inheritance: The ability of a class to inherit attributes and methods from its parent class.
# 4. Polymorphism: The concept of using a single interface to represent different types of objects.

# Class: A blueprint for creating objects.
# A class is a collection of data members (attributes) and member functions (methods).
# The class name is a user-defined identifier.
# Class Syntax:
# class ClassName:
#     # Your code here
#     pass
# The class name should follow valid identifier naming conventions.

# Object: An instance of a class.
# An object is an abstract data type created from a class.
# An object contains attributes (data) and behavior (methods).
# Once a class is defined, you can create one or more objects of that class.
# Using objects, developers can access attributes and methods defined in the class.

# Creating a Class and Object:
# class ClassName:
#     # Your code here
#     pass
# Create an object of the class:
# object_name = ClassName()

# Example:
# Create a class named "Person" with attributes and a method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
# Create an object of the class "Person".
person1 = Person("Alice", 25)
# Access the attributes and call the method of the object.
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25
person1.introduce()  # Output: Hello, my name is Alice and I am 25 years old.

# Example 1:
# Define a class named Calculation
class Calculation:
    # Initialize class variables
    a = None
    b = None
    # Define a method to get data from the user
    def getData(self):
        self.a = int(input("Enter a number: "))  # Prompt the user to enter a number and assign it to variable 'a'
        self.b = int(input("Enter b value: "))  # Prompt the user to enter a value for 'b' and assign it to variable 'b'
    # Define a method to show the calculation results
    def showResult(self):
        # Perform addition and store the result in the 'addition' variable
        addition = self.a + self.b
        # Perform multiplication and store the result in the 'multiplication' variable
        multiplication = self.a * self.b
        # Perform division and store the result in the 'division' variable
        division = self.a / self.b
        # Perform subtraction and store the result in the 'subtraction' variable
        subtraction = self.a - self.b
        # Perform modulus and store the result in the 'modulus' variable
        modulus = self.a % self.b

        # Print the result of addition
        print("Addition: " + str(addition))
        # Print the result of multiplication
        print("Multiplication: " + str(multiplication))
        # Print the result of division
        print("Division: " + str(division))
        # Print the result of subtraction
        print("Subtraction: " + str(subtraction))
        # Print the result of modulus
        print("Modulus: " + str(modulus))
# Create an object of the Calculation class
obj = Calculation()
# Get data from the user
obj.getData()
# Display the results
obj.showResult()

# Example 2:
# Define a class named Max
class Max:
    # Initialize class variables
    max_num = None
    lst = None
    # Define a method to create a list of numbers
    def create_list(self):
        self.lst = []  # Initialize an empty list
        for i in range(5):
            num = int(input("Enter a number: "))  # Prompt the user to enter a number
            self.lst.append(num)  # Add the entered number to the list
    # Define a method to find the maximum number in the list
    def findMax(self):
        self.max_num = max(self.lst)  # Find the maximum number in the list using the max() function    
    # Define a method to display the maximum number
    def showMax(self):
        print("The Max num is: " + str(self.max_num))  # Print the maximum number
# Create an object of the Max class
obj = Max()
# Call the create_list() method to create a list of numbers
obj.create_list()
# Call the findMax() method to find the maximum number in the list
obj.findMax()
# Call the showMax() method to display the maximum number
obj.showMax()

# Membership in Python OOP
# A class is a collection of data members and functions
# Data members are variables that represent attributes or properties of an object
# Example:
class Person:
    name = "John"  # Data member

    def get_name(self):  # Member function
        return self.name
# In the above example, the class 'Person' has a data member 'name' which represents the name of a person.
# The class also has a member function 'get_name' which returns the value of the 'name' data member.
# Member functions are normal functions defined within a class using the 'def' keyword

# Example:
class Circle:
    radius = 5  # Data member
    def calculate_area(self):  # Member function
        return 3.14 * self.radius ** 2
# In the above example, the class 'Circle' has a data member 'radius' which represents the radius of the circle.
# The class also has a member function 'calculate_area' which calculates the area of the circle based on the radius.

# Modifier for member functions and data members:
# In OOP, we can use different modifiers for member functions and data members, such as public, private, and protected.

# Public modifier:
# Public members are accessible from anywhere within the program.
# They can be accessed using the object of the class or through inheritance.

# Example:
class Rectangle:
    width = 10  # Public data member

    def calculate_area(self):  # Public member function
        return self.width * self.length

# In the above example, the class 'Rectangle' has a public data member 'width' and a public member function 'calculate_area'.
# These can be accessed using an object of the class or through inheritance.

# Private modifier:
# Private members are only accessible within the class itself.
# They are denoted by prefixing the member name with a double underscore (__).

# Example:
class BankAccount:
    __balance = 1000  # Private data member

    def __withdraw(self, amount):  # Private member function
        if amount <= self.__balance:
            self.__balance -= amount

# In the above example, the class 'BankAccount' has a private data member '__balance' and a private member function '__withdraw'.
# These can only be accessed within the class itself.

# Protected modifier:
# Protected members are accessible within the class itself and its subclasses.
# They are denoted by prefixing the member name with a single underscore (_).

# Example:
class Vehicle:
    _speed = 60  # Protected data member

    def _drive(self):  # Protected member function
        print("Driving at", self._speed, "km/h")

# In the above example, the class 'Vehicle' has a protected data member '_speed' and a protected member function '_drive'.
# These can be accessed within the class itself and its subclasses.

# Note: Python doesn't enforce strict access control like some other languages, so these modifiers are conventions rather than strict rules.
# Example:
class Marks:
    math = None
    eng = None
    cs = None
    total = None
    avg = None

    def getStudentMarks(self):
        # Prompt the user to enter marks for each subject
        self.math = int(input("Enter Math subject Marks: "))
        self.eng = int(input("Enter English subject Marks: "))
        self.cs = int(input("Enter Computer Science Marks: "))

    def show_total_marks(self):
        # Calculate the total marks by summing up the marks of all subjects
        self.total = self.cs + self.eng + self.math
        # Display the total marks
        print("Total: " + str(self.total))
        # Calculate the average marks by dividing the total marks by the number of subjects (3 in this case)
        self.avg = self.total / 3
        # Display the average marks
        print("Average: " + str(self.avg))

# Create an object of the Marks class
obj = Marks()
# Call the getStudentMarks method to input the marks
obj.getStudentMarks()
# Call the show_total_marks method to calculate and display the total and average marks
obj.show_total_marks()

# Example:
class Student:
    # Define class attributes for studentID, studentName, and marks
    studentID = 5678
    studentName = "Faisal Zamir"
    marks = 64738

    def show(self):
        # Display the student ID
        print("Student ID: " + str(self.studentID))
        # Display the student name
        print("Student Name: " + str(self.studentName))
        # Display the student marks
        print("Student Marks: " + str(self.marks))

# Create an object of the Student class
obj = Student()
# Call the show method to display the student details
obj.show()

# Membership in Python OOP

# A class is a blueprint for creating objects. It is a collection of data members (variables) and member functions (methods).
# The data members represent the attributes or properties of an object.

# Example: Defining a class called 'Person' with data members 'name' and 'age'
class Person:
    # Data members
    name = ""
    age = 0

    # Member function
    def display_info(self):
        # Accessing the data members within the member function
        print("Name: " + self.name)
        print("Age: " + str(self.age))

# Creating an object of the 'Person' class
person1 = Person()
# Assigning values to the data members of the object
person1.name = "John"
person1.age = 25
# Calling the member function to display the information
person1.display_info()

# Member functions are normal functions defined within a class.
# They are typically prefixed with the 'def' keyword and operate on the data members of the class.

# Example: Defining a class called 'Calculator' with a member function 'add' to perform addition
class Calculator:
    def add(self, num1, num2):
        # Performing addition using the given parameters
        result = num1 + num2
        # Returning the result
        return result

# Creating an object of the 'Calculator' class
calculator = Calculator()
# Calling the 'add' member function and printing the result
print("Sum: " + str(calculator.add(5, 3)))

# In Python, we can use different modifiers with member functions and data members.
# The three common modifiers are public, private, and protected.

# Public members are accessible from anywhere outside the class.
# Private members are only accessible within the class itself.
# Protected members are accessible within the class and its subclasses.

# Example: Defining a class called 'Person' with public and private data members
class Person:
    # Public data member
    name = ""

    def __init__(self):
        # Private data member
        self.__age = 0

    def display_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.__age))

# Creating an object of the 'Person' class
person2 = Person()
# Accessing the public data member
person2.name = "Alice"
# Accessing the private data member through the member function
person2.display_info()
# Note: To access private members outside the class, we can define getter and setter methods.

# Public: Python Access Modifier

# Python Access Modifier
# Access modifiers are used in Python OOP to control the visibility and accessibility of attributes and methods.
# There are different types of modifiers used in Python OOP.

# The purpose of using modifiers is to define the level of accessibility for data and methods:
# - Public: Provides unrestricted access from anywhere in the program (inside class, outside class, child class).
# - Protected: Provides access from the base class and its child classes in the program. It is denoted by a single underscore (_).
# - Private: Provides access only from the base class in which it is declared. It is denoted by a double underscore (__).

# Public Access Modifier:
# When we declare attributes or methods with the public modifier, it means they can be accessed from anywhere in the program.

# Example: Defining a class called 'Person' with public attributes and methods
class Person:
    # Public attribute
    name = ""

    # Public method
    def display_info(self):
        print("Name: " + self.name)

# Creating an object of the 'Person' class
person = Person()
# Accessing the public attribute
person.name = "John"
# Calling the public method to display the information
person.display_info()

# Public attributes and methods can be accessed both inside and outside the class, as well as in child classes.

# Protected Access Modifier:
# When we declare attributes or methods with the protected modifier, it means they can be accessed from the base class and its child classes.

# Example: Defining a class called 'Vehicle' with a protected attribute and method
class Vehicle:
    # Protected attribute
    _fuel_type = ""

    # Protected method
    def _start_engine(self):
        print("Engine started")

# Creating an object of the 'Vehicle' class
vehicle = Vehicle()
# Accessing the protected attribute
vehicle._fuel_type = "Gasoline"
# Calling the protected method to start the engine
vehicle._start_engine()

# Protected attributes and methods can be accessed within the class and its subclasses.

# Private Access Modifier:
# When we declare attributes or methods with the private modifier, it means they can only be accessed from the base class in which they are declared.

# Example: Defining a class called 'Employee' with a private attribute and method
class Employee:
    # Private attribute
    __salary = 0

    # Private method
    def __calculate_bonus(self):
        print("Bonus calculated")

# Creating an object of the 'Employee' class
employee = Employee()
# Accessing the private attribute is not possible outside the class

# Note: Although private attributes and methods cannot be directly accessed outside the class,
# Python provides name mangling to access them indirectly within the class.

# Private Access Modifier:

# Private access modifier restricts the accessibility of attributes and methods to only the base class in which they are declared.

# Example: Defining a class called 'Person' with private attribute and method
class Person:
    # Private attribute
    __name = ""

    # Private method
    def __display_info(self):
        print("Name: " + self.__name)

# Creating an object of the 'Person' class
person = Person()
# Accessing the private attribute is not possible outside the class

# Note: Although private attributes and methods cannot be directly accessed outside the class,
# Python provides name mangling to access them indirectly within the class.

# Example: Accessing private attributes and methods using name mangling within the class
class Person:
    __name = ""

    def __display_info(self):
        print("Name: " + self.__name)

    def update_name(self, new_name):
        self.__name = new_name

    def show_info(self):
        self.__display_info()

# Creating an object of the 'Person' class
person = Person()
# Accessing private attribute and method using name mangling
person._Person__name = "John"  # Name mangling
person._Person__display_info()  # Name mangling
person.update_name("Jane")  # Accessing through a public method
person.show_info()  # Accessing through a public method

# Private attributes and methods can only be accessed within the class in which they are declared.
# However, Python provides name mangling to indirectly access them within the class using the syntax _ClassName__private_attribute/method.

# Inheritance in Python OOP:

# Inheritance is the process of creating a class (child class) from an existing class (parent class).
# The child class inherits all the attributes and methods of the parent class, allowing for code reuse and extension.

# Parent Class:
# The parent class, also known as the base class, is the class from which a new class can be created.
# It serves as the blueprint for the child class, providing the attributes and methods that can be inherited.

# Child Class:
# The child class, also known as the derived class, is the class that inherits all the properties and methods
# from the parent class. It extends the functionality of the parent class by adding new attributes and methods
# or by overriding the existing ones.

# Example: Creating a parent class called 'Animal' and a child class called 'Dog'
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog barks.")

# Creating an object of the child class 'Dog'
dog = Dog("Buddy", "Labrador")
print(dog.name)  # Accessing attribute inherited from parent class
dog.speak()  # Overriding the speak() method of the parent class

# In the above example, the 'Animal' class serves as the parent class, and the 'Dog' class is the child class.
# The 'Dog' class inherits the 'name' attribute and the 'speak()' method from the 'Animal' class.
# It also defines its own attribute 'breed' and overrides the 'speak()' method with its own implementation.

# With inheritance, we can reuse and extend existing classes, promoting code reusability and modularity.


# Constructor in Python OOP:

# A constructor is a special method that is automatically called when an object of a class is created.
# It initializes the object's attributes and performs any necessary setup.
# In Python, the constructor method is defined as '__init__(self)', and it can take parameters if needed.

# Non-Parameterized Constructor:
# A non-parameterized constructor is a constructor that does not take any parameters.
# It is used to perform default initialization of the object's attributes.

# Parameterized Constructor:
# A parameterized constructor is a constructor that takes one or more parameters.
# It allows customization of object initialization by passing values to the constructor.

# Default Constructor:
# The default constructor is a constructor that is automatically created when a class does not have any explicitly defined constructors.
# It initializes the object's attributes with default values or performs default setup.

# Destructor in Python OOP:
# A destructor is a special method that is called when an object is destroyed or when the program ends.
# It is used to perform any necessary cleanup operations before the object is removed from memory.
# In Python, the destructor method is defined as '__del__(self)'.

# Example: Creating a class called 'Person' with a constructor and destructor
class Person:
    def __init__(self, name):
        self.name = name
        print("Constructor called. Object created.")

    def __del__(self):
        print("Destructor called. Object destroyed.")

    def display_name(self):
        print("Name:", self.name)

# Creating an object of the class 'Person'
person = Person("John")  # Constructor is called automatically

person.display_name()

del person  # Destructor is called when the object is destroyed or when the program ends

# In the above example, the class 'Person' has a constructor '__init__(self, name)' that takes a 'name' parameter.
# The constructor initializes the 'name' attribute of the object.
# The class also has a destructor '__del__(self)' that is called when the object is destroyed or when the program ends.
# The 'display_name()' method is used to display the name attribute of the object.
# The constructor is automatically called when the object is created, and the destructor is called when the object is destroyed or when the program ends.
# Constructors and destructors are useful for initializing objects and performing cleanup operations, respectively.


# Example 1:
# Define the Test01 class
class Test01:
    # Class attributes
    name = "John"
    age = 19
    contact = "+44 7911 123456"
    # Method to show information
    def showInfo(self):
        print(self.age)
        print("Parent Class")
# Define the Test02 class that inherits from Test01
class Test02(Test01):
    # Class attribute
    city = "London"
    # Method to display information
    def disInfo(self):
        print("Child Class")
# Create an instance of Test02 class
obj = Test02()
# Call the showInfo method from the parent class
obj.showInfo()
# Call the disInfo method from the child class
obj.disInfo()

# Example 2:
# Define the CircleArea class
class CircleArea:
    # Class attribute
    radius = None
    # Method to get the radius from the user
    def getRadius(self):
        self.radius = float(input("Enter the radius: "))
# Define the FindArea class that inherits from CircleArea
class FindArea(CircleArea):
    # Method to calculate and display the area of the circle
    def showArea(self):
        # Calculate the area using the formula: area = pi * radius^2
        self.circle_area = 3.1415 * self.radius * self.radius
        print("The area of the circle is:", self.circle_area)
# Create an instance of the FindArea class
obj = FindArea()
# Call the getRadius method to input the radius from the user
obj.getRadius()
# Call the showArea method to calculate and display the area of the circle
obj.showArea()

# Example 3:
# Define the Test1 class
class Test1:
    # Constructor to initialize the class with two values
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
    # Method to get additional values from user
    def getValues(self):
        self.num1 = int(input("Enter a value: "))
        self.num2 = int(input("Enter b value: "))
    # Method to perform arithmetic operation and display the result
    def showArithmetic(self):
        print("Addition: " + str(self.num1 + self.num2))
    # Destructor method
    def __del__(self):
        print("This is a destructor")
# Get input values from the user
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
# Create an object of Test1 class with the input values
obj = Test1(a, b)
# Call the showArithmetic method to perform the addition operation and display the result
obj.showArithmetic()
