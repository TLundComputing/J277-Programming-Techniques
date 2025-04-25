'''
  This file covers:
  * Sequencing
  * Data Types
  * Casting
'''

# Sequencing is one of the three constructs of programming.
# It means the code is ran in the order that it is typed. It is
# important for your code to written in the correct order otherwise
# You will get different results to what you expect.

# This file is a calculator, it takes in two numbers and adds them
# together

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
answer = num1 + num2
print(num1, "+", num2, "=", answer)

# If you run this code with the numbers 5 and 2 as inputs, you should
# get the answer 52. This is incorrect however to Python it is correct.

# This is because an input always reads data in as a string, adding two
# strings together is concatination which adds one string to another,
# making a longer string.

# We can force num1 and num2 to be integers (Whole numbers).
# Modify lines 16 and 17 so they read something like this and try
# running the code again.
num1 = int(input("Enter a number: "))
