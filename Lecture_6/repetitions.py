#------------Classes---------
# Vanliga klasser: init, magic methods, methods, arguments, istans/klass/objekt, inheritance vs composition
# Functions, args, kwargs
# Dataclasses
from dataclasses import dataclass
# Create a class and an object of that class
class Person:
    pass

my_dude = Person()


# Create a class with properties 
class Human:
# In dataclasses, properties must be listed here, before the init
# You can place default values here
    name: str
    age: int
    def __init__(self, name: str, age: int):
        self.name = name
        self. age = age

the_dude = Human("Jeff", 40)

# Data can be stored even without init method, if we create another method for doing it

class Noinit:
    name: str
    age: int

    def addname(self, name: str):
        self.name = name

noinithuman = Noinit() # Create object
noinithuman.addname("Humberto") # runs addname() to add name
print(noinithuman.name)


#-------------Dataclasses-------------

# @dataclasses adds an init-function (and some other shit)
# Dataclass don't need no init method, can still store data
# We can write an init-method in a dataclass, it will overwrite the dataclass init method
# Decorators change the behaviour of what they are decorating

@dataclass
class DataHuman:
    name: str
    age: str

my_datahuman = DataHuman("Jeff", 40)


# if you print a dataclass (print(DataHuman)), it looks different from printing a normal class
# Just as dataclasses have their own init-methods, they have other methods too, this being one of them



#---------Magic Methods---------

#__dict__ returns the values of the object as a dictionary
# my_datahuman.__dict__
#__str__ returns a string value. "Print(object)" returns whatever this method specifies


class PrintPerson:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str: # Arrow shows what will be returned
        return "Jadu"

# olof = PrintPerson("olof")
# print(olof) # Returns whatever is in the __str__ ("Jadu")
# print(olof.__dict__) #Prints the properties as dict ({'name': 'Olof', 'age': 40})



#-----------args/kwargs----------

def my_function(*args, **kwargs):
    print(f"my_function {args}, {kwargs}") # args return tuple, kwarg returns dict

my_function("olof", "är", "sur", olof = 23, bajs = "Hanna") # Send in arguments and keyword arguments respectivelly

# Order: positional, arguments, keyword arguments
# Other arguments can be inserted if specified later, see below
# Self is a positional arguments, always gets in first position
# So if we add self, "olof" will be self, since it's the first position

def my_function(self, *args, **kwargs):
    print(f"my_function {args}, {kwargs}") 

my_function("olof", "är", "sur", olof = 23, bajs = "Hanna") # olof is excluded from the printout, since it is now "self" and self was not printed

# This is extra important in methods, where self is needed


def my_function(*args, otherarg, **kwargs): # Add otherarg as a value
    print(f"my_function {args}, {kwargs}, {otherarg}") # print otherarg

my_function("olof", "är", "sur", otherarg= "bajs", olof = 23, bajs = "Hanna") # Define value of otherarg

# print() takes infinite arguments. Puts them in a list and goes through

def my_function2(*args, **kwargs): # Add otherarg as a value
    print(f"my_function {args}, {kwargs}") 

def my_second_function(func, *args, **kwargs): # First argument is a function
    func(*args, **kwargs) #send in the function, with the args and kwargs as arguments

my_second_function(my_function2, "olof", "är", "sur", olof = 23, bajs = "Hanna") 
# my_second_function(func, *args, **kwargs) is run with my_function2 as the function
# and the other arguments as the arguments in my_founction2
# Basically, this runts my_function2, since my_second_function just runs another function


def my_third_function(func, *args, **kwargs): # First argument is a function
    a, b, *rest = args # "unpacking". Does this mean we pick out element one (a) and two (b), and let the rest remain in *rest?
    print(a,b) # Prints "Olof" and "Hatar", first and second element or *args
    print(rest)
    func(*args, **kwargs) # Sends the rest of the args into "func"

def my_function_three(*args, **kwargs):
    print(f"my_function {args}, {kwargs}") 

my_third_function(my_function_three, "Olof", "Hatar", "Allt", "men", "är", "glad", "ändå", hej = 1, då = 2)
# my_third_function is run first????? And the my_function_three??? Why is that?
# my_third_function saves all args in "args"
# It also saves first item in "a", asecond in "b", and the rest in "rest"
# So "a" = "Olof", "b" = "Hatar"
# "rest" = ['Allt', 'men', 'är', 'glad', 'ändå']
# "args"

#----------instance/class/objhects--------

# Instance is an object of a specific class
# Class is a blueprint for an object
# Object is a collection of data and methods


#--------inheritance and composition---------

class Person:
    pass

class Teacher(Person): # all teachers are persons, but not all persons are teachers
    pass

class Student(Person):
    pass

# Composition is when a class contain multiple instances of another class
# Eg. a course has several students. Both course and students are classes
# No inheritance between the two, just that one class consists of many of the other class
# Allows you to manipulate the collection of instances within the class they are a part of



# Inheritance using @dataclass
@dataclass
class Animal():
    tooth_count: int
    colour: str
    size: int

class Dog(Animal):
    fur: str
    def __init__(self, fur: str):
        self.fur = fur
    def bark(self):
        print("woof")

fido = Dog(4, "gray", "medium") # Inheritance is autoomatic
rufus = Dog()
print(fido)
fido.bark()

@dataclass # dataclass automatically adds all properties, inherited and not, when creating the mouse-object (mickey)
class Mouse(Animal):
    habitat: str
    sound: str


#mikey = Mouse() # options for all atributes are added because Mouse is a @dataclass
# Otherwise we would have to use init
# Below is the same thing but without using @dataclass
class Animal1:
    tooth_count: int
    colour: str
    size: int

    def __init__(self, tooth_count: int, colour: str, size: int):
        self.tooth_count = tooth_count
        self.colour = colour
        self.size = size

class Fish(Animal1):
    sound: str

    def __init__(self, sound, tooth_count, colour, size):
        super().__init__(tooth_count, colour, size)
        self.sound = sound


guppy = Fish("blubb", 4, "Black", 125)
print(guppy.colour)

# Anything that cen be described as a verb is a method (usually)
# Noun is an attribute or a class (usually)

