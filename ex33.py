# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

# Study Drills: functionalised loop with variable end point % step-size
def iterate(N, M):
    for i in range(0, N, M):    # step size is optional argument of range() function, which makes start point mandatory
        print "i at the top: %d" % i
        numbers.append(i)   # iterative action
        i += M  # incrementation of iterator absolutely essential to prevent infinite looping
        # useful checks for status of iterator & result of iterative action
        print "Numbers now:", numbers
        print "i at the bottom: %d" % i


N = int(raw_input("Please provide an end number (start is 0): "))
M = int(raw_input("And a step-size, please: "))

numbers = []    # initialise empty list

iterate(N, M)

# initialise while-loop with iterator
# executes indented code block until boolean expression returns FALSE

print "The numbers:"
for num in numbers:
    print num
