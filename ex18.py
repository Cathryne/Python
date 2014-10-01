# Exercise 18: Names, Variables, Code, Functions
# http://learnpythonthehardway.org/book/ex18.html

# function definition with argument unpacking like with argv 
def print_two(*args):
	"""Takes two arguments, unpacks and prints them."""
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	"""Takes two arguments and prints them without unpacking"""
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	"""Takes just one argument."""
	print "arg1: %r" % arg1

def print_none():
	"""Takes no arguments."""
	print "I got nothin'."

# function calls with arguments (in number and order as defined above)
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
