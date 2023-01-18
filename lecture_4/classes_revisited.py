



from typing import List, Tuple


class Animals:
    sound: str
    
    def __init__(self, sound: str):
        self.sound = sound

    def speak(self):
        print(f"I say {self.sound}")
        return f"I say {self.sound}"

    def change_sound(self, sound: str):
        self.sound = sound

cat = Animals("Mjau")
# Only prints the sound:
#print(cat.sound) # calling using the argument you get the print from the function, since its run.

# Runs speak(), thus printing and then prints the return. Prints I say mjau twice.
#print(cat.speak()) # calling using the function, we recieve "return" and prints that. No return, output is "none"

# Change sound
# cat.change_sound("SHKRIII")
#print(cat.sound) # Prints only the sound, nothing else
#print(cat.speak()) # Runs the function (printing the sentance), then prints the return
cat.speak() # Runs the function

dog = Animals("Woooof")
horse = Animals("Gnägg")
cow = Animals("Mooooo")

# cow.speak() # "I say Moooo"

class Person:

    def __init__(self, first_name: str, last_name: str, age: int, height: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.full_name = f"{self.first_name} {self.last_name}" # Creates new variable without taking any more inputs
        self.company = company

    def __str__(self) -> str:
        return f"The person is called {self.first_name} {self.last_name}"

    def give_name(self):
        print(f"{self.first_name} {self.last_name}")

    ## When creating out own magic methods, we define what datatype they are
    ## This way, whenever we call the method, we will get an answer of that datatype
    ## Also, if we run the object with a function that requires that datatype, magic method will run
    ## print(object) will run -> str, int(object) will run -> int, etc

    
    def __int__(self) -> int: 
        return len(self.last_name)

    def __int2__(self, letter) -> int:
        return self.last_name.count(letter)

    def __list__(self) -> list:
        return [self.first_name, self.last_name, self.age] # if "return self.first_name, self.last_name, self.age" then result is set to tuple, not list

# olof = Person("Olof", "Stenlund", 33, 173)
# print(olof) # Because of the __str__ printing the object prints whatever is returned in __str__
# olof.give_name() # runs give_name
# print(olof.give_name()) # Returns none, since return from give_name is none (it only prints, does not return)
# print(olof.give_name) # prints infor about the method, as we dont call it using ()
# print(olof.__list__()) # Prints the return from __list__. If return is not set as list, result will be tuple
# test = int(olof) # Int(olof) calls the first int-method (__int__). Must be called that?
# print(test) # return from __int__ is 8, prints here
# print(olof.__int2__("n")) # sends "n" into __int2__, counting the number of "n" in last_name



class Company: # Since we use the class Company in the next class, we must define Company first

    def __init__(self, name: str, location: str, CEO: str):
        self.name = name
        self.location = location
        self.CEO = CEO

    def __str__(self) -> str:
        return f"CEO is {self.CEO}"

class EmployedPerson: 
    def __init__(self, first_name: str, last_name: str, age: int, height: int, company: Company): # Takes another class as argument
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.full_name = f"{self.first_name} {self.last_name}" # Creates new variable without taking any more inputs
        self.company = company 

    def __str__(self) -> str:
        return f"The person is called {self.first_name} {self.last_name}"

    def give_name(self):
        print(f"{self.first_name} {self.last_name}")

    def __int__(self) -> int: 
        return len(self.last_name)

    def __int2__(self, letter) -> int:
        return self.last_name.count(letter)

    def __list__(self) -> list:
        return [self.first_name, self.last_name, self.age]

# # Creating an EmployedPerson, we must now enter the agruemnts in the class company.
# Torgny = EmployedPerson("Torgny", "Söderqvist", 60, 193, Company("Logisnext", "Mölnlycke", "Martin Björkroth"))
# print(Torgny.company.CEO) # get the CEO from company, from employedperson
# lastnameletters = int(Torgny) # runs the int-method, counting the number of letter in the last name
# print(lastnameletters) 
# logisnext = Company("Logisnext", "Mölnlycke", "Martin Björkroth")

# print(logisnext) # Prints __str__ from Company (print(logisnext.__str__()))

# # You can access the function within Company by going through another object of that class
# print(f"{Torgny.first_name} works at {Torgny.company.name}, and their {logisnext.__str__()}")
# # Or you can access it through the person-object. "logisnext.__str__()" and "Torgny.company.__str__()" leads to the same place
# print(f"{Torgny.first_name} works at {Torgny.company.name}, and their {Torgny.company.__str__()}")



## Inheritance

class Phone:
    number: str 
    maker: str = "illuminati"
    weight: int
    year: int
    colour: str

    def __init__(self, number: str, maker: str, weight: int, year: int, colour: str):
        self.number = number
        self.maker = maker
        self.weight = weight
        self.year = year
        self.colour = colour


class SmartPhone(Phone):
    five_g_compatible: bool
    camera_lenses: int
    apps: List[str] # What is the difference between List[str] (imported) and list[str]

    def __init__(self, five_g_compatible: bool, camera_lenses: int, apps: list[str], number: str, maker: str, weight: int, year: int, colour: str):
        super().__init__(number, maker, weight, year, colour) # super().__init to run the init function in super. Cannot use "maker: str" format
        self.five_g_compatible = five_g_compatible
        self.camera_lenses = camera_lenses
        self.apps = apps

    def __str__(self) -> str:
        return f"This is a {self.maker} phone"

#g7 = SmartPhone(True, 5, ["Google Maps", "SleepCycle", "Swedbank"])
g8 = SmartPhone(True, 5, ["facebook", "tinder"], "025480", "Nokia", 210, 2019, "black") # adds all values in super and sub
print(g8.apps) # Return the list of apps
print(g8.apps[0]) # Return only the first item, index 0
# In the above case, the __init__ method of the superclass Phone does not run.
# Therefore, the values associated with it, are not assigned.

# You can set a default value to avoid errors when values have not been assigned.
# class SuperClass():
    # name: str = "hej"
    # age: int = 0
# These will return when called on, unless any other value is assigned

# class NokiaPhone(SmartPhone): # Inherits from smartphone, which inherits from phone.
#     # Init is run in smartphone, which (thanks to super()) runs init in super-class as well
#     pass