from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copyinf from %s to %s..." % (from_file, to_file)

# We could do these two on one line, but how?
in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes ling." % len(in_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready! Press RETURN to continue or CTRL+C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "OK, all done!"

out_file.close()
in_file.close()
