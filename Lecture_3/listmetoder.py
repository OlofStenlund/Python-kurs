# Functions (hio to define them)
# Indentions
# Calling functions
# Parameters
# Argument (position och namngivna)

#Functions
def my_function(): # No input arguments
    print("It's my function")
    return "Hej"
#my_function()
#print(my_function()) # Prints whaterver is "return" in the function. Default is "none" (salso prints the print statement)


def my_function(name):
    print("It's my function " + name)
    return "Hej " + name

#my_function("Olof") # Does not include "return" 
#print(my_function("Olof")) 

def a_general_function(*args, **kwargs): # Arguments and key works argumnets)
    print(args, kwargs)

#a_general_function("A", "B", 1, 2, 3) # Will be entered into args, since key is not defined


def a_general_function(*args, **kwargs): # Arguments and key works argumnets)
    print(args, kwargs)


#a_general_function("A", "B", 1, 2, 3, name="Olof", location="Göteborg") # Kaywords must be put last, positional first


# When run, the arguments are put into args, keywords will be put into kwargs

def my_function(name, *args): # *args catpures all positional arguments after name, which only catches one
    print("It's my function " + name + str(args))
#y_function("olof", 1, 2, 3) # Olof goes into name, the args go into the tupple rest
# * catches positional arguments (just....things) and ** catches key-word-arguments

def my_function(name, *args): 
    a, b, c = args # Gives names to the positions in the tupple
    print("It's my function " + name + str(args))
    print(a, c) # Prints specified elements in the tupple
#my_function("olof", 1, 2, 3)

def my_function(name, *args): # Can you print elements of the tupple without nicknames?
    print("It's my function " + name + str(args))
#my_function("olof", 1, 2, 3)

def generate_person(name, surname, *attributes, is_employed=False, hobbies=[], **kwargs): # is_employed is set to a defautl values, not needed. Default values established here does not require input when calling the function
    print(name, surname, " is a person with ", attributes)
    print(name, " is ")
    if is_employed:
        print("Employed")
    else:
        print("Unemployed")
    print("Hobbies are: ")
    for i in hobbies:
        print(i)
    print("Other info")
    for key, value in kwargs.items():
        print(key, value)

#generate_person("Olof", "Stenlund", "dumb as a rock", "tired", is_employed=True, hobbies=["drinking", "gabling", "hookers"], kids=0, life=False)

def function_without_catchallargs(pos1=None, pos2=None, kw1=None, kw2=None, **kwargs): # without_catchall = without *
    print(pos1, pos2, kw1, kw2, kwargs)
    pass # Tells the function to just do nothing

#function_without_catchallargs("A", "B", hej=2) # Prints pos1, pos2, and kwargs, as those are the arguments defined in calling the function. 
# Works since arguments are defined as none in def

def fuction_without_kwargs(pos1=None, pos2=None, kw1=None, kw2=None): # without_kwargs = without **
    print(pos1, pos2, kw1, kw2)
    pass

#fuction_without_kwargs(1, 2) # Can only enter positional arguments
#fuction_without_kwargs(pos1="Olof", pos2="Bajs") # using key words
#fuction_without_kwargs(pos1="Olof", pos2="Bajs", "jaha", 3) # Does not work, positional arguments must come before key word arguments


# Return values

def a_function_that_returns_an_int():
    return 1

#print(a_function_that_returns_an_int())
#print(type(a_function_that_returns_an_int)) # Returns funtion, you're asking for the actual function
print(type(a_function_that_returns_an_int())) #Returns int, youre asking for the result of the function

def a_function_that_returns_a_list(a, b, c):
    return [a, b, c]

listan = a_function_that_returns_a_list(1, 2, 3)
print(listan)