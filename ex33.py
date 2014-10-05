# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

i = 0   # initialise variable
numbers = []    # initialise empty list

# initialise while-loop with iterator
# executes indented code block until boolean expression returns FALSE
while i < 6:
    print "i at the top: %d" % i

    # iterative action
    numbers.append(i)

    # incrementation of iterator absolutely essential to prevent infinite looping
    i += 1

    # useful checks for status of iterator & result of iterative action
    print "Numbers now:", numbers
    print "i at the bottom: %d" % i

print "The numbers:"
for num in numbers:
    print num
