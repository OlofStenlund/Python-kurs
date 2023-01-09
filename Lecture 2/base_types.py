# Grundläggande datatyper
# int, integers are whole numbers
# float, floating point numbers, are numbers with decimals
# str, strings, are strings of text
# bool, booleans, binary operator which is either T or F, on or off
# none, equal to null

My_little_integer = 10
print(f"Integer{My_little_integer} - Type: {type(My_little_integer)}")
# Prints a formated string that inputs the variable name to output its values
# type() returns the data type of the content
# When dividing ints, the retun will be float
# Because division can result in floats, all results willl be floats
# Operations with floats will always lead to floats
# If there is a possibility for the result to be float, it wil always be float

Datatyp1 = 5
Int2 = 10
Int3 = 15
Int4 = 20

Datatyp1 + Int2

# To change the name on multiple occations, used ctrl+D

string1 = "Olof"
string2 = "Stenlund"

# To (un)comment several rows ctrl+*

string3 = string1 + string2 # Adding two strings together works
print(string3) 
print(Int2 * string3) # Multiplying string with int prints that string int number of times

boolean1 = True
boolean2 = False

print(boolean1 + boolean2) # true/false is 0/1 so counting can be done
print(boolean1 + boolean1) # true+true = 1+1
print(Int2 * boolean1) # = 10*1
print(Int2 * boolean2) # = 10*0

#none1 = None
#print(Int2 + none1) # Does not work, none is nothing, not a number.
# No operations can be made with none.

floater = 1.0 # "Floater" is a float data type
result = int(floater) # Convert to integer (casting)
print(type(result)) # Print type

stringer1 = "3"
resultagain = int(stringer1)
print(type(resultagain)) # Converted to integer

print(resultagain + Int2) # =3+10

# Can also convert to bool, resulting in a value of 1 or 0
