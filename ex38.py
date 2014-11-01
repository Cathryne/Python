# Exercise 38: Doing Things to Lists
# http://learnpythonthehardway.org/book/ex38.html

ten_things = "Apples Oranges Crows Telephone Light Sugar"  # initialise string variable

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')  # split string into list at spaces
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]  # initialise list variable with some items


# CSQ: alternative to while len(stuff) != 10
for i in range(len(stuff), 10):
    next_one = more_stuff.pop()  # removes and returns last item from 2nd list
    print "Adding: ", next_one
    stuff.append(next_one)  # adds returned item from 2nd list to 1st
    print "There are %d items now." % len(stuff)  # displays length of appended 1st list
    i += 1  # not for while-loop

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]  # displays item at index 1 = 2nd item, because cardinal numbers
print stuff[-1]  # displays last item in list
print stuff.pop()  # removes & returns last item in list
print ' '.join(stuff)  # merges list items into string with spaces in between; can't be stuff.join(' ')
print '#'.join(stuff[3:5]) # merges items at indices 3 and 4 (like range(3,5)) with # in between
