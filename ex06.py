# Exercise 6: Strings and Text
# http://learnpythonthehardway.org/book/ex6.html

# variable definitions can have string formatters, too
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# raw formatting of string within single quotes 
print "I said: %r" % x
print "I also said: '%s'." % y
# string formatting of string doesn't include ''

# Boolean and string variable definitions
hilarious = False
joke_evaluation = "Isn't that joke so funn?! %r" # value not inserted immediately

print joke_evaluation % hilarious # value inserted here

w = "This is the left side of... "
e = "A string with a right side."

# addition of strings
print w + e
