# Exercise 36: Designing and Debugging (own game: CleanLab)
# http://learnpythonthehardway.org/book/ex36.html

print """\nWelcome to CleanLab! The cleanest laboratory at this university!
If anyone bothers. Which you do, right...?\n
To progress in this game, type numbers and letters
from the choices presented to you."""

# enables restarting of program
import sys
import os


def restart(message):
    """Restarts the current program, without returning anything before-hand
    Hence, clean-up and save data before calling."""
    print "Press any key to restart."
    raw_input(message)
    python = sys.executable
    os.execl(python, python, * sys.argv)

def do_stuff(action, choice1, choice2, result1, result2):
    choice = str(raw_input(action))
    if not ((choice1 in choice) or (choice2 in choice)):
        print "Try again."
        do_stuff(action, choice1, choice2, result1, result2) # learned from https://stackoverflow.com/questions/12556907/continually-prompting-user-for-input-in-python
    elif choice1 in choice:
        print "\t", result1
    elif choice2 in choice:
        print "\t", result2
    else:
        print "I have no idea what you mean!?! Press any key to restart..."
        do_stuff(action, choice1, choice2, result1, result2)


def room_choice():
    room = raw_input("Which room do you want to enter? Please type its number: ")
    try:
       room = int(room)
    except ValueError:
       restart("Learn to type a number!")
    return room
#     if any(room in entry for entry in rooms) == True: # learned from http://stackoverflow.com/a/4843172
#         matching = (s for s in rooms if room in s)
#         return matching
#     else:
#         print "Try again."
#         room_choice()


def talk_to():
    person = raw_input("Who do you want to chat to? ")
    try:
       person = int(person)
    except ValueError:
       print "Learn to type a number!"

    return person


print """You stand in the hallway of CleanLab.
You can enter one of the these rooms:"""
rooms = ["microscopy room", "protein lab", "DNA lab", "office"] # , "climate chamber", "freezer room", "PostDoc office", "PI office", "storage rooom"

for i in rooms:
    print "\t", rooms.index(i), "-", i
    i += i

room = room_choice()

if room == 0:
    print "\nIt's dark in the microscopy room. You flick the light switch and...\n...find a dysfunctional UV emitter. What do you do to fix it?"
    do_stuff("Tune emission or replace light source? ", "une", "eplace", "That was a quick and easy solution. In the short term.", "You spent a lot of money, but the microscope will work for a long time now!")
elif room == 1:
    print "\nYou hear the squeaking of an old gel shaker.\nWhat do you do to stop the squeaking?"
    do_stuff("Lubricate with some oil or reduce shaking speed? ", "ubricate", "educe", "Good job! The gels will be well shaken and the blots will work nicely!", "Useless! The gels will be inhomogeneous and the blots won't work well.")
elif room == 2:
    print "\nYou see the thermocycler's hazard light blinking.\nThe cooling block broke at the end of the sampling run. What do you do with the PCR products inside?"
    do_stuff("Leave there or transfer to fridge? ", "eave", "ransfer", "Not a good idea :-( The samples degraded and your colleague has to repeat the experiment.", "Thanks for saving the samples :-) Just don't forget to tell your colleague where exactly you put the samples.")
elif room == 3:
    print "\nThere's lots of chatter in the office."
    persons = ["Professor", "PostDoc", "Technician"]

    for i in persons:
        print "\t", persons.index(i), "-", i
        i += i

    person = talk_to()

    if person == 0:
        print "\tNo time, sorry. Have to prepare talk."
    elif person == 1:
        print "\tNo time, sorry. Have to write manuscript."
    elif person == 2:
        print "\tNo time, sorry. Have to prepare experiment."
    else:
        person = talk_to()


else:
    restart("That was not any of those numbers!")
