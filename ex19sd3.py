# Exercise 19: Functions and Variables
# http://learnpythonthehardway.org/book/ex19.html
# Study Drill 3: Write at least one more function of your own design, and run it 10 different ways.

def milkshake(milk_to_blend, fruit_to_blend, suggar_to_blend):
	servings = int(raw_input("Oh yeah, I forgot! For how many servings shall all this be? "))
	milk_to_serve = servings * milk_to_blend
	fruit_to_serve = servings * fruit_to_blend
	suggar_to_serve = servings * suggar_to_blend
	print "You'll need %d g fruit, %d mL milk and %d g of suggar. Will it blend?!" % (fruit_to_serve, milk_to_serve, suggar_to_serve)

milk = 200
fruit = 50
suggar = 10

print "\nLet's make a milkshake! I know this recipe: Blend %d mL milk, %d g fruit and %d g suggar in a blender. However, you should adjust something..." % (milk, fruit, suggar)

# get recipe modifiers from user; can be negative
fruitiness = float(raw_input("... Like the fruitiness! How many % more or less do you want? "))
sweetness = float(raw_input("Same for the sweetness: "))


print "\n\nResults calculated in function call:"
milkshake(milk, fruit * (1 + (fruitiness / 100)), suggar * (1 + (sweetness / 100)))

print "\n\nResults calculated via helper variables:"
milk_to_blend = milk
fruit_to_blend = fruit * (1 + (fruitiness / 100))
suggar_to_blend = suggar * (1 + (sweetness / 100))
milkshake(milk_to_blend, fruit_to_blend, suggar_to_blend)