
def func_one():
    print("Func 1")

def func_two(a):
    a()
    print("Func 2")

#func_two(func_one) # func_one is used as argument in func_two. func_one is then called (a()) inside func_two

# Decorator takes in a 
def func_three(func):
    print("Func 3")

    def wrapper():
        func()
    return wrapper
    
@func_three()
def func_four():
    print("Func 4")

func_four()

# Using decorator is the same as using func_four = func_three(func_four())
# func_four is now actuallr func_three with func_four saved inside (in the wrapper function)
# Decorators are usually imported things that extend functions to add functionality
# Whatafakkisdisshiet?


## Decorators in classes. Dataclass

