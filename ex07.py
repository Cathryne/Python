# Exercise 7: More Printing
# http://learnpythonthehardway.org/book/ex7.html

# Displaying string variables, 2nd with insertion
print "Mary had a little lamb."
print "Its fleece was white as %s." % "snow"    # On-the-fly insertion of string here saves up-front definition of string variable: snow = "snow"
print "And everywhere that Mary went."
print "." * 40    # multiplication of print output

# Defining more string variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Combining string variables
# comma prevents new line in output, enforces only a space
# otherwise: single print command with many variables would make line too long = bad style
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12 

# Testing comma effects
print "Yes, the"
print "comma really does",
print "replace the default line ending with a space."