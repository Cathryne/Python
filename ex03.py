# Exercise 3: Numbers and Math
# http://learnpythonthehardway.org/book/ex3.html
# general advice: leave space around all numbers & operators in mathematical operations, to distinguish from other code & esp. negative numbers

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
# , comma forces calculation result into same line
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# result of mathematical operation is printed directly; "qoutes" only for strings
# order PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition & Subtraction)
# modulo operator % returns remainder after division

print "Is it true that 3 + 2 < 5 - 7 ?"

print 3 + 2 < 5 - 7 # Boolean statement returns True or False

print "What is 3 + 2 ?", 3 + 2
print "What is 5 - 7 ?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# Study Drill 5: Rewrite to use floating point numbers so it's more accurate (hint: 20.0 is floating point).
# appending decimal point & 0 to each number
# Also works with only relevant ones?
print "And now the calculations again with floating points."
print "Hens", 25 + 30 / 6.0 # no effect, because 30 can already be completely divided by 6
print "Roosters", 100 - 25 * 3 % 4.0 # no effect because remainder of 75 / 3 = 72 is the integer 3
print "Eggs:", 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4.0 + 6 # effect, because 1 / 4.0 = 0.25
