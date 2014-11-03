# Exercise 40: Modules, Classes, and Objects
# http://learnpythonthehardway.org/book/ex40.html

# class definition followed by suit (usually contains only function definitions)
class Song(object):

    # initialises empty object upon instantiation of class
    def __init__(self, lyrics):
        # assignment of variable that is passed into class; self specifies instance attribute & differentiates from potential local variable of same name
        self.lyrics = lyrics

    # custom function definition that iterates through lines of list variable
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# instantiates classes & passes lyric lists into resulting objects
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# calls custom function from class on objects that contain lyric lists
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
