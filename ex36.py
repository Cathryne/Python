# Exercise 36: Designing and Debugging (own game: CleanLab)
# http://learnpythonthehardway.org/book/ex36.html

print """\nWelcome to CleanLab! The cleanest laboratory at this university!
If anyone bothers. Which you do, right...?\n
To progress in this game, type room names
and verbs from the choices presented to you."""

# enables restarting of program
import sys
import os


def restart_program():
    """Restarts the current program, without returning anything before-hand
    Hence, clean-up and save data before calling."""
    raw_input("I have no idea what you mean!?! Press any key to restart... ")
    python = sys.executable
    os.execl(python, python, * sys.argv)


def do_stuff(action, choice1, choice2, result1, result2):
    print  "What do you do?"
    choice = str(raw_input(action))
    if choice1 in choice:
        print "\t", result1
    elif choice2 in choice:
        print "\t", result2
    else:
        restart_program()



# Room selection

print """You stand in the hallway of CleanLab.
There are the following rooms:"""
rooms = ["protein lab", "DNA lab", "climate chamber", "freezer room", "PhD office", "PostDoc office", "PI office", "storage rooom", "microscopy room"]

for i in rooms:
    print "\t", i
    i += i

enter = raw_input("Which room do enter? ")

if "micro" in enter:
    print """\nIt's dark in the microscopy room. You flick the light switch and...
    ...find an old UV emitter."""
    do_stuff("Tune emission or replace light source? ", "une", "eplace", "That wasa quick and easy solution. In the short term.", "You spent a lot of money, but the microscope will work for a long time now!")
elif "protein" in enter:
    print "\nYou hear the squeaking of an old gel shaker."
    do_stuff("Lubricate with some oil or reduce shaking speed? ", "ubricate", "educe", "Good job! The gels will be well shaken and the blots will work nicely!", "Useless! The gels will be inhomogeneous and the blots won't work well.")
else:
    restart_program()
