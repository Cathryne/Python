# Exercise 32: Loops and Lists
# http://learnpythonthehardway.org/book/ex32.html

# initialises lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for-loop uses iterator to go through list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# printing items from mixed lists requires general conversion specifier in string formatting
for i in change:
    print "I got %r" % i

# initialises empty list
elements = []

# fill empty list iteratively
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # applies "append"-method
#     elements.append(i)
# Study Drill 2: fill empty list in a simpler way
elements = range(0, 6)

# Works in Python console also :-)
# >>> list = []
# >>> list = range(11)
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list = []
# >>> for i in range(11):
# ...     list.append(i)
# ...
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in elements:
    print "Element was: %d" % i
