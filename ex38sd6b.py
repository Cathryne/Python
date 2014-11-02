# Exercise 38: Doing Things To Lists
# http://learnpythonthehardway.org/book/ex38.html
# Study Drill 6: other examples of lists and what do do with them
# detecting email addresses & extracting 1st & last name
# inspired by https://github.com/pagekite/Mailpile/issues/776

# functionalised extraction of 1st & lastname from name list, plus title casing
def extract_1st_lastname(splitter):
	name = alias.split(splitter)
	firstname = name[0].title()
	lastname = name[1].title()
	print "\tOK, I think this person is called %s %s." %(firstname, lastname)

alias = raw_input("\tPlease enter an email address: ")
alias = str(alias)  # converts to string
alias = alias.split('@')  # splits into list at @
alias = alias.pop(0)  # returns 1st item in list, which must be alias
# 1-line alternative: alias = str(raw_input("Please enter an email address: ")).split('@').pop(0)

# check for splitters (order just from gut feeling) & split alias string into name list
if '.' in alias:
	extract_1st_lastname('.')
elif '_' in alias:
	extract_1st_lastname('_')
elif '-' in alias:
	extract_1st_lastname('-')
	# could become a problem with double-names, ergo also no use to try something general like "split on punctuation"
else:
	print "\tNo splitter found. Omitting name extraction & sticking with alias:", alias
