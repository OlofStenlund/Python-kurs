def function_1():
    print("function_1; the printout")

#function_1()

def function_2():
    print("function_2; the printout")

#function_2()

# We must not call the funtion, we can use it other ways

# variable_1 = function_1
# variable_1()
# Define variable as a function without calling it. The variable then calls the function. (using ())
# Basically, a variable can be a function
# Variables can be overwritten, so beware

def first_function(a):
    print("First function, the prinout", a)
    a()

def second_function():
    print("Second function, the printout")

#first_function("Hej")
#first_function(second_function) # Take second_function as an argument, without calling it
first_function(second_function) # Gets sent in as "a", and if we call a() in first_function, which is the secont function. So the second_function runs.
# First, in the print, "a" is not called, so the funtion is not run, just printed
# second time, a() is run

# Lambda

#my_lambda = lambda a b: a + b

# Lambda function is an anonomus function.
# A function without a name

def lambda_function_func(a):
    print(a(1, 2))

# syntax: lambda a, b: a + b. (first parameter, second parameter: what to return from the function)

lambda_function_func(lambda a, b: a + b) # define the lambda
# Send the lambda function as argument in the function
# In the function, inout "a" is lambda, and the the function calls a() with the values, and excecuted the lambda with those values.

people = [  {"name": "Anton", "age": 30},
            {"name": "Olof", "age": 33},
            {"name": "Jonas", "age": 69}]

print(sorted(people, key=lambda person_var_name: person_var_name["age"])) # Sorted takes a second argument, we can set this as a lambda function
# person_var_name is a variable name for the list we are sorting (people), and then we chose what to sort by person_var_name["age"]

# Let's use a different methos to sort by name
def compare_name(a): 
    return a ["name"]

print(sorted(people, key=compare_name))


# Some other shit

def func_one():
    print("Func 1")

def func_two(func: callable): #Define the argumnet "func" as callable
    func()
    print("Func 2")

#func_two(func_one) # Runs func_one, then func_two

# Decorate a function with another function



def func_four(func: callable): #Define the argumnet "func" as callable
    def wrapper():
        func()
    print("Func 4")
    return wrapper
    
@func_four # can also take arguments as input using ()
def func_three():
    print("Func 2")

func_three()

# What is this nonsense?
# func_three is "decorate" takes in a function, does some logic
# Returns another function, in which the first function is executed
# Allows you to modify how a function works, without haveing to modify the function itself
# Know that a decorator is a function that is run with another function inside it.

