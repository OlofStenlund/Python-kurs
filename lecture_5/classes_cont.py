from dataclasses import dataclass

class Person:
    def __init__(self, name: str, age: int, spy_name: str):
        self.name = name
        self.age = age
        self.spy_name = spy_name


olof = Person("Olof", 30, "Locust")

#print(olof.name)

# A public attribute is like the above, reachable by typing olof.name.
# You can define the attributes as private so tehy cannot be as easily modified

olof.name = "Siegward"
#print(olof.name)
# Name has now easily been modified

#print(olof.spy_name) # oops, spy_name should not be public

class Person_spy:
    def __init__(self, name: str, age: int, spy_name: str):
        self.name = name
        self.age = age
        self.__spy_name = spy_name # Private
        
    def get_spy_name(self):
        print(self.__spy_name)

    def get_spyname_return(self):
        return self.__spy_name

    def set_spyname(self, spy_name: str):
        self.__spy_name = spy_name

    def __shoutout_spy_name(self): # Private function
        print(self.__spy_name)

    def public_shoutout(self):
        self.__shoutout_spy_name()

OlofSpy = Person_spy("Olof", 30, "Locust")

#print(OlofSpy.__spy_name) # This does not work, __ makles the attribute private, so __spy_name is not available 
#print(OlofSpy.name)
#OlofSpy.get_spy_name() # <-- by calling the function in the class, we can get the name 

# Getter and setter
# Functions inside classes that return what you want

# print(OlofSpy.get_spyname_return()) # runs get_spyname_return, which returns the name. Then prints the returned name
# print(OlofSpy.set_spyname("Local plague")) # use function set_spyname to change the values of spyname
# print(OlofSpy.get_spyname_return()) # Print new spyname

#OlofSpy.__shoutout_spy_name() # 
#OlofSpy.public_shoutout() # Runs public_shoutout, which runs __shoutout_spy_name

# Private can be accessed by using other functions inside the class.
# Private attributes in a class can be accessed by a function inside the same class
# Private functions in a class can be accessed using a function in the same class that runs the function



#-------------Static methods--------------------

# Methods that don't change the class?

class Person_spy_boss:

    def __init__(self):
        pass

    @staticmethod # Must have a decorator to work
    def say_hi(): # Ususally, slef is needed, but not in a static method. In fact, do not use self. Arguments can be used, self is out.
        print("Hi")

Göran = Person_spy_boss()

#Göran.say_hi() 
#Göran.say_hi("my friend") # to use this, arguments must be set in say_hi()


class Calculator: # Init not needed because no data is saved in the class
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def subtract(a, b):
        return a-b
    @staticmethod
    def multiply(a, b):
        return a*b
    @staticmethod
    def divide(a, b):
        return a/b

res = Calculator.add(3, 5)
#print(res)


#--------------Dataklasser----------------

#@dataclass # must be imported from library dataclasses. Is a decorator for a class
# Init not needed, automatically created. also __repr__, whatever that is
# Dataclasses can take arguments as well
class Animal:
    name: str
    height: float
    weight: float
    diet: str

    def update_name(self, name):
        self.name = name

    # def __str__(self): # If you print the class, __str__ is retuned if used?
    #     return "hello"

mouse = Animal("Mickey", 2.5, 120, "Omnivore")
print(mouse)
mouse.update_name("Samuel")
print(mouse.name)

#@dataclass(init=false, repr=false) # Negates init and repr. Other arguments can be used

@dataclass(kw_only=True) # you have to define keyword when defining object
class Dog(Animal): # inheritance
    race: str

@dataclass
class Cat(Animal):
    race: str

Fido = Dog("Fido", 21.6, 12, "carnivore", race = "dalmatian") # If you use kw_only "race =" needs to be scecified
ShaggyDog = Cat("ShaggyDog", 21.2, 4.5, "carnivore", "Mancoon") # Cat is not kw_only, keyword need not be specified
print(Fido, ShaggyDog)