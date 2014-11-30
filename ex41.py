import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function and call it with the parameters self and @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# check for certain command argument
if len(sys.argv) == 2 and sys.argv[1] == "english":
    # sys.arg is list, with script's filename as first/0th element but is only created if command argument is given at all
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # fills empty word list with words from downloaded file
    WORDS.append(word.strip())
    # strip is function of module 'string'

def convert(snipped, phrase):
    # initialise lists with items to be compiled into sentence later
    # list comprehension is way to construct lists from conditional statements
    class_names = [w.capitalize() for w in random.sample(WORDS, snipped.count("%%%"))]
    other_names = random.sample(WORDS, snipped.count("***"))
    # 'sample(population, k)' is method of class 'random' that returns list of k elements picked randomly from population
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snipped, phrase:
        result = sentence[:]
        # CSQ: "slice" syntax of copying a list from 1st to last element

        # next 3 for loops insert elements from _names lists into result sentence

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL+D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            # poses assembled question, waits for input & displays answer no matter what
            print question
            raw_input("INPUT:  ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    # class in module 'exceptions'; is returned when Python tries to read beyond end of file
    print "\nBye"
