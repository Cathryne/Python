# Exercise 21: Functions Can Return Something
# http://learnpythonthehardway.org/book/ex21.html
# Study Drill 4: implement known formula via function that returns a value

from math import sqrt

def pythagoras(x, y):
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
