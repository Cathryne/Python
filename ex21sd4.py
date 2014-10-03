# Exercise 21: Functions Can Return Something
# http://learnpythonthehardway.org/book/ex21.html
# Study Drill 4: implement known formula via function that returns a value

from math import sqrt

def pythagoras(x, y):
	"""
	Calculates length of hypotenuse c from given lengths of
	legs a and b.
	"""
	print "Square-rooting squares of a and b via a function...",
	return round(sqrt(x ** 2 + y ** 2), 3)

print "Now, let's do the Pythagoras!"
a = float(raw_input("a = "))
b = float(raw_input("b = "))

print "So, those squared make: %d and %d" % (a ** 2, b ** 2)
print "Thus, c squared is: %d" % (a ** 2 + b ** 2)
print "And c itself must be: %r" % round(sqrt(a ** 2 + b ** 2), 3)
print pythagoras(a, b)

c = int(raw_input("Again, with the above valules multiplied by: "))
print pythagoras(a * c, b * c)



def fibonacci(a, b):
	c = a + b
	# using only one calculation here & overwriting either initial variable with result
	# yields linearly increasing sequence, because 2nd initial variable remains static
	# second helper variable is necessary so that results are generated in pairs
	d = b + c
	print c
	print d
	return (c, d)

print "\n\nAnd now another math genius' tinkering! Let's do a Fibonacci sequence."
print "I'll need to numbers from you:"
a = int(raw_input("a = "))
b = int(raw_input("b = "))
limit = int(raw_input("And I'll need an upper limit. Can't be doing this all day! "))

print "OK, the sequence is based on %d and %d up to %d is:" % (a, b, limit)

c = a + b
while c < limit:
	 a, b = fibonacci(a, b)
	 # self-assigning necessary to pass next pair into sequence
	 c = a + b

# more elegant solutions
# https://github.com/nunayerBeezwax/fibonacci_python/blob/master/fibonacci.py
# https://github.com/yamogi/Python_Fibonacci/blob/master/fib.py
# https://github.com/DeanThomas1983/fibonacci/blob/master/fibonacci/src/fibonacci.py
