# Exercise 15: Reading Files
# http://learnpythonthehardway.org/book/ex15.html
# Study Drill 5: Use raw_input() instead of argv

# get filename from user
filename = raw_input("\nWhich file do you want to open? Please type its name here, including file extension: ")

# opens file and assigned it to variable
file_content = open(filename)
# print type(txt) would return 'file'

# displayes filename (given as command argument)...
print "OK, thanks! Here's your file %r:" % filename
print file_content.read()    #  ...and file contents after calling read function on file variable
file_content.close()
