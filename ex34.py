# Exercise 34: Accessing Elements of Lists
# http://learnpythonthehardway.org/book/ex34.html

def get_animal_out(animal_out, animals):
    if animal_out == "exit":
        print "OK, exiting..."
    else:
        print "OK, at index %d I found the %s." % (animal_out, animals[animal_out])

# prompt user for 1st element & initialise list with that
animals = []
animal_in = str(raw_input("Which animal shall I add to the list? "))

# keep prompting for more elements
print "A few more, please. type 'exit' to close."
while animal_in != "exit":
    animals.append(animal_in) # can take 1st animal_in from before loop, but doesn't take last "exit"
    animal_in = str(raw_input("Which animal shall I add to the list? "))
    if animal_in == "exit":
		print "OK, exiting..."

print "\nOK, the list is now %d elements long: %r" % (len(animals), animals)

# set initial value to max. index
animal_out = len(animals) - 1
print "And it ends with the %s." % animals[animal_out]

while animal_out < len(animals):
    animal_out = int(raw_input("\nA few more? Again, type 'exit' to stop. "))
    if animal_out >= len(animals):
        print "Sorry, the maximum index is only %d. Exiting..." % (len(animals) - 1)
    else:
        get_animal_out(animal_out, animals)



