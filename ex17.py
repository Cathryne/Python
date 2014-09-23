# Exercise 17: More Files
# http://learnpythonthehardway.org/book/ex17.html


from sys import argv
from os.path import exists
script, from_file, to_file = argv

print "Copyinf from %s to %s..." % (from_file, to_file)

# combine opening of file and reading of content
in_data = open(from_file).read()

print "The input file is %d bytes long." % len(in_data) # built-in function, also for number of items in sequence

print "Does the output file exist? %r" % exists(to_file) # function of Posix module
raw_input("Ready! Press RETURN to continue or CTRL+C to abort. ")

# combine opening and writing
open(to_file, 'w').write(in_data)

print "OK, all done!"
