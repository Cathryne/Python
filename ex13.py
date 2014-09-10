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