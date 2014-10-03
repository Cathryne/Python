# Exercise 30: Else and If
# http://learnpythonthehardway.org/book/ex30.html

print "We'll need some numbers. How many people, cars and buses should there be?"
people = int(raw_input("People: "))
cars = int(raw_input("Cars: "))
buses = int(raw_input("Buses: "))

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# intended code only executed if "parent" if or elif statement is true
# 1st true if or elif statement is executed, while following true ones are dropped

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we should take the trucks."
else:
	print "We still can't decice."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

# Study Drill 3: More complex boolean expressions
# check if both numbers or people equals number of cars, and if number of cars equals number of buses
if people == cars and cars == trucks:
	# if True (people = cars = buses), display the following
	print "One person per car or truck. Let's squeeze into the latter. Will be merrier drives."
# if False (either people != cars or  cars != trucks), display other message
elif people > cars and (people > trucks + cars):
	print "Too many people for even cars and trucks combined. We'll have to stay."
elif people != cars and cars != trucks:
	print "All different!"
