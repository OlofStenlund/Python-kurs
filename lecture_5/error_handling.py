# # try
# # except
# # else
# finally
# raise
# assert
# custom exceptions

try: # Try this. If faulty, go to except.
    pass
except:
    pass


def do_something(a):
    res = int(a)
    if res < 2:
        raise SyntaxError


# try:
#     print("trying")
#     print(do_something("5"))
# except:
#     print("error")
# runs "do_something" with "5" as an argument

# try:
#     # print("trying")
#     # print(do_something("hej"))
# except:
#     print("error")
# Cannot convert "hej" to int, so except runs (nearest except)


# try:
#     print("trying")
#     print(do_something("hej"))
# except ValueError: # only runs if we get valueerror
#     print("error")
#     print(ValueError)

# Only the first error is returned, in this case assert. print(do_something("hej")) returns valueerror but is not run, since assert was run first and triggered except.
# try:
#     print("trying")
#     #assert 1==2 # checks if an expression is T/F. If false, returns false and trigger except AssertionError
#     print(do_something(1)) # "Hej" triggers ValueError, 1 triggers syntax error in the function, since we told it to.
# except AssertionError:
#     print(AssertionError)
# except ValueError:
#     print("error", ValueError)
# except SyntaxError: # We can raise a syntax error in the function.
#     print(SyntaxError)
# except:
#     print("Catch them all")
# finally: # always runs
#     print("Did it work?")


# errors are also classes
class TooLowNumberValueError(Exception): # "Extends" the class exception. Adds another function to it? Inheritance from that class
    msg: str
    def __init__(self, msg):
        self.msg = msg


def do_something_else(a):
    res = int(a)
    if res < 2:
        raise TooLowNumberValueError("Way to low") # Argument is automatically included. Must be here, in the function. Not in try/except
    return res


try:
    print(do_something_else(1))
except TooLowNumberValueError as e: # Must be saved as a varable, otherwise it does not work (e as in error is standard)
    print(e.msg)

# class extends the class Exception to include our manual exception
# this exception is raised, this creates manuel conditions
# Whattafakk

