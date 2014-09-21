from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, press CTRL+V (^C)."
print "If you do want that file erased, press RETURN."

raw_input("? ")

print "Openeing the file..."
target = open(filename, 'w')

print "Truncating the file. Good bye!"
target.truncate()

print "Now I'm going to ask you for three lines to write into the file."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close the file..."
target.close()
