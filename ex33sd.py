# Exercise 33: While Loops
# http://learnpythonthehardway.org/book/ex33.html

# functionalised while-loop
def iterate(i):
    while i < 6:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

i = 0
numbers = []

#function call passes iterator
iterate(i)


print "The numbers: "

for num in numbers:
    print num
