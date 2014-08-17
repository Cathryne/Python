# Exercise 5: More Variables and Printing
# http://learnpythonthehardway.org/book/ex5.html

# variable definitions, both strings and numbers
name = 'Zed A. Shaw'
age = 35 
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# inserting variable values into strings via format strings
# percent symbols followed by s or d within print statement indicate format sequences for strings and integers
# % after print statement needs to be followed by variable name whose value should be inserted; separate several by comma and enclose in parentheses
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "And %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eye and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# more inserting with on-thy-fly math
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

# Study Drill 1: removing all ""-parts from variable names