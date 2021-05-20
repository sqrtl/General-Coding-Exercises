# From the libary sys import the argv part of the libary
from sys import argv

# This script [Script] is going to take the argument [Filename] to run properly.
script, filename = argv

# This stores file in a variable called txt.
txt = open(filename)

# Prints the file's name using the %r to input in raw data
print("Here's your file %r:" % filename)
# Read the txt file, and prints the results of it.
print (txt.read())

# Prompting you to type the filename again and print the result.
print("Type the filename again:")
# Prompt to put the file name again.
file_again = input("> ")

# Open's the text file and stores it in a variable. 
txt_again = open(file_again)

# It's reading the .txt file
print(txt_again.read())