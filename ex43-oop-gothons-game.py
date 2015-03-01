# Exercise 43: Basic Object-Oriented Analysis and Design
# http://learnpythonthehardway.org/book/ex43.html

import random

# Scene is-an object
class Scene(object):

    # Scene has-an enter function that takes the default parameter.
    def enter(self):
        pass


class Engine(object):

    # Engine has-an init function that takes 2 parameters
    def __init__(self, scene_map):
        pass

    # Engine also has-a play function that takes only self as an parameter.
    def play(self):
        pass

# Death is-an object
class Death(object):

    # Death has-an enter function that takes self as an parameter.
    def enter(self):
        print "You died in a funny way!"


# same as above

class Corridor(object):

    def enter(self):
        print "You are in the central corridor of the ship. Where do you want to go next?"
        places = ['Armory', 'Bridge', 'Escape Pod']

        for idx, place in enumerate(places):
            print idx, place
            # learned from https://stackoverflow.com/questions/522563/; alternative to for-looping over range()

class Armory(object):

    def enter(self):
        print "You find a bomb."

class Bridge(object):

    def enter(self):
        print "You can set the bomb here."

class Escape(object):

    def enter(self):
        pods = ['A', 'B', 'C', 'D', 'E']
        N_pods = len(pods)
        N_damaged_pods = int(N_pods * 2 / 3)
        #damaged_pods = random.sample(pods, N_damaged_pods)
        damaged_pods = ['C', 'D', 'E']

        print "This is the list of the %d escape pods:" % (N_pods)
        for pod in pods:
            print pod

        print "Unfortunately, %d of them are damaged, but you don't know which ones." % N_damaged_pods

        pod = str(raw_input("You better pick an undamaged pod... "))

        if pod in damaged_pods:
            print "The escape failed :-("
        else:
            print "The escape worked :-)"

# Map is-an object
class Map(object):

    # Map has-an init function that takes the parameters self and start_scene.
    def __init__(self, start_scene):
        pass

    # Map also has-a next_scene function that takes parameters self and scene_name.
    def next_scene(self, scene_name):
        pass

    # Map also has-an opening_scene function that takes only the self parameter.
    def opening_scene(self):
        pass


# Instantiate class Map with parameter 'Corridor' (passed into init function) in object a_map
a_map = Map('Corridor')

# Instantiate class Engine with parameter a_map (which is 'Corridor' passed into Engine's init function) in object a_game
a_game = Engine(a_map)

# From a_game (instance of Engine), execute function play()
a_game.play()
