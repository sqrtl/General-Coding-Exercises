from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

# Assigning the variable of "target" to open the file specified in the script arguments.
target = open(filename, 'a+')

# Truncating it is a method, but a but redundant and pointless... Maybe learn this later to see what the hell is going on.
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

# ========== Writing to the target file in multilple lines ===============
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# ================= Condensing the write statments to one line ===============

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
# print(len(line1 + "\n" + line2 + "\n" + line3 + "\n"))
# print(len("\n"))
target.close()