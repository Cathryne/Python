# Exercise 21: Functions Can Return Something
# http://learnpythonthehardway.org/book/ex21.html
# Study Drill 1: Practice returning of values with other functions

def add(a, b, c):
	"""Adds 3 variables."""
	print "Adding %d, %d & %d... " % (a, b, c)
	return a + b + c

print "Let's do an addition of 3 values. Please tell me which:"
a = int(raw_input("a = "))
b = int(raw_input("b = "))
c = int(raw_input("c = "))

d = add(a, b, c)
print "That makes: %d" % d
