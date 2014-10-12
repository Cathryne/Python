# Exercise 36: Designing and Debugging (own game: CleanLab)
# http://learnpythonthehardway.org/book/ex36.html

# enables restarting of program
import sys
import os
def restart_program():
    """Restarts the current program, without returning anything before-hand
    Hence, clean-up and save data before calling."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

print "\nWelcome to CleanLab! The cleanest laboratory at this university! If anyone bothers."
print "To progress in this game, type room names and verbs from the choices presented to you."

def find_old_shit(object, action, choice1, choice2, result1, result2):
    print "\nYou found an old %s. What do you do?." % object
    choice = str(raw_input(action))
    if choice1 in choice:
        print result1
    elif choice2 in choice:
        print result2
    else:
        raw_input("I have no idea what you mean!?! Press any key to restart... ")
        restart_program()

print "You stand in the hallway from which the following"

find_old_shit("Microscope", "Polish lenses or tune light source? ", "polish", "tune", "Focussing works again!", "Samples are visible again!")
