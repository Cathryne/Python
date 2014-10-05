# Exercise 33: While Loops -- Study Drills
# http://learnpythonthehardway.org/book/ex33.html

# while loop from ex33 completely converted to function
# def while_append(i):
# 	while i < upper_bound:
# 		print "At the top, i is %d." % i
# 		numbers.append(i)    # current state of i is added to list
# 		i += 1    # i is incremented; long form: i = i + 1; causes infinite loop if in function 
# 		print "Numbers now: ", numbers
# 		print "At the bottom, i is %d." % i    # display value of increment that will next be appended to list

# while loop from ex33 partially converted to function
def while_append(i):
	print "At the top, i is %d." % i
	numbers.append(i)    # current state of i is added to list
		
i = 0    # variable that will be incremented

upper_bound = int(raw_input("Please tell me a natural number: "))
increment = int(raw_input("And one of it's divisors, please: "))
upper_bound += increment

# keep prompting for increment that is divisor of upper_bound
# upper_bound = int(raw_input("Please tell me a natural/integer number between 1 and 20: ")) 
while (((upper_bound / increment) <= 2) and (upper_bound % increment != 0)): 
	increment = int(raw_input("Erm, sorry, but that's not a divisor for %d. Please try again: " % upper_bound))

numbers = []    # list that will be filled by while loop with incrementing i

# rest of functionalised while loops
while i < upper_bound:
	while_append(i)
	i += increment    # i is incremented; long form: i = i + 1; causes infinite loop if in function 
	print "Numbers now: ", numbers
	print "At the bottom, i is %d." % i    # display value of increment that will next be appended to list
	
	
print "The numbers: "

# for loop defines & initialises own variable on-the-fly & displays items in now completed list
for num in numbers:
	print num

# print "No, I didn't forget the %d, I just started counting at 0 ;-p" % upper_bound