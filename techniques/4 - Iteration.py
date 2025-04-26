'''
This file covers
  * Iteration
  * For Loops
  * While Loops
'''

# Iteration is one of the three fundamentals of programming
# Iteration is used to repeat a block of code multiple times
# there are 3 types of loop you need to study for your exam
# For Loops, While Loops, and Do-until loops

# For loops are count controlled, they are great if you know
# how many times your code needs to repeat.

# The following code shows a counter for counting up to 10

for number in range(1, 11):
  print("This is number", number)

# The variable number is the counter that we will use.
# range() is a function that counts from a starting number 
# up to a, but not including, given number. The code is
# then indented to show it belongs to the loop

for number in range(1, 11, 2):
  print(number)

# The above code does the exact same however it only counts 
# up in twos. This is using an extra argument in the range
# function called a stepper

# WHILE loops are condition controlled and need to have a
# counter declared outside of the loop. These are perfect
# if you don't know how many times your code needs to repeat

current = 10
while current > 0:
  print(current)
  current = current - 1 # also can be current -= 1
print("Lift off!")

# This code is a rocket countdown. You can see that we have made a
# counter called current, the loop repeats WHILE current is greater than
# 0. After we have printed the number we decrease current by 1. If we
# don't then the loop would be infinate.

# Do-while or do-until loops are not available in python
