# Exercise 16: Reading and Writing Files
# http://learnpythonthehardway.org/book/ex16.html

# pass & unpack command arguments into script
from sys import argv
script, filename = argv

# prompt user to abort or confirm file overwrite
print "We're going to erase %r." % filename
print "If you don't want that, press CTRL+V (^C)."
print "If you do want that file erased, press RETURN."
raw_input("? ")

print "Opening the file..."
# open file in write mode
target = open(filename, 'w')
# Study Drill 4: open() defaults to read-only mode

# Overwrite content by truncating file to 0 bytes
print "Truncating the file. Good bye!"
target.truncate()
# Study Drill 5: Not required, because opening in write mode already overwrites existing content. Tested by by adding target.flush() and checking file size & content changes while script ran.

print "Now I'm going to ask you for three lines to write into the file."
# Prompt user for file contents
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# Study Drill 3: simplify multiple write commands with multi-line
target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close the file..."
target.close()
