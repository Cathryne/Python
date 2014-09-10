# Exercise 13: Parameters, Unpacking, Variables
# http://learnpythonthehardway.org/book/ex13.html

# import adds Python modules to a script
# argv = variable that takes arguments that are passed along with the script execution command
from sys import argv

# unpacks values from argv into variables in the given order
script, first, second, third = argv

# Displays variables
print "The script is called:", script 
print "Your 1st variable is:", first 
print "Your 2nd variable is:", second
print "Your 3rd variable is:", third


# Common Student Question: Are the command line arguments strings?

print "Any numbers here?"
print type(first)
print type(second)
print type(third)
# type() returns type of variable; will always be 'str' for command arguments

print "I guess not. Yet."
print "Processing... Done!"

# exception handling for "ValueError: could not convert string to float"
try:
	first = float(first)
	print "Your 1st variable is the number:", first
except ValueError:
	print "Your 1st variable is not a number."
	
try:	
	second = float(second)
	print "Your 2nd variable is the number:", second
except ValueError:
	print "Your 2nd variable is not a number."
	
try:
	third = float(third)
	print "Your 3rd variable is the number:", third
except ValueError:
	print "Your 3rd variable is not a number."