class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init(self, scene_map):
        pass

    def play(self):
        pass

class Death(object):

    def enter(self):
        pass

class Corridor(object):

    def enter(self):
        pass

class Armory(object):

    def enter(self):
        pass

class Bridge(object):

    def enter(self):
        pass

class Escape(object):

    def enter(self):
        pass


class Map(object):

    def __init_(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('Corridor')
a_game = Engine(a_map)
a_game.play()
