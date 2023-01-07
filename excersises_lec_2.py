# Övning 1

int1 = 10
float1 = 1.5
str1 = "Hej"
bool1 = True

print(int1+float1)
print(int1+bool1)
print(float1+bool1)

# Övning 2

str2 = "Hej jag heter Ingemar."

print(str2[:5]) # prints from (incuding) 0 up to (not including) 5
print(str2[5:]) # prints from (including) 5 upwards
print(str2[5:-1]) # prints from (including) 5, up to the second last index
print(str2[5:-2]) # prints from (including) 5, up to the third last index
print(str2[4:10]) # prints from index 4 up to (not including) index 10

# Övning 3

list1 = [1, 5, 6, 23, 4, 10]
list2 = [4, 74, 12, 3, 7, 1]
print(list1+list2) # Prints the lists after each other
#print(list1*list2) #No work

list3 = [[1,2,3], [4,5,6], [7,8,9]]
list4 = [["ett", "två", "tre"], [4,5,6], ["sju", "åtta", "nio"]]
print(list3[1]) # Prints index 1 in list ([4,5,6])
print(list3[1][1]*list3[2][0]) # Multiplies the item index 1, index 1 (5) with item index 2, index 0 (7)
print(list3[0][0],list4[0][0]) # prints int and str, does not work with + (as one is a str)

# Övning 4
# Keys in lists must be immutable, ie. cannot change
# int, str, tuples and floats

dict1 = {
    "firstname": "Olof",
    "lastname": "Stenlund",
    "age": 33,
    "location": "Göteborg",
    "married": False,
    "school": {
        "schoolname": "EC Utbildning",
        "location": "Göteborg",
        "employees": 18,
        "taxfunded": True,
        "board": {
            "CEO": "Lasse Larsson",
            "CFO": "Stine Jönsson",
            "CTO": "Lawan Rimo",
            "CPO": "Sickan Karlsson"
        },
    },
}

print(dict1["age"]*dict1["married"]) # prints 0, since marries is false, ie. 0
print(dict1["age"]*dict1["school"]["taxfunded"]) # Prints 33 since "taxfunded is true, ie 1
print(dict1["age"]+dict1["school"]["taxfunded"]) # Prints 34 because 33+1=34

dict1["firstname"] = "Jöns" # Changes "firstname"
print(dict1["firstname"])

age = dict1["age"]
ceo = dict1["school"]["board"]["CEO"]
print(age, type(age), ceo, type(ceo)) # Prints the age, name of CEO and their data types

dict2 = {
    1: "one",
    2: "two"
}

print(dict2[1]) # Prints "one"

# Övning 5
# For loops

print(dict1.keys())
print(dict1.values())

for i in dict1.keys():
    print(i)

for i in dict1.values(): # Prints values on the forst level, everything else on lower levels
    print(i)

