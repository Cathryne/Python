# Exercise 15: Reading Files
# http://learnpythonthehardway.org/book/ex15.html

# loads sys and argv modules
from sys import argv

# unpacks command arguments into variables
script, filename = argv

# opens file and assigned it to variable
txt = open(filename)
# print type(txt) would return 'file'

# displayes filename (given as command argument)...
print "Here's your file %r:" % filename
print txt.read()    #  ...and file contents after calling read function on file variable

# let user confirm filename; open and display again
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()


# Study Drill 7: properly close files by calling close() method on file variable
txt_again.close()
txt.close()
