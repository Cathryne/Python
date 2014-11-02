# Exercise 39: Making Your Own Dictionary Module
# http://learnpythonthehardway.org/book/ex39.html

import ex39c_hashmap

# create a mapping of state to abbreviation
states = ex39c_hashmap.new()
ex39c_hashmap.set(states, 'Oregon', 'OR')
ex39c_hashmap.set(states, 'Florida', 'FL')
ex39c_hashmap.set(states, 'California', 'CA')
ex39c_hashmap.set(states, 'New York', 'NY')
ex39c_hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = ex39c_hashmap.new()
ex39c_hashmap.set(cities, 'CA', 'San Francisco')
ex39c_hashmap.set(cities, 'MI', 'Detroit')
ex39c_hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
ex39c_hashmap.set(cities, 'NY', 'New York')
ex39c_hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY State has: %s" % ex39c_hashmap.get(cities, 'NY')
print "OR State has: %s" % ex39c_hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % ex39c_hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % ex39c_hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % ex39c_hashmap.get(cities, ex39c_hashmap.get(states, 'Michigan'))
print "Florida has: %s" % ex39c_hashmap.get(cities, ex39c_hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
ex39c_hashmap.list(states)

# print every city in state
print '-' * 10
ex39c_hashmap.list(cities)

print '-' * 10
# by default python says "nil" when something isn't in there
state = ex39c_hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = ex39c_hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

print '-' * 10
print "Now adding a city to Texas"
ex39c_hashmap.set(cities, 'TX', 'Houston')
print ex39c_hashmap.list(cities)  # introduces a None somehow at end of list

print '-' * 10
print "We have the following cities now:"
print list(cities)
delete_cities = str(raw_input("Which state shall we delete the city from? "))
ex39c_hashmap.delete(cities, delete_cities)
print "OK, it's deleted, see?"
print list(cities)


