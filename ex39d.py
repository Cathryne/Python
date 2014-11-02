# Exercise 38: Doing Things To Lists
# http://learnpythonthehardway.org/book/ex38.html
# Study Drill 6: other examples of lists and what do do with them

import string  #


# create list of words from character's line by stripping punctuation & splitting at spaces
def wordlist(characters_line):
	characters_words = characters_line.translate(None, string.punctuation)
	characters_words = characters_words.split(' ')
	# 1-line alternative: characters_words = characters_line.translate(None, string.punctuation).split(' ')
	return characters_words

def result(character, characters_words):
    print "\n%s's words are:" % character, characters_words
    print "\nAnd %r was his last word..." % characters_words.pop()


print "\nLet's play a literature quiz! I am going to show you famous lines, you select one and then we'll garble the words!\n"

dict = {
    "Hamlet" : "To be, or not to be, that is the question.",  # https://en.wikipedia.org/wiki/To_be,_or_not_to_be#Text
    "Crusoe": "Thus fear of danger is ten thousand times more terrifying than danger itself.",  # https://www.goodreads.com/quotes/318230-thus-fear-of-danger-is-ten-thousand-times-more-terrifying
    "Weasley": "Never trust anything that can think for itself if you can't see where it keeps its brain."  # http://www.quotegarden.com/bk-hp.html
    }

for k, v in dict.items():
    print k, "said: %r" % v

# Get character name from user as raw input & convert to lower case, so that if statements can work with only that spelling variant
choice = raw_input("\nOK, whose quote shall we work with? Please type the name of the characters who spoke the quote you want: ")

# if ("hamlet" or "Hamlet") in choice: # doesn't work, only 1st one is accepted
if "Hamlet" in choice:
	# Hamlets_words = Hamlet.translate(None, string.punctuation)
	# Hamlets_words = Hamlets_words.split(' ')
	# Hamlets_words = Hamlet.split(' ') doesn't work, because Hamlet string variable still has the punctuation, only Hamlets_words doesn't
	# functionalised version of above:
	Hamlets_words = wordlist(Hamlets_line)
	result(choice, Hamlets_words)
elif "Crusoe" in choice:
	Crusoes_words = wordlist(Crusoes_line)
	result(choice, Crusoes_words)
elif "Weasley" in choice:
	Weasleys_words = wordlist(Weasleys_line)
	result(choice, Weasleys_words)
else:
	print "No correct guess, sorry!"

print ""
