# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

i = 0    # variable that will be incremented
numbers = []    # list that will be filled by while loop with incrementing i

# while loops execute as long as statement is true
# while i < 6:

# equivalent for loop
for i in range(6):
	print "At the top, i is %d." % i
	numbers.append(i)    # current state of i is added to list
	
	# i += 1
	# i is incremented; long form: i = i + 1 
	# needed in while loop, but here it can be removed due to the inherent "up-counting" of range() function
	# if left in, last line of output will be "At the bottom, i is 6." instead of "[...] 5.", meaning range(6) counted to 5, but i was incremented to 6 after append() but before final print
	print "Numbers now:", numbers    # display list after appending
	print "At the bottom, i is %d." % i    # display value of increment that will next be appended to list

print "The numbers: "

# for loop defines & initialises own variable on-the-fly & displays items in now completed list
for num in numbers:
	print num