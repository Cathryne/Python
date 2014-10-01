# Exercise 21: Functions Can Return Something
# http://learnpythonthehardway.org/book/ex21.html

def add(a, b):
	"""Adds 2 variables."""
	print "ADDING %d + %d" % (a, b)
	return a + b	# function call receives the value stated here 

def subtract(a, b):
	"""Subtracts 2 variables."""
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	"""Multiplies 2 variables."""
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	"""Divides 2 variables."""
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

# variable definitions based on return values from functions
# functions calls pass values into function; return statement passes values out again
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit
print "Here's a puzzle."

# nested function calls are executed inside out
# Study Drills 2 & 3: unwrap function calls to formula with variables
what1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = 30 + 5 + (78 - 4 - (90 * 2 * (100 / 2 / 2)))

print "The function-based formula says:", what1
print "The hand-made formula says:", what2
