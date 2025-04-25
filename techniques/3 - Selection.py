'''
  This file covers:
  * Selection
'''

# Selection is one of the three programming constructs. It is incharge
# of letting your program branch or change depending on a input.

# The following program checks if someone is an adult or a child.

age = int(input("Enter your age: "))
# The colon means the following indented code belongs to this line
if age >= 18:
  print("You are an adult") # Notice how this line is indented
else:
  print("You are a child") # Nortice how this line is indented

# The above code takes in the users age as an input. If the user is
# 18 or over the program outputs "You are an adult" if the value is
# anything else it prints out "You are a child"

# There are many different boolean operators you can use, these include
# == equal to
# != not equal to
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to

# You can add additional conditions by using elif see how the if
# statement changes

age = int(input("Enter your age: "))
if age >= 18:
  print("You are an adult")
elif age >= 13:
  print("You are an adolecent")
else:
  print("You are a child")
  
# The other type of selection is a switch case. Python does not fully
# support this however they do have a different version called a
# match-case

print("Menu")
print("1 - New File")
print("2 - Open a file")
print("3 - Add to a file")
print("Any Key - Exit")
response = input("> ")
match response: # This is equivilent to switch
  case "1":
    print("Starting a new file")
  case "2":
    print("Opening a file")
  case "3":
    print("Adding to a file")
  case _: # This is the default case e.g. else
    print("Exiting")
