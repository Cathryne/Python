# Exercise 14: Prompting and Passing
# http://learnpythonthehardway.org/book/ex14.html

# get arguments from user's command execution & assign to variables
from sys import argv
script, user_name, computer_name = argv

# prompt variable (string-type) contains the characters used to highlight the prompt to user 
prompt = 'So speak! '

# display inputs from command arguments
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name

# prompt for next variable with the string assigned above to highlight the prompt
likes = raw_input(prompt)

# prompt for more variables with string from prompt variable
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
 
print "What kind of computer do you have?"
computer = raw_input(prompt)
 
 # display additional variable inputs
print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
And you have a %r computer. Nice! Oh, that's me, isn't it? Call me %s please ;-)
""" % (likes, lives, computer, computer_name)

# What's wrong with the following code?
# print "What should my name be then?"
# computer_name = raw_input(prompt)
# print "OK, I'll henceforth be known as %s!" % computer_name
# Wrong logic: computer_name assigned by command argument already. Doesn't need prompt.
