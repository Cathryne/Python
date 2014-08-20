# Exercise 11: Asking Questions
# http://learnpythonthehardway.org/book/ex11.html

# request input from user by:
# a) displaying instructions separately from input function
print "How many years are you old?",
# b) applying input function
age = int(raw_input())
# int() converts input to integer type

# alternative, one-line input prompt
height_m = float(raw_input("How tall are you (in m)? "))
# float() converts input to loating point decimal type

# alternative
# height_cm = int(raw_input("How tall are you (in m)? "))
# height_m = float(float(height_cm) / 100)

print "How much do you weigh (in kg)?",
weight = int(raw_input())

# displaying inputs in raw type (as entered) with string formatting
print "So, you're %d old, %d m tall and %d kg heavy." % (
	age, height_m, weight)

# calculate & display BMI, needs defined units
BMI = weight / ( height_m * height_m )
print "Therefore, your BMI is: %d." % BMI
