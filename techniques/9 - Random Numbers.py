'''
This file covers
  * Random number generation
'''

# Random numbers can be generated easily in python. You need to import
# the random library first, then you can call the randint function to
# generate a number

# The following program generates 6 random numbers between 1 and 52 
# for people to use as lucky numbers

import random

lucky_numbers = []

while len(lucky_numbers) < 6:
	generated_num = random.randint(1, 52)
	if generated_num in lucky_numbers:
		continue
	lucky_numbers.append(generated_num)

print(lucky_numbers)

# Line 13 imports the random library. Line 15 starts an empty list.
# A condition controlled loop is used to keep generating numbers until 
# 6 numbers are in the list.

# Line 18 generates the number between 1 and 52. Line 19-20 make sure 
# that only unique numbers are in the list. Line 21 adds the number to 
# the list
