# Exercise 19: Functions and Variables
# http://learnpythonthehardway.org/book/ex19.html

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	"""
	Prints out the results of cheese and crackers counting
	by different, previously done calculations.
	"""
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man! That's enough for a party!"
	print "Get a blanket.\n"

# CSQ: get variables from user

print "Yo! Raid the fridge!"
amount_of_cheese = int(raw_input("How much cheese do you have? "))
amount_of_crackers = int(raw_input("And how many boxes of crackers? "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "Or, let's increase that. I know you are hiding some of the goodies!"
cheese_and_crackers(amount_of_cheese * 2, amount_of_crackers * 3)
