# Class_Train.py: Booking System
This script models a basic railway reservation system using a Train class. 
It stores a train number and provides methods to simulate booking a ticket, checking the train's running status, and generating a random fare between two locations. 
The code demonstrates how an object can maintain state (the train number) while performing various functional tasks.

# Class_calculator.py: Mathematical Operations
This file defines a Calculator class that performs power-related calculations on a number provided during initialization. 
It includes specific methods to calculate the square, cube, and square root of the input value. 
It is a practical example of using instance variables to store data that multiple methods can then process.

# Class_attribute.py: Attribute Priority
This experiment illustrates the difference between class attributes and instance attributes in Python. 
It shows that while a class variable a is defined globally for all instances, assigning a value to C.a creates a separate instance-level attribute. 
The final print statements prove that changing an instance attribute does not modify the original class attribute.

# Class_programmer.py: Employee Records
This script manages employee data for a specific organization using a Programmer class. 
It uses a class attribute to set a universal company name ("Microsoft") while using the __init__ constructor to assign unique names, salaries, and pincodes to individual objects. 
It demonstrates how to instantiate multiple objects from the same class blueprint.

# Greet_user.py: Static Methods
This code extends the previous calculator example by introducing the @staticmethod decorator. 
The Greet method is defined as a static method, meaning it can be called without needing access to the instance data (it doesn't use self). 
This is a key OOP concept used for utility functions that belong to a class's namespace but are independent of its state.

# Class_slf.py: Self Parameter
This practice file demonstrates that the first parameter of a class method (usually named self) is just a naming convention, not a strict keyword. 
By successfully using slf and even harry as the first argument in the __init__ method, the code proves that Python treats the first parameter as the instance reference regardless of its name. 
It highlights the underlying flexibility of Python's method definitions.
