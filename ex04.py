# Exercise 4: Variables And Names
# http://learnpythonthehardway.org/book/ex4.html

#variable definitions: name = value
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# calculations same, regardless whether done with numbers directly or variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity =  cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# displaying results; print valid for entire line; insertion of values via variables
# , replaces newline after print "1st part" with space
print "There are", cars, "cars available."
print "There are", drivers, " drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drill 1: Necessary to use decimal point for space_in_car?
space_in_a_car = 4
carpool_capacity =  cars_driven * space_in_a_car
print "Without decimal point, we can transport", carpool_capacity, "people today."
# no, not necessary output changes from "120.0" to "120"
# necessary however, if result can be a fractional number
