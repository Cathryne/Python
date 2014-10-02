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
	d = b + c
	e = c + d
	f = d + e
	g = e + f
	h = f + g
	i = g + h
	j = h + i
	k = i + j
	l = j + k
	m = k + l
	n = l + m
	o = m + n
	p = n + o
	q = o + p
	r = p + q
	s = q + r
	t = r + s
	u = s + t
	v = t + u
	w = u + v
	x = v + w
	y = w + x
	z = x + y
	return c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

print "And now another math genius' tinkering! Let's do a Fibonacci sequence."
print "I'll need to numbers from you:"
a = int(raw_input("a = "))
b = int(raw_input("b = "))

print "OK, the sequence is based on %d and %d is:" % (a, b), fibonacci(a, b)

