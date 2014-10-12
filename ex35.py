# Exercise 35: Branches and Functions
# http://learnpythonthehardway.org/book/ex35.html

# make exit module/class available
from sys import exit

# function for gold room: ask user for number input & react depending on number value
def gold_room():
	choice = raw_input("This room is full of gold. How much do you take? ")
	# other variant of checking input for integer type:  if next.isdigit(), see  http://stackoverflow.com/a/5424750
	try:
		how_much = int(choice)
	except ValueError:
	    dead("Man, learn to type a number.") # jumps to line 63

	if how_much < 50:
		print "Nice! Not greedy wins!"
		exit(0) # exits program gracefully (0 means no error, anything else would be an error message ID number)
	else:
		print "The bear hears you rummaging about and drags you to his room."
		bear_room() # jumps to line 63


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True: # infinite loop => needs dedicated exit point(s; 2 stages here) somewhere in it, because while statement can't become False
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.") # jumps to line 63
        elif choice == "taunt bear":
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and "bear moved":
            dead("The bear gets pissed off and chews your leg off.") # jumps to line 63
        elif choice == "open door" and bear_moved:
            gold_room() # jumps to line 8
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start() # jumps to line 87
    elif "head" in choice:
        dead("Well that was tasty!") # jumps to line 63
    else:
        cthulhu_room() # jumps to line 48


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room() # jumps to line 25
    elif choice == "right":
        cthulhu_room() # jumps to line 48
    elif choice == "front":
        print "Congratulations! You found a short-cut!"
        gold_room() # jumps to line 8
    else:
        dead("You stumble around the room until you starve.")


start() # jumps to line 67
