'''
This file covers
  * File Handling
  * Opening / closing
  * writing
  * appending
  * reading
'''

# File handling allows you to create and manipulate files within 
# your python file. To get started you have to open a file, you can 
# then manipulate your file and then close it to save changes

file = open("my_file.txt", "w")

# The above code opens a file called my_file.txt in write mode. If 
# the file doesn't exist then it is created. If the file exists then
# the contents is deleted so you can write data.

# \n puts the cursor onto the next line of the text file

file.write("Hi There, I'm Python\n") # Writes the string to the file
file.close() # Closes the file (saves changes)

# To read a file you open it using "r" where the "w" is. You can then 
# read through the file.

file = open("my_file.txt", "r")

for line in file:
	print(line)
	
file.close()

# The for loop reads through the file however you could also manipulate
# the lines seperatly this way.

# By appending a file you open it in a mode where you can write lines
# and they are added to the end of the file

file = open("my_file.txt", "a")

file.write("Hi Python, how are you?\n")

file.close()

# Run this file to see it in action. You will find the text file in 
# the same location as this file in your file system. 
