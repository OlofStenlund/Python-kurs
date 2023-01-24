

def my_function(*args, **kwargs):
    print(f"My function takes in {args} and {kwargs}")

#my_function() # Returns empty tuple and empty dict

#my_function("bajsa", "på", "dig", reason="Fight me", soup=35) # three positional arguments end up in *args, key word adrguments end up in **kwargs

def my_weird_function(self, *args, **kwargs ):
    print(f"My function takes in {args} and {kwargs}")
    
# "bajsa" ends up in "self", as it is a positional argument
# kwargs cannot be put before any positional argument
my_weird_function("bajsa", "på", "dig", reason="Fight me", soup=35)    


def another_function(*args, other, **kwargs):
    print(f"args {args}, other {other}, kwargs{kwargs}")

# "Other" is a named argument. Since it's between position and keyword argeumnets, it must be defined
another_function(1, 2, 3, other="hejdu", bajs="najs", kiss="gött")
# Will not work:
#another_function(1, 2, 3, bajs="najs", kiss="gött")

# Compare the below where others is first, thus need not be defined when calling the function
# IE, the order matters
def otherfunction(other, *args, **kwargs):
    print(f"other should be {other}, args should be {args}, and dict should be {kwargs}")

otherfunction("hallå du!", 1, 2, 3, bajs="jah")


#---------------------


# Unpacking the arguments.
def unpacking(*args, **kwargs):
    a, b, c = args
    e, f, g = kwargs
    print(a, b, c)
    print(e, f, g)
# All arguments will be unpacked
unpacking(1, 2, 3, Hej="hej", Då="då", Idiot="idiot")

# unpack first 3 positional args, the rest are stored in *rest
# Unack first 3 kwargs, rest are storet in *kwrest
def unpacking2(*args, **kwargs):
    a, b, c, *rest = args
    e, f, g, *kwrest = kwargs
    print(a, b, c)
    print(rest)
    print(e, f, g)
    print(kwrest)
# First 3 arguments unpacked
unpacking2(1,2,3,4,5,6, God="god", Morgon="morgon", Min="min", Lilla="lilla", Gurka="gurka")