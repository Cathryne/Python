# Exercise 16: Reading and Writing Files
# http://learnpythonthehardway.org/book/ex16.html
# Study Drill 2: Write script that reads file written by ex16, using read() and argv

from sys import argv
script, filename = argv

# create file object and convert content to string
file = open(filename)
content = file.read()

print "Here is what you wrote in ex16:\n%s\n" % content

print "Closing..."
file.close()