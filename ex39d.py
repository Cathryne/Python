# Exercise 38: Doing Things To Lists
# http://learnpythonthehardway.org/book/ex38.html
# Study Drill 6: other examples of lists and what do do with them

import string


# create list of words from character's line by stripping punctuation & splitting at spaces
def wordlist(dict, character):
    characters_words = dict[character].translate(None, string.punctuation).split(' ')
    print "\n%s's words are:" % character, characters_words
    print "\nAnd %r was his last word..." % characters_words.pop()

def character_choice(message):
    character = str(raw_input(message))
    return character


print "\nLet's play a literature quiz! I am going to show you famous lines, you select one and then we'll garble the words!\n"

dict = {
    "Hamlet" : "To be, or not to be, that is the question.",  # https://en.wikipedia.org/wiki/To_be,_or_not_to_be#Text
    "Crusoe": "Thus fear of danger is ten thousand times more terrifying than danger itself.",  # https://www.goodreads.com/quotes/318230-thus-fear-of-danger-is-ten-thousand-times-more-terrifying
    "Weasley": "Never trust anything that can think for itself if you can't see where it keeps its brain."  # http://www.quotegarden.com/bk-hp.html
    }

for k, v in dict.items():
    print k, "said: %r" % v

# Get character name from user as raw input & convert to lower case, so that if statements can work with only that spelling variant
character = character_choice("Whose quote shall we work with? Please type the name of its speaker: ")

try:
    wordlist(dict, character)
except KeyError:
    character = character_choice("Lean to type a name! ")
    wordlist(dict, character)


