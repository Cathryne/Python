# Exercise 26: Congratulations, Take a Test!
# http://learnpythonthehardway.org/book/ex26.html

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)    # missing : after function definition
    """Prints the first word after popping it off."""
    word = words.poop(0)    # typo in method
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1    # missing )
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5    # wrong math => 5 needs to be 6
print "This should be five: %s" % five    # from conversion specifier: five is intiger, so %d would be correct

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100    # wrong character: backslash => needs to be /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)
# wrong operator: == checks if left & right are equal; returns boolean => needs to be only =
# also, wrong symbol: - should be _

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont
# typo in string
# typo in variable & missing )


sentence = "All god\tthings come to those who weight."
# typo in string

words = ex25.break_words(sentence)    # "ex25." not required if script is run
sorted_words = ex25.sort_words(words)    # "ex25." only needed to call function from Python environment

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)    # incorrect .
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words    # typo in built-in function name

print_irst_and_last(sentence)    # typo in function name

   print_first_a_last_sorted(senence)    # incorrect tab & typo in variable
