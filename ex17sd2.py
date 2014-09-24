# Exercise 17: More Files
# http://learnpythonthehardway.org/book/ex17.html
# Study Drill 2: Shorten ex17 even more by combining lines via ;

from sys import argv; from os.path import exists; script, from_file, to_file = argv; print "Copying from %s to %s..." % (from_file, to_file); open(to_file, 'w').write(open(from_file).read()); print "OK, all done!" # nested opening, reading and writing
