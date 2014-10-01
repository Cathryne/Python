# Exercise 20: Functions and Files
# http://learnpythonthehardway.org/book/ex20.html

# imports dynamic object "argv" from module "sys" => enables command line arguments
from sys import argv

# unpacks command line arguments
script, input_file = argv

def print_all(f):
	"""Takes opened file object and prints it entirely"""
	print f.read()

# function that 
def rewind(f):
	"""Takes opened file object  moves (back) to byte 0 in file."""
	f.seek(0)

# function that prints numbered lines from file 
# CSQ: How does readline() know where each line is?
# 	It doesn't. Instead, position in the file is returned, so file opbject "f" retains that for next function call. "current_line" and "line_count" are only for printing the incrementing numbers, not for specifying the actual line in the file.
def print_a_line(line_count, f):
	"""
	Takes previously calculated line count and prints it together
	with content of line that way determined by readline()'s return.
	"""
	print line_count, f.readline()

# creates file object by opening the file provided via command line argument
current_file = open(input_file)

# calls function to read and print entire file
print "First, let's print the whole file:\n"
print_all(current_file)

# falls function to move back to position 0 in file
print "Now, let's rewind it like a tape."
rewind(current_file)

# increments line number & calls function to print only that line repeatedly
# Study Drill 5 / CSQ: What is +=?
#	"Contractiong" = short-hand notation for incrementation: a = a + 1
print "Let's print three lines:"
current_line = 1	# = 1
print_a_line(current_line, current_file)
current_line += 1	# = 2
print_a_line(current_line, current_file)
current_line += 1	# = 3
print_a_line(current_line, current_file)
# CSQ: because readline()'s return include "\n" from line end in file, output has empty lines
