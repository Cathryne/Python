# Exercise 42: Is-A, Has-A, Objects, and Classes
# http://learnpythonthehardway.org/book/ex42.html

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a attribute "name"
        self.name = name

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a attribute "name"
        self.name = name

# Person is-a object => parent class to Employee(Person)
class Person(object):

    def __init__(self, name):
        # Person has-a attribute "name"
        self.name = name

        # Person has-a pet of a default type upon instantiation
        self.pet = None

# Employee is-a Person => child class of Person(object)
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a attribute that results from method  "__init__" being called with parameter "name" on result of function "super" that is called with parameters "Employee" & "self"
        # super() runs __init__ of parent class; long explanation: http://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        # effectively; Employee has-a name
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet that is-a satan is-a Cat
mary.pet = satan

# frank is-a Employee that has-a salary of 120000
frank = Employee("Frank", 120000)

# frank has-a pet that is-a rover is-a Dog
frank.pet = rover

# flipper is-a Fish is-a object
flipper = Fish()

# crouse is-a Salmon is-a fish
crouse = Salmon()

# harry is-a Halibut is-a fish
harry = Halibut()
