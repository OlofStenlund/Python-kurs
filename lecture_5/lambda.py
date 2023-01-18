## Ordinary function

def function_1():
    print("Function 1")

def function_2():
    return "Function 2"
    print("Fucntion 2")


# function_1() # Runs funtion_1, printing "Function 1"
# variable_1 = function_1 # Instead of calling the function using (), we save it in a variable. We can then call the variable later
# # # variable_1() # Call the function, by calling the variable the function is stored in. Runs function_1 printing "Function 1"
# # print(function_1) # Prints info about the function

# variable_2 = function_2 # Saves function_2 in variable
# print(variable_2()) # Print return value stored in variable
# variable_2() # Does nothing, as the function only returns a value

# print(function_2, variable_1) # Prints infor on function_2 and variable_1
# print(function_2(), variable_1()) # Prints the return value of function 1(), and none from variable_1() as there is no return value
# print(function_1(), function_2()) # Printin function_1() and variable_1() are the same thing, both returning None
# print(variable_1, variable_2) # prints info about variables (if function_2 is run () when assigning it into variable_2, this would return "Function 2")
# print(variable_1(), variable_2()) # Returns None and "Function 2"
# variable_1() # Returns "Function 1"
# print(variable_2()) # Returns "Function 2"

def first_function(a):
    print("first function", a)

def second_function():
    print("second function")

def third_function():
    return "thrid function"

# first_function("Hej")
# first_function(second_function) # Send the second function in as argument. Executes first function with second function as "a"
# # first_function(second_function()) # Runs second_function (printing "second fucntion") Sends the result of running second_function (none, since nothing is returned), into first function, ptinting "first function none"
# first_function(third_function()) # Result of third_function is "third function", sent into first_function as "a"


## Lambda

# Basis of lambda. Here it is saved in a variable that takes arguments
# Lambda is a function without a name
# my_lambda = lambda a, b: a + b # What is after the colon will be returned
# print(my_lambda(1, 2))
# Don't use variable to use lambda, this is just to show how it works


def first_lambda_function(a):
    print(a(1, 3))
    print("hej", a(1, 5))

first_lambda_function(lambda a, b: a + b)
# lambda function(1+b) is used as an argument in first_lambda_function()
# print(a(1,3)) == print(lambda 1, 3: 1 + 3)
# print("hej", a) prints the function, ie. info about it. (No arguments were given to the function, so id does not run)
# print("hej", a(1,5)) prints "hej" and the result of the lambda


## Let's look at how lambdas are used

# Lambdas are simple functions that are used instead of defning a function that will only be used once
# Variable that contains a list of dictionaries
people= [{"name": "Anders", "age": 30},
            {"name": "Olof", "age": 12},
            {"name": "Ted", "age": 63}]

print(sorted(people, key=lambda person: person["age"])) # Sorted uses "<" to caompare. Does not work on dictionsries. But soretd takes arguments like key, which allow us to use lambda.
# Lambda takes person(x, person is a variable name) as argument, and returns person.age (x.age). Basically for x in people, return x."age" and send that result into sorted.
# Works with person["name"] as well
print(sorted(people, key=lambda person: (person["name"])))

def comapre_name(person): # Create a function to run instead of lambda
    return person["name"]
print(sorted(people, key=comapre_name)) # key takes a function as argument, van be normal or lambda 

# The compare_name function will not be used anywhere else, so it's rather pointless to create it.
# Lambda function can be used instead, as a one of function. Need not be defined, but created just for a singe purpose