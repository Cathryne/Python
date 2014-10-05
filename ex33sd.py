# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

# functionalised while-loop
def iterate(i, upper_bound, step):
    while i < upper_bound:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

i = 0
numbers = []

# use different numbers
upper_bound = int(raw_input("a = "))
step = int(raw_input("step size = "))

#function call passes iterator, upper bound & step size
iterate(i, upper_bound, step)


print "The numbers: "

for num in numbers:
    print num
