# Exercise 8: Printing, Printing
# http://learnpythonthehardway.org/book/ex8.html

# formatting characters can have different types
formatter = "%r %r %r %r"
# formatter = "%s %s %s %s" works as well, because (1, 2, 3, 4) can be strings as well ("downward compatible")
# formatter = "%d %d %d %d" can't work, because ("one", "two", "three", "four") can't be decimal numbers

# Displaying different insertions into above variable
# always same as print "%r %r %r %r" % ...
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) # recursive insertion
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # internal ' will make output be surrounded by "", rather than ''
	"So I said goodnight.",
)