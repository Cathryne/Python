# Exercise 9: Printing, Printing, Printing
# http://learnpythonthehardway.org/book/ex9.html

# Define string variables 
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n enforces new line in out-put

# Output lists of days & months as formatted above
print "Here are the days: ", days
print "Here are the months: ", months

# Alternative:
# print "Here are the days: %s" % days
# print "Here are the months: %s" % months
# %r would output exactly "\nJan\nFeb\n..."

# Output multiple lines between 3 double or single quotes
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" 