# Exercise 17: More Files
# http://learnpythonthehardway.org/book/ex17.html
# Study Drill 1: Make ex17 more user-friendly by removing features.

from sys import argv
from os.path import exists
script, from_file, to_file = argv

print "Copying from %s to %s..." % (from_file, to_file)

# sequential combination of file opening and content reading
in_data = open(from_file).read()

# Another function sequence: opening and writing
open(to_file, 'w').write(in_data)

print "OK, all done!"
