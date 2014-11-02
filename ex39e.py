# Exercise 38: Doing Things To Lists
# http://learnpythonthehardway.org/book/ex38.html
# Study Drill 6: other examples of lists and what do do with them
# comparing word lists

# quote examples for testing
# Hamlet = "To be, or not to be, that is the question."
# https://en.wikipedia.org/wiki/To_be,_or_not_to_be#Text
# Crusoe = "Thus fear of danger is ten thousand times more terrifying than danger itself."
# https://www.goodreads.com/quotes/318230-thus-fear-of-danger-is-ten-thousand-times-more-terrifying

# functionalised listing of character name & quote words into list
def make_list(character, quote):
	import string
	quote_list = [character]
	word_list = quote.translate(None, string.punctuation)
	word_list = word_list.split(' ')
	print "\tOK, so %s said: " % character, word_list
	for i in range(len(word_list)):
		last_word = word_list.pop()
		quote_list.append(last_word)
		i =+ 1
	# print quote_list
	return quote_list

def add_to_dict(dict, i):
    character = str(raw_input("\tWho shall 1st quote number %d be from? " % (i+1)))
    quote = str(raw_input("\tAnd what did they say? "))
    dict[character] = quote  # one at a time
    return dict


N_quotes = 2
print "\tLet's play a literature game! You are going to tell me %d famous quotes and I'm going to tell you, which words they have in common." % N_quotes

dict = {}

for i in range(N_quotes):
    add_to_dict(dict, i)

print "OK, we'll use these quotes:"
for k, v in dict.items():
    print k, "said: %r" % v


# determine longer quote & assign
if len(quote1_list) <= len(quote2_list):
	reticent = character1
	fewer_words = quote1
	shorter_list = quote1_list
	verbose = character2
	more_words = quote2
	longer_list = quote2_list
else:
	reticent = character2
	fewer_words = quote2
	shorter_list = quote2_list
	verbose = character1
	more_words = quote1
	longer_list = quote1_list

print "\tIn other words, %s was reticent in saying:" % reticent, fewer_words
print "\tWhile %s was verbose:" % verbose, more_words

# compare quote lists & convert result to new list
plagiates = set(quote1_list).intersection(quote2_list)
plagiates = list(plagiates)

# check if plagiates exist & display
if len(plagiates) != 0:
	print "\tHa! Either %s or %s plagiarised the words from the other:" % (character1, character2), plagiates
else:
	print "\tNo plagiate words found!"
