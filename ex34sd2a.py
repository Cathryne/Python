# Exercise 34: Accessing Elements of Lists
# http://learnpythonthehardway.org/book/ex34.html
# Study Drill 2: Write some more lists and work out similar indexes until you can translate them.

# function to print out list entry
# 1-line functions can remain individual commands
def print_animal():
	print "List entry %d is:" % animal_out, animals[animal_out]

# wrong order of requesting a list entry from user
# animals = []
# animal_in = raw_input('Please tell me which animal I should add to the list: ')
# missing the addition of animal_in to the list
# 1st while iteration will replace animal_in with next input, so list is smaller than user may assume

# correct order of requesting a list entry from user
animal_in = raw_input('Add animal to list: ')
animals = [animal_in]

# adding more list entries until user aborts input
while animal_in != "exit":
	animal_in = str(raw_input('Another one? Or type "exit": '))    	# could do input check & exception handing here, see http://stackoverflow.com/a/22025830
	if animal_in == "exit":
		print "OK, exiting..."
	else:
		animals.append(animal_in)

	# needlessly long
	# animals.append(animal_in)
	# if animal_in == "exit":
	# 	print "OK, exiting and removing %r entry..." % animal_in
	# 	animals.remove("exit")


# get integer from user & assign to "retrieval" variable for animals list
# wrong: animals.count()=> returns not list size in total, but number of entries specified in ()
animal_out = int(raw_input("List contains %d animals. Which one to display? " % len(animals)))
if animal_out == "exit":
	print "OK, exiting..."
else:
	print_animal()

# more displaying until user aborts
while animal_out != "exit":
	animal_out = raw_input('Another one? You can finish the input by typing "exit": ')
	# basic input check by detecting "exit"
	if animal_out != "exit":
		animal_out = int(animal_out)
		print_animal()
	else:
		print "OK, exiting..."
