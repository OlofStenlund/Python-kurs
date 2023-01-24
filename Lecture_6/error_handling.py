print(Exception)
print(ValueError)
print(ValueError.__base__)

# Errors are classes.
# __base__ shows what the class in based on? Perhaps?
# ValueError.__base__ shows class Exception, are all errors based on exception?
# What is Exception

class Myerror(Exception):
    pass

print(Myerror.__base__)

# Myerror is an exctention to Exception, we extend Exception to include whatever Myerror is.
# An error inherits the class Exception

num = 2
try:
    if num == 0:
        raise ValueError
    elif num == 1:
        raise Myerror
    elif num == 2:
        raise Exception
    else:
        raise # raise without any specificity rasies Exception

except ValueError: # when num == 0
    print("Value error")
except Myerror: # when num == 1
    print(" My own error, sorry")
except Exception: # When num == 2
    print("Exception")
except: # when num != 1, 2, or 3
    print("all exceptions")
else: # Never, since "else" rasises "exception"
    print("All is well")