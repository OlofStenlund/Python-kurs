from dataclasses import dataclass
from typing import List


# class TestClass:
#     item1: str
#     item2: int
#     item3: List[str]

#     def __init__(self, item1: str, item2: int, item3: List[str]):
#         self.item1 = item1
#         self.item2 = item2
#         self.item3 = item3

#     def __str__(self) -> str:
#         return f"The items are: {self.item1}, {self.item2}, {self.item3}"
    

# olof = TestClass("ajajaj", 34, ["listan", "ännu en"])
# print(olof)


# @dataclass
# class TestDataClass:
#     item1: str
#     item2: int
#     item3: List[str]

#     def __str__(self) -> str:
#         return f"The items are: {self.item1}, {self.item2}, {self.item3}"
# # Without the __str__ it årints: "TestDataClass(item1='ajajaj', item2=34, item3=['listan', 'ännu en'])"
# # With the __str__ it prints: The items are: ajajaj, 34, ['listan', 'ännu en']
# # It has a builtin __str__, how does this one work?
# olof2 = TestDataClass("ajajaj", 34, ["listan", "ännu en"])
# print(olof2)

# Let's try to make an object with several classes

# class Phone:
#     pass
# class Cellphone:
#     pass
# class Landline:
#     pass
# class ElectronicDevice:
#     pass
# class InsuredObject:
#     pass



@dataclass
class CellPhone:
    OS: str
    batteryMaH: int
    year: int
    apps: List[str]
@dataclass
class LandLine:
    adress: str
    owner_name: str
@dataclass
class ElectronicDevice:
    charge: str
    region: str
@dataclass
class InsuredObject:
    insurrance_number: str
    insurer: str
    issued: str
    valid: bool

# @dataclass
# if this is a dataclass and init is removed, it does not work
class Phone:
    number: str
    maker: str
    operator: str
    phone_cellphone: CellPhone
    phone_landline = LandLine
    phone_electronicdevice = ElectronicDevice
    phone_insuredobject = InsuredObject

    def __init__(self, number: str, maker: str, operator: str, phone_cellphone: CellPhone, phone_landline: LandLine, phone_electronicdevice: ElectronicDevice, phone_insuredobject: InsuredObject) -> None:
        self.number = number
        self.maker = maker
        self.operator = operator
        self.phone_cellphone = phone_cellphone
        self.phone_electronicdevice = phone_electronicdevice
        self.phone_insuredobject = phone_insuredobject
        self.phone_landline = phone_landline
    
    def __str__(self):
        return f"{self.maker}, {self.phone_insuredobject.insurer}"

# my_variable = Phone("0214958", "Nokia", "Telia", CellPhone("Symbian", 2500, 2007, ["Angry birds", "Maps", "Tinder"]), 
#                    LandLine("Berättelsegatan 24", "Jaget"), ElectronicDevice("60mph", "EU"), InsuredObject("21649", "Metlife", "2007-12-12", True))

# print(my_variable)

# This does not work since all arguments must be given when creating an object. Solve this by args???
# my_other_variable = Phone("0215495", "Nokia", "Telia", CellPhone("Symbian", 2500, 2006, ["Angry birds", "Tinder", "Facebook"], 
#                     ElectronicDevice("60mph", "EU")))
# print(my_other_variable)


# If we donä't use a init-function in a class, we can assign individual values later
# Use a method fro this. Does not work with dataclasses
# dataclasses include an init-function, making this impossible
class TestingIncompleteObjects:
    name: str
    age: int
    properties: List[str]
    married: bool

    # If an init-method is used, we cannot use add_name to define a value.
    # self.name = name can only be defined once per class
    # In @dataclass init-method is automatic if not explicitly overwritten.
    # cannor use add_name() in dataclass, unless we take in all arguments


    def add_name(self, name: str):
        self.name = name


testdude = TestingIncompleteObjects()
testdude.add_name("Mah Dude")
print(testdude.name)
# Change allre3aqdy established name
testdude.add_name("Adolf")
print(testdude.name)
# Set default value






class TestingIncompleteObjects2:
    name: str
    age: int
    properties: List[str]
    married: bool

    # If an init-method is used, we cannot use add_name to define a value.
    # self.name = name can only be defined once per class
    # In @dataclass init-method is automatic if not explicitly overwritten.
    # cannor use add_name() in dataclass, unless we take in all arguments

    def __init__(self, name:str, age: int, properties: List[str], married: bool):
        self.name = name
        self.age = age
        self.properties = properties
        self.married = married

    def __str__(self) -> str:
        return f"I am the great {self.name}, master of {self.properties[0]} och {self.properties[1]}. Married? {self.married}"

testdude2 = TestingIncompleteObjects2("olof", 33, ["Sricka sprit", "hålla käften"], False)
print(testdude2)




@dataclass
class TestingDefaultValues:
    name: str = "hejdu"
    age: int = 34

    # self.name has allready been assigned in the dataclass init method.
    # Cannot be set again testolof.name = "str" will have to be used instead
    def add_name(self, name: str):
        self.name = name

# Cannot change the value when default has been set? Needs another function to do that?
testolof = TestingDefaultValues
testolof.name = "Ruben"
print(testolof.name)
# testolof.add_name("Dasani") # Cannot run add_name when value of name has allready been set
