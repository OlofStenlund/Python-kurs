# Everything is objects in python
#print(type(1)) # <- returns <class, 'int'> ie, it is an object of class int
# Classes are a blueprint for its features
from typing import List
# IMPORTANT!! Classes do not use snake_case, but CapWork/PascalCase
class AnimalInCaptivity:
    sound: str ="Growl" # <- Basically a keyword pair in the class. An object of the class recieves the sound "growl"
    def __init__(self, sound: str): # will run when the class is initiated. Other functions run when called on
        self.sound = sound
    
    def speak(self):
        print( "I say " + self.sound)


# self.sound = sound -> self= the object, .sound = the field or value within the class, = sound = the value being sent into the class, argument
# what comes after the = is the input value

class AnimalInTheWild:
    pass

animal1 = AnimalInCaptivity("woof")

#print(type(animal1)) #<- returns <class '__main__'.AnimalInCaptivity. __main__refers to the whole file?
# If you import a class from another file (say, 'file_2') it will say 'file2.animal' instead.

print(AnimalInCaptivity.sound)

class Person:
    sound: str = "Gnyr"
    def speak(self): # <- first positional argument, is self, refers to the first instance of the object
        return("I say " + self.sound) # If we chose to print, then the funtion will return None, so if we call the function, the return will be none.
        # A function that returns none returns no output

olof = Person()
#print(olof.speak())

dog = AnimalInCaptivity("bjäbb")
#print(dog.sound)
#print(dog.speak())

class AnimalInCaptivity:
    sound: str ="Growl" 
    def __init__(self, sound: str): # self is the object(dog) sound is the second argument
        self.sound = sound # dog.sound = sound (sound being the string value used as argument when definin dog ("woof")


class Person2:
    def __init__(self, first_name: str, last_name: str, age: int, height: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def __str__(self) -> str:
        return f"hej, jag heter {self.first_name} {self.last_name} och är {self.age} år gammal och {self.height} cm lång"

olof = Person2("Olof", "Stenlund", 33, 175)
#print(olof.first_name) # Prints the first name 
#print(olof) # prints the info about the class (unless there is a __str__ in the class)

# Create another object of the class and pass the info. Print the return (comes from the __str__)
lasse = Person2("Lasse", "Mickelssen", 45, 187)
#print(lasse) 

#__str__ decides what is printed when we print(object)

class Company:
    name: str
    number_of_employees: int
    adress: str
    CEO: str

    def __init__(self, name: str, number_of_emplyees: int, adress: str, CEO: str):
        self.name = name
        self.number_of_employees = number_of_emplyees
        self.adress = adress
        self.CEO = CEO

class Person3:
    first_name: str
    last_name: str
    age: int
    height: int
    full_name: str

    def __init__(self, first_name: str, last_name: str, age: int, height: int, company: Company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.company = company
        self.full_name = f"{first_name} {last_name}" # creates a new attribute even without input, by putting together inputs
        
    def __str__(self) -> str:
        return f"hej, jag heter {self.first_name} {self.last_name} och är {self.age} år gammal och {self.height} cm lång, och jobbar på {self.company.name}"

#olof3 = Person3("Olof", "Stenlund", 30, 175) # No full name input
#print(olof3.full_name) # but full name output


# Look at what he did with company, it was a class in a class

olof4 = Person3("Olof", "Stenlund", 33, 175, Company("Unicarriers", 150, "Rådavägen", "Martin Björkroth"))
#rint(olof4.company.CEO) # prints the values of CEO in the company assigned to the class that olof4 belongs to
#print(olof4)

# inheritance. A class can use another class as basis

class Phone:
    number: str # can start with 0, int can't
    weight: int
    manufacurer: str
    colour: str
    five_g_enabeled: bool
    
    def __init__(self, number: str, weight: int, manufacturer: str, colour: str, five_g_enabeled: bool):
        self.number = number
        self.weight = weight
        self.manufacurer = manufacturer
        self.colour = colour
        five_g_enabeled = five_g_enabeled

class SmartPhone(Phone): # Smartphone derives from the superclass Phone. Inherits it's properties
    apps: List[str] # Must be imported from typings
    foldable: bool

    def __init__(self, apps: List[str], foldable: bool, number: str, weight: int, manufacturer: str, colour: str, five_g_enabeled: bool):
        super().__init__(number, weight, manufacturer, colour, five_g_enabeled) # calls the into from the superclass __init__ function
        self.apps = apps
        self.foldable = foldable

    def __str__(self) -> str:
        return f"Min telefon är från {self.manufacurer} och väger {self.weight} gram. Den är också {self.colour}"

min_fån = SmartPhone(["maps", "tinder"], False, "051245", 215, "LG", "dark blue", "False" ) # Only __init__ from the subclass is run?
print(min_fån)