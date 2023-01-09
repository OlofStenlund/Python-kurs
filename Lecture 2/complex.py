# Lists

# Can contain different types of elements

list1 = [] # Square brackets to contain the list
list2 = list() # Use to add items to list?
list3 = [1, 2, 3, 4, 5]
list4 = list(["hej", "Då", 5, True]) # We'll get to this later

listoflists1 = [list3, list4] 
listoflists2 = [[1,2,3], [4,5,6], [7,8,9]]

print(listoflists1)
print(listoflists2)

print(list4[0]) # Prints the first item (number 0) in the list
greeting = (list4[0]) # make a variable out of the result
print(greeting)

print(len(list3)) # Number of elements in the list
print(type(len(list3)))

# get the last index: len-1
list_len = len(list3)
print(list_len) # prints last item in the list
print(list3[list_len-1]) # prints last item in the list
print(list4[-1]) # prints last item in the list

# If you make listn = listx, a change to either will change both.

list1 = list2.copy() #creates a copy (list1 is the copy)

list_slize1 = list4[:2] # selects the item in the list, up till (but not including) item 2
list_slize2 = list4[1:-1] # Prints from item 2 to (not including) last index
list_slize3 = list4[1:] # Print from index 1 up, including last one.
slized = list_slize1 + list_slize2 # Put the slizes into one list
print(slized)

my_string = "Hi, my name is: "
print(my_string[0]) #prints index 0 of the string
print(my_string[0:5]) # Prints index 0-4
print(my_string[-8:-1]) # prints the last 7 indexes (not including the final space)
print(my_string[-1]) # prints the last index (final space)

# if we make a string into a list, the list will contain all the individual characters

# Set
# Order does not matter

set1 = set() # Creates empty set
set2 = {"Olof", "Stenlund"} # cannot be created empty ("{}"), then it will be a dictionary
setlist1 = [1, 1, 2, 2, 2, 3, 4, "Olof", "Olof", "Stenlund", "Stenlund", "Stenlund"]
set3 = set(setlist1) # Takes only the unique items from a list

print(set3)

# Tuples
# Order matters (for unpacking)
# Cannot change the values in a tuple

tuple1 = () # Empty tuple
tuple2 = ("Olof", "Stenlund", "tönt") 
print(tuple2)

name, age, role = tuple2 # Assign connection between words an itmes in tuple
# This is called unpacking. Must be the same number of values
print(role, name) # print the related values


# Dictionaries
# Builds key values
# Key needs to be imutable value. int, string, tuple. 
# Values can be bot mutabla and imutable
# imutable: where the value cannot be changed.

dict1 = {} # Creates empty dictionary
dict2 = dict() # Creates empty dictionary

# key: value
dict4 = {1: "one", "greeting": "Hello", False: "hi!"}
print(dict4)



Olof = {
    "name": "Olof",
    "age": 30,
    "location": "Göteborg",
    "school": {
        "name": "EC Utbildning",
        "location": "Göteborg",
        "board": {
            "CFO": "Lasse",
            "CEO": "Maja"
        },
    },
}

# An item in the dictionary is another dictionary
print(Olof)
Olof_name = Olof["name"] # Returns the value for key "name"
print(Olof_name)

school_name = Olof["school"]["name"] # goes to "shool" and then "name"
print(school_name)


Olof_Name = Olof["name"]
print(Olof_Name)
SchoolCEO = Olof["school"]["board"]["CEO"] # Go to school, then board, then get value of key CEO
print(SchoolCEO)