'''
  This file covers the following:
  * outputs
  * variables
  * constants
  * inputs
'''

# To output data we use the print function
print("Hello World")

# A variable is named memory location where the value being held can
# be changed while the program is running. We declare a variable by
# typing the name of the identifier followed by an equals and then the
# value.
name = "TLundComputing" # This variable holds a string
year = 2025 # This variable holds an integer

# A constant is a named memory location where the value cannot be
# changed while the program is running.
# Python doesn't fully support constants however by convention we can 
# type the name of the identifier in all capitals
PI = 3.14
GRAVITY = 9.8

# You can get input from the user by using the input() function.
# You can store the inputted value in a variable for further
# computations
name = input("What is your name? ")
print("Hello,", name)
