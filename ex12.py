# Exercise 12: Prompting People
# http://learnpythonthehardway.org/book/ex12.html

# request input from user
# shorter alternative to ex11 with extra print ""
height = float(raw_input("How tall are you (in m)? "))
weight = int(raw_input("How many kilograms do you weigh? "))

print "So, you're %r m tall and %d kg heavy." % (height, weight) 

# shorter without "BMI" helper variable in ex11: calculate directly after print, even without string formatting
print "That makes your BMI round about:", round(weight / ( height * height ), 1)    # round(x, n) rounds x to n decimal places