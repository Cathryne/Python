# Exercise 30: Else and If
# http://learnpythonthehardway.org/book/ex30.html

print "We'll need some numbers. How many people, cars and buses should there be?"
people = int(raw_input("People: "))
cars = int(raw_input("Cars: "))
trucks = int(raw_input("Trucks: "))

if cars > people:
	print "Us %d people should take the %d cars." % (people, cars)
elif cars < people:
	print "Us %d people should not take the %d cars." % (people, cars)
else:
	print "We can't decide. There are %d people and %d cars." % (people, cars)

# intended code only executed if "parent" if or elif statement is true
# 1st true if or elif statement is executed, while following true ones are dropped

if trucks > cars:
	print "%d trucks is too many, compared to %d cars." % (trucks, cars)
elif trucks < cars:
	print "Maybe we should take the %d trucks instead of the %d cars." % (trucks, cars)
else:
	print "We still can't decice. There are %d trucks and %d cars." % (trucks, cars)

if people > trucks:
	print "Alright, let's just take the %d trucks, because we are %d people ." % (trucks, people)
else:
	print "Fine, let's stay home then."

# Study Drill 3: More complex boolean expressions
# check if both numbers or people equals number of cars, and if number of cars equals number of trucks
if people == cars and cars == trucks:
	# if True (people = cars = buses), display the following
	print "One person per car or truck makes %d rides." % ((people + cars + trucks) / 3)
# if False (either people != cars or  cars != trucks), display other message
elif people > cars and (people > trucks + cars):
	print "Too many people (%d) for even cars and trucks combined (%d) . We'll have to stay." % (people, cars + trucks)
elif people != cars and cars != trucks:
	print "All different: %d people, %d cars and %d trucks." % (people, cars, trucks)
