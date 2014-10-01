# Exercise 25: Even More Practice
# http://learnpythonthehardway.org/book/html

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)	# jumps up to line 6 and assignes words returned from there to variable here
	return sort_words(words)	# jumps up to line 11 and itself returns return value from there

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)	# jumps up to line 6 and assignes words returned from there to variable here
	print_first_word(words)	# jumps to line 15
	print_last_word(words)	# jumps to line 20

def print_first_and_last_sorted(sentence):
	"""Sorts the words and prints the first and last one."""
	words = sort_sentence(sentence)	# jumps up to line 25, then 6
	print_first_word(words)	# jumps to line 15
	print_last_word(words)	# jumps to line 20

sentence = "All good things come to those who wait."
words = break_words(sentence)	#jumps to line 6
print words

sorted_words = sort_words(words)	# jumps to line 11
print sorted_words

print_first_word(words)	# jumps to line 15
print_last_word(words)	# jumps to line 20
print words

print_first_word(sorted_words)	# jumps to line 15
print_last_word(sorted_words)	# jumps to line 20
print sorted_words

sorted_words = sort_sentence(sentence)	# jumps to line 25, then 6
print sorted_words

print_first_and_last(sentence)	# jumps to line 30 and 6, then 31 and 15, then 32 and 20
print_first_and_last_sorted(sentence)	# jumps to line  36, 25 and 6, then 37 and 15, then 38 and 20
