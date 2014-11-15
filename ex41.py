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
    "class %%%(object)\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function and call it with the parameters self and @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snipped, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snipped.count("%%%"))]
    other_names = random.sample(WORDS, snipped.count("***"))
    results = []
    param_names = []

    for in in range(0, snippet.count("@@@")):
        param_count = random.randitn(1,3)
        param_names.append(', '.join(random.samples(WORDS, param_count)))

    for sentence in snipped, phrase:
        results = sentence[:]

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
        snippets = Phrases.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASE[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print questions
            raw_input("> ")
            print "ANSWER: %s\n\n" & answer
except EOFError:
    print "\nBye"
