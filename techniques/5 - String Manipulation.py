'''
This file covers
  * String manipulation
  * Changing case
  * Slicing Strings
'''

# String manipulation is used to extract or change strings in certain
# ways so that data can be extracted.

# We are going to use the string Computer Science

my_string = "Computer Science"

print(my_string.upper()) # COMPUTER SCIENCE
print(my_string.lower()) # computer science
print(len(my_string)) # 16

# We can also extract information using string slicing/sub-strings

print(my_string[:8]) # Computer (equivilent to .left())
print(my_string[9:]) # Science (equivilent to .right())
print(my_string[9:12]) # Sci (equivilent to .substring())

# String slicing in python can be complicated however you declare 
# the position of the letter you are starting from (first letter is 0)
# followed by a colon then the position of the letter you are ending 
# at (the position specified is not included)
