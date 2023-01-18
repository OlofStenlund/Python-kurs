from typing import List, Tuple
from enum import Enum

class Test1(Enum):
    Fuck = 1
    Shit = 2
    Cunt = 3
    Ass = 4

print(Test1(2).name) # print name of value 2
print(Test1['Cunt'].value) # print value of name 'Cunt'
print(Test1.Ass.value) # Print Test1, value of Ass
print(f"The value of {Test1(4).name} is {Test1.Ass.value}") # The value of Ass is 4
print(f"{Test1(4).name} {Test1(1).name} {Test1(2).name} {Test1(3).name} {Test1.Fuck.value} {Test1.Shit.value} {Test1.Cunt.value} {Test1.Ass.value}")

for i in (Test1): # Enum-Class must be in parenthesis
    print(i.name, "-", i.value) 

for i in (Test1):
    print(i) # i = Test1.Fuck, or Class.Name. Does not include value. Has a value been assigned to the name?
    print(i.value)