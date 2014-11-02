# -*- coding: utf-8 -*-
# required to use German Umlaute in ; otherwise: SyntaxError: Non-ASCII character '\xc3' in file ex39.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

# Exercise 39: Dictionaries, Oh Lovely Dictionaries
# http://learnpythonthehardway.org/book/ex39.html

# map/associate states to abbreviations (case-sensitive!)
states = {
	'Sachsen-Anhalt': 'SA',
	'Berlin': 'B',
	'Hamburg': 'HH',
	'Bremen': 'HB',
	'Niedersachsen': 'NS',
}

# map some cities to states
cities = {
	'SA': 'Dresden',
	'NS': 'Hannover',
	'HB': 'Bremerhaven'
}

# add cities to empty dicts; otherwise: KeyError
cities['B'] = 'Mitte'
cities['HH'] = 'Harburg'

# display some cities by accessing values in dict via keys
print '-' * 10
print "NS has:", cities['NS']
print "BW has:", cities['SA']

# display some states & their abbreviations
print '-' * 10
print "Niedersachsen's abbreviation is:", states['Niedersachsen']
print "Sachsen-Anhalt's abbreviation is:", states['Sachsen-Anhalt']

# repeat above, but by using both dictionaries
print '-' * 10
print "Niedersachsen contains:", cities[states['Niedersachsen']]
print "Sachsen-Anhalt contains:",  cities[states['Sachsen-Anhalt']]
# nested retrieval of abbreviation (inner), followed by outer one (city), because cities list uses abbreviation as identifier
# value that was retrieved via key in inner dict can be key for outer dict

# display all state abbreviations
print '-' * 10
for state, abbr in states.items():
	print "%s is abbreviated %s." % (state, abbr)

# display every city in state
print '-' * 10
for abbr, city in cities.items():
	print "%s contains %s." % (abbr, city)

# now both at the same time
print '-' * 10
for state, abbr in states.items():
	print "%s state is abbreviated %s and has city %s." % (
		state, abbr, cities[abbr])    # goes through all states, abbreviations and all cities accessed by the latter

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Bayern')

if not state:
	print "Sorry, no Bayern."

# get a city with a default value
city = cities.get('BY', 'Does not exist')
print "The city for the state 'BY' is: %s" % city
