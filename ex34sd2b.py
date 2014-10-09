# Exercise 34: Accessing Elements of Lists
# http://learnpythonthehardway.org/book/ex34.html
# Study Drill 2: Write some more lists and work out similar indexes until you can translate them.

ingredient = raw_input("Let's make a meal! Main ingredient: ")
meal = [ingredient]

# user input loop until exited
while ingredient != "exit":
	# get next ingredient name as string
	ingredient = str(raw_input('OK, what else? Or type "exit": '))
	# exit loop or append ingredient name to list
	if ingredient == "exit":
		print "OK, exiting..."
	else:
		meal.append(ingredient)

# display list contents
print "So, you'll need:", meal
