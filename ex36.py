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
    if not ((choice1 in choice) or (choice2 in choice) or "leave"):
        print "Learn to type a room number! Or leave."
        do_stuff(action, choice1, choice2, result1, result2) # learned from https://stackoverflow.com/questions/12556907/continually-prompting-user-for-input-in-python
    elif choice1 in choice:
        print "\t", result1
    elif choice2 in choice:
        print "\t", result2
    else:
        restart("\nOK, back to the hallway!")


def option_choice(N_options, message):
    option_number = raw_input(message)

    try:
        option_number = int(option_number)
    except ValueError:
       print "A number, please."
       return option_choice(N_options, message)
       # return essential here, because function call only would create noneType in final return value of whole function
       # learned from https://www.daniweb.com/software-development/python/threads/380491/trouble-with-nonetype-after-calling-a-function#post1638105

    option_number = int(option_number)

    if option_number > N_options:
        print "Only one of the above numbers, please."
        return option_choice(N_options, message)

    else:
        return option_number


def list_options(list_name):
    for i in list_name:
        print "\t%d:" % (list_name.index(i) + 1), i
        i += i


def back_to_hallway(room_exit):
    raw_input("Press any key to return to the hallway ")
    print "You exited the %s" % room_exit
    room = option_choice(N_rooms, "Which room do you want to enter now? ")


print """You stand in the hallway of CleanLab.
You can enter one of the these rooms:"""
rooms = ["microscopy room", "protein lab", "DNA lab", "office"] # , "climate chamber", "freezer room", "PostDoc office", "PI office", "storage rooom"
N_rooms = len(rooms)
list_options(rooms)
room = option_choice(N_rooms, "Which room do you want to enter? Please type its number: ")

if room == 1:
    print "\nIt's dark in the microscopy room. You flick the light switch and...\n...find a dysfunctional UV emitter. What do you do to fix it?"
    do_stuff("Tune emission or replace light source? ", "une", "eplace", "That was a quick and easy solution. In the short term.", "You spent a lot of money, but the microscope will work for a long time now!")
    back_to_hallway(rooms[0])
elif room == 2:
    print "\nYou hear the squeaking of an old gel shaker.\nWhat do you do to stop the squeaking?"
    do_stuff("Lubricate with some oil or reduce shaking speed? ", "ubricate", "educe", "Good job! The gels will be well shaken and the blots will work nicely!", "Useless! The gels will be inhomogeneous and the blots won't work well.")
    back_to_hallway(rooms[1])
elif room == 3:
    print "\nYou see the thermocycler's hazard light blinking.\nThe cooling block broke at the end of the sampling run. What do you do with the PCR products inside?"
    do_stuff("Let it be or transfer to fridge? ", "et", "ransfer", "Not a good idea :-( The samples degraded and your colleague has to repeat the experiment.", "Thanks for saving the samples :-) Just don't forget to tell your colleague where exactly you put the samples.")
    back_to_hallway(rooms[2])
elif room == 4:
    print "\nThere's lots of chatter in the office."
    persons = ["Professor", "PostDoc", "Technician"]
    N_persons = len(persons)
    list_options(persons)
    person = option_choice(N_persons, "Who do you want to chat to? ")

    if person == 1:
        print "\tNo time, sorry. Have to prepare talk."
        back_to_hallway(rooms[3])
    elif person == 2:
        print "\tNo time, sorry. Have to write manuscript."
        back_to_hallway(rooms[3])
    elif person == 3:
        print "\tNo time, sorry. Have to prepare experiment."
        back_to_hallway(rooms[3])
    else:
        back_to_hallway(rooms[3])

    back_to_hallway(rooms[3])

else:
    restart("That was not any of those numbers!")
