# Exercise 40: Modules, Classes, and Objects
# http://learnpythonthehardway.org/book/ex40.html

# class definition followed by suit (usually contains only function definitions)
class Song(object):

    # initialises empty object upon instantiation of class
    def __init__(self, input):
        # assignment of variable that is passed into class; self specifies instance attribute & differentiates from potential local variable of same name
        self.lyrics = input

    # custom function definition that iterates through lines of list variable
    def sing_me_a_song(self):
        print "-" * 10
        for i in self.lyrics:  # "line" was only iterator & can therefore be renamed
            print i

# instantiates classes & passes lyric lists into resulting objects
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
# Study Drill 1:  Write some more lists of strings
humming = Song(["Dadaa Dada Dadadada",
                "Dadum Dadum Dadadadum"])

# Study Drill 2: Put lyrics in separate variable & pass into class
bird_song = ["Chirp", "Chirp", "Chirp"]
bird = Song(bird_song)

# calls custom function from class on objects that contain lyric lists
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
humming.sing_me_a_song()
bird.sing_me_a_song()
