# Exercise 11: Asking Questions
# http://learnpythonthehardway.org/book/ex11.html

# request input from user by:
# a) displaying instructions separately from input function
print "How old are you?",
# b) applying input function
age = raw_input()

# alternative
height = raw_input("How tall are you? ")

print "How much do you weigh?",
weight = raw_input()
# raw => can be mixed types, like number with unit => integer with string

# displaying inputs in raw type (as entered) with string formatting
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
