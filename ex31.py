# Exercise 31: Making Decisions
# http://learnpythonthehardway.org/book/ex31.html

# enables restarting of program
import sys
import os
def restart_program():
    """Restarts the current program, without returning anything before-hand
    Hence, clean-up and save data before calling."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

door = raw_input("\nYou enter a dark room with three doors. Do you go through the door to your _front_, _left_ or _right_? ")
# while loop to prevent invalid responses
# strange problem: only 1st answer was accepted by (logical) code "while door != ("1st" or "2nd" or "3rd")
# strange problem: only 3rd answer was accepted by (logical) code "while door != ("1st" and "2nd" and "3rd")
# possible explanation: while & if blocks execute only if statement is true.
# truth terms need "" here, because numbers haven't been converted by int() and are thus still strings
while door != "left" and door != "right" and door != "front":
	door = raw_input("Please pick a door: front, left or right. ")

# Study Drill 1: New game part with input check and restart function
if door == "front":
	gold = int(raw_input("\nYou find three chests of gold. How many do you take for your self? "))

	if gold == 0:
    	raw_input("\nYou found the easter-egg and get to play again, after pressing any key.")
    	restart_program()

    # numbers converted to integers here, thus no "" necessary
	while gold != 1 and gold != 2 and gold != 3:
		gold = raw_input("How many gold chests do you take? 1, 2 or 3? ")

	if gold <= 2:
		print "\nOK, that's reasonable. A ladder appears from above and ceiling cat helps you get out into the fresh air.\n"
	elif gold == 3:
		print "\nYou're a greedy one! The weight of the gold breaks your back and the floor. You fall into the darkness.\n"

elif door == "left":
    print """\nThere's a giant bear here eating a cheese cake.
    1. Take the cake.
    2. Scream at the bear."""
    bear = raw_input("What do you do? ")

    if bear == "1":
         print "The bear eats your face off. Good job!"
    elif bear == "2":
    	print "The bear eats your legs off. Good job!"
    else:
    	raw_input("\nYour answer doesn't fit to the options. Press anything to start the game now. ")
    	restart_program()

elif door == "right":
    print """\nYou stare into the endless abyss at Cthulhu's retina."
    1. Blueberries.
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies."""
    insanity = raw_input("What will it be? ")

    if insanity == "1" or insanity == "2":
    	print "\nYour body survives powered by a mind of jello. Good job!\n"
    else:
    	print "\nThe insanity rots your eyes into a pool of muck. Good job!\n"
