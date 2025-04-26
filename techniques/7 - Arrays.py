'''
This file covers
  * Arrays (Lists in python)
  * adding data
  * changing data
  * length
'''

# In python arrays do not exist so we use lists. Unlike arrays lists are 
# dynamic meaning that the length can change as needed

# The program below describes a shopping list.

shopping_list = ["bread", "eggs", "milk", "soup", "fruit", "veg"]

# We can check the length of the array using the len() function

print(len(shopping_list)) # 6

# To print a specific item we use an index. The index is the position
# The first position is position 0

print(shopping_list[2]) # prints milk

# To change data we reassign one of the positions

shopping_list[0] = "cake" # changes bread to cake

# To add an item to the list we use .append()

shopping_list.append("ice cream")

# You can also use a for loop to print all of the items

for index in range(0, len(shopping_list)):
	print(shopping_list[index])
