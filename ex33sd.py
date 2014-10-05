# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

# functionalised while-loop
def iterate(i, upper_bound):
    while i < upper_bound:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

i = 0
numbers = []

# use different numbers
upper_bound = int(raw_input("a = "))

#function call passes iterator & upper bound
iterate(i, upper_bound)


print "The numbers: "

for num in numbers:
    print num
