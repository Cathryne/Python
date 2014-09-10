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
	print "Your 1st variable is the number:", first, type(first) 
except ValueError:
	print "Your 1st variable is not a number, but:", type(first) 
	
try:	
	second = float(second)
	print "Your 2nd variable is the number:", second, type(second)
except ValueError:
	print "Your 2nd variable is not a number, but:", type(second)
	
try:
	third = float(third)
	print "Your 3rd variable is the number:", third, type(third)
except ValueError:
	print "Your 3rd variable is not a number, but:", type(third)

# Can these try statements be condensed?
# try:
# 	first = float(first)
# 	print "Your 1st variable is the number:", first
# 	second = float(second)
# 	print "Your 2nd variable is the number:", second
# 	third = float(third)
# 	print "Your 3rd variable is the number:", third
# 	# no, check all checks after 1st failed one fail as well and all exception commands are executed
# 	# or this?
# 	first = float(first)
# 	second = float(second)
# 	third = float(third)
# 	print "Your 1st variable is the number:", first
# 	print "Your 2nd variable is the number:", second
# 	print "Your 3rd variable is the number:", third
#	# no, all checks fail and all exception commands are executed
# except ValueError:
# 	print "Your 1st variable is not a number."
# 	print "Your 2nd variable is not a number."
# 	print "Your 3rd variable is not a number."
