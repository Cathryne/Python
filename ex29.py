# Exercise 29: What If
# http://learnpythonthehardway.org/book/ex29.html

# Study Drill 5: Other initial values? Will result in different if statement becoming true!
print "We'll need some numbers. How many people, cats and dogs should there be?"
people = int(raw_input("People: "))
cats = int(raw_input("Cats: "))
dogs = int(raw_input("Dogs: "))

# Study Drills 1-3. if statement with variable comparison, : and indented commands that only execute if statement is true. In other words: code branch with boolean bouncer.
# "IndentationError: expected an indented block" if not intended by 4 spaces
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

# Study Drill 4: Other boolean expressions, see ex27
if people != cats:
	print "Different number of cats and humans. Anarchy!"

if people == cats:
	print "Equal number of cats and humans. Harmony!"


# "increment-by operator" or "contraction" => short-hand notation for dogs = dogs + 5
# increments same variable
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."

print "\nNow they are multiplying! But by which factors?"
people_multiplier = int(raw_input("People: "))
cat_multiplier = int(raw_input("Cats: "))
dog_multiplier = int(raw_input("Dogs: "))

# contraction / short-hand notation for people = people * pm
people *= people_multiplier
cats *= cat_multiplier
dogs *= dog_multiplier

if people < cats:
   	print "Too many cats! The world is doomed!"

if people > cats:
   	print "Not many cats! The world is saved."

if people != cats:
	print "Different number of cats and humans. Anarchy!"

if people == cats:
	print "Equal number of cats and humans. Harmony!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry."

if people == dogs:
   	print "People are dogs."
