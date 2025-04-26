'''
This file covers
  * Functions
  * Procedures
'''

# Subprograms are fantastic for reusable code. It also makes code
# more readable.

# Functions return a value to be used in the main program. Procedures
# don't return a value (great for menus or tiles)

# The program below greets a user

def greeting_procedure():
	print("Hello")

def greeting_function():
	return "Hello"
	
greeting_procedure() # Calls the procedure
# Calls the function and uses the result to make the string longer
print(greeting_function(), "World") 

# Making functions and procedures uses the def keyword. The only tell
# tale sign of a function or procedure is the return keyword. 
